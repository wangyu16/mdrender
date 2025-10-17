#!/usr/bin/env python3
"""
Generate static site HTML files from markdown sources using a remote Markdown render API.

Usage:
  python scripts/generate_site.py [--api-url URL] [--style STYLE_FILE]

The script reads all `.md` files from the `sources/` directory and writes `.html`
files into the `docs/` directory. It wraps the returned HTML with a simple page
frame that links the chosen CSS file from `style/`.
"""
import os
import sys
import json
import argparse
from pathlib import Path
import requests
import urllib.request


HERE = Path(__file__).resolve().parent.parent
SOURCES = HERE / "sources"
STYLE_DIR = HERE / "docs/style"
DOCS = HERE / "docs"
PRISM_DIR = DOCS / "prism"

# Cloudflare Workers API - publicly available
API_URL = "https://markdown-render.fishdream-82.workers.dev/api/render"

# Prism.js CDN resources
PRISM_RESOURCES = {
    "prism-tomorrow.min.css": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css",
    "prism-line-numbers.min.css": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css",
    "prism-toolbar.min.css": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/toolbar/prism-toolbar.min.css",
}


def find_markdown_files(src: Path):
    return sorted(p for p in src.glob("**/*.md") if p.is_file())


def download_prism_resources():
    """Download Prism.js CSS files locally to avoid CDN issues with GitHub Pages."""
    PRISM_DIR.mkdir(parents=True, exist_ok=True)
    
    for filename, url in PRISM_RESOURCES.items():
        filepath = PRISM_DIR / filename
        
        # Skip if already downloaded
        if filepath.exists():
            print(f"Prism resource already exists: {filename}")
            continue
        
        try:
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, filepath)
            print(f"Downloaded: {filepath}")
        except Exception as e:
            print(f"Warning: Failed to download {filename}: {e}", file=sys.stderr)


def call_render_api(api_url: str, markdown: str):
    payload = {"markdown": markdown, "includeKatexCSS": False}
    resp = requests.post(api_url, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    # Expecting {"html": "..."}
    return data.get("html", "")


def make_page(title: str, body_html: str, style_href: str = None):
    """Generate a single content HTML page."""
    style_link = f'<link rel="stylesheet" href="{style_href}">' if style_href else ""
    katex_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">'
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title}</title>
  {katex_css}
  {style_link}
  <!-- Prism.js theme - Tomorrow Night -->
  <link href="prism/prism-tomorrow.min.css" rel="stylesheet" />

  <!-- Prism.js plugins -->
  <link href="prism/prism-line-numbers.min.css" rel="stylesheet" />
  <link href="prism/prism-toolbar.min.css" rel="stylesheet" />

  <!-- Override theme CSS to preserve Prism syntax highlighting -->
  <style>
    pre code {{
      color: inherit !important;
    }}
    
    code[class*="language-"],
    pre[class*="language-"] {{
      color: inherit !important;
    }}
  </style>

</head>
<body>
<main>
{body_html}
</main>
</body>
</html>
"""


def make_index_page(file_list, style_href: str = None):
    """Generate the main index page with two-panel layout and theme selector."""
    style_link = f'<link id="theme-stylesheet" rel="stylesheet" href="{style_href}">' if style_href else ""
    katex_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">'
    prism_css = """<!-- Prism.js theme - Tomorrow Night -->
  <link href="prism/prism-tomorrow.min.css" rel="stylesheet" />

  <!-- Prism.js plugins -->
  <link href="prism/prism-line-numbers.min.css" rel="stylesheet" />
  <link href="prism/prism-toolbar.min.css" rel="stylesheet" />"""
    
    # Build the navigation list
    nav_items = []
    for filename in file_list:
        display_name = filename.replace(".html", "").replace("-", " ").replace("_", " ").title()
        nav_items.append(f'<li><a href="#" data-page="{filename}">{display_name}</a></li>')
    
    nav_html = "\n        ".join(nav_items)
    first_page = file_list[0] if file_list else ""
    
    # Get the base style filename (e.g., "style_template1.css" from "../style/style_template1.css")
    default_theme = style_href.split('/')[-1] if style_href else "style_template1.css"
    
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Learning Materials</title>
  {katex_css}
  {style_link}
  {prism_css}
  <!-- Override theme CSS to preserve Prism syntax highlighting -->
  <style>
    pre code {{
      color: inherit !important;
    }}
    
    code[class*="language-"],
    pre[class*="language-"] {{
      color: inherit !important;
    }}
    
    .theme-selector {{
      position: fixed;
      top: 20px;
      right: 20px;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.95);
      padding: 12px 18px;
      border-radius: 10px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: system-ui, -apple-system, sans-serif;
    }}
    
    .theme-selector label {{
      font-weight: 600;
      font-size: 14px;
      color: #333;
      white-space: nowrap;
    }}
    
    .theme-selector select {{
      padding: 6px 12px;
      border-radius: 6px;
      border: 2px solid #ddd;
      font-size: 14px;
      cursor: pointer;
      background: white;
      min-width: 180px;
      transition: border-color 0.3s ease;
    }}
    
    .theme-selector select:hover {{
      border-color: #3b82f6;
    }}
    
    .theme-selector select:focus {{
      outline: none;
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }}
    
    @media (max-width: 768px) {{
      .theme-selector {{
        top: 10px;
        right: 10px;
        padding: 8px 12px;
        flex-direction: column;
        gap: 6px;
      }}
      
      .theme-selector label {{
        font-size: 12px;
      }}
      
      .theme-selector select {{
        font-size: 13px;
        min-width: 150px;
      }}
    }}
  </style>
</head>
<body>
  <div class="theme-selector">
    <label for="theme-select">🎨 Theme:</label>
    <select id="theme-select" onchange="changeTheme(this.value)">
      <option value="style_template1.css">Professional</option>
      <option value="style_template2_minimalist.css">Minimalist</option>
      <option value="style_template3_dark.css">Dark Mode</option>
      <option value="style_template4_vibrant.css">Vibrant</option>
      <option value="style_template5_academic.css">Academic</option>
      <option value="style_template6_modern_gradient.css">Modern Gradient</option>
      <option value="style_template7_serif_academic.css">Serif Academic</option>
      <option value="style_template8_minimal_dark.css">Minimal Dark</option>
      <option value="style_template9_modern_dark.css">Modern Dark</option>
    </select>
  </div>

  <div class="container">
    <aside class="sidebar">
      <h2>Contents</h2>
      <nav>
        <ul>
        {nav_html}
        </ul>
      </nav>
    </aside>
    <main class="content" id="main-content">
      <p>Loading...</p>
    </main>
  </div>
  
  <script>
    // Theme switching functionality
    function changeTheme(themeName) {{
      const themeLink = document.getElementById('theme-stylesheet');
      const stylePath = themeLink.href.split('/').slice(0, -1).join('/');
      themeLink.href = stylePath + '/' + themeName;
      
      // Save preference to localStorage
      localStorage.setItem('preferred-theme', themeName);
      
      console.log('Theme changed to:', themeName);
    }}
    
    // Load saved theme preference on page load
    function loadSavedTheme() {{
      const savedTheme = localStorage.getItem('preferred-theme');
      const themeSelect = document.getElementById('theme-select');
      
      if (savedTheme) {{
        themeSelect.value = savedTheme;
        changeTheme(savedTheme);
      }} else {{
        // Set default theme in dropdown
        const currentTheme = '{default_theme}';
        themeSelect.value = currentTheme;
      }}
    }}
    
    // Load content dynamically
    async function loadPage(filename) {{
      const contentDiv = document.getElementById('main-content');
      try {{
        const response = await fetch(filename);
        if (!response.ok) throw new Error('Failed to load page');
        const html = await response.text();
        
        // Extract the main content from the loaded page
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const mainContent = doc.querySelector('main');
        
        if (mainContent) {{
          contentDiv.innerHTML = mainContent.innerHTML;
        }} else {{
          contentDiv.innerHTML = html;
        }}
        
        // Update active link
        document.querySelectorAll('.sidebar nav a').forEach(a => {{
          a.classList.remove('active');
        }});
        document.querySelector(`[data-page="${{filename}}"]`)?.classList.add('active');
      }} catch (error) {{
        contentDiv.innerHTML = '<p>Error loading content.</p>';
        console.error(error);
      }}
    }}
    
    // Set up navigation
    document.querySelectorAll('.sidebar nav a').forEach(link => {{
      link.addEventListener('click', (e) => {{
        e.preventDefault();
        const page = e.target.getAttribute('data-page');
        loadPage(page);
      }});
    }});
    
    // Initialize on page load
    window.addEventListener('DOMContentLoaded', () => {{
      loadSavedTheme();
      
      // Load first page
      if ('{first_page}') {{
        loadPage('{first_page}');
      }}
    }});
  </script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-url", help="Render API URL", default=API_URL)
    parser.add_argument("--style", help="CSS filename in style/ to apply", default="style_template1.css")
    args = parser.parse_args()

    api_url = args.api_url
    style_file = STYLE_DIR / args.style

    if not SOURCES.exists():
        print("sources/ directory not found", file=sys.stderr)
        sys.exit(2)

    DOCS.mkdir(parents=True, exist_ok=True)
    
    # Download Prism.js CSS files locally
    download_prism_resources()

    md_files = find_markdown_files(SOURCES)
    if not md_files:
        print("No markdown files found in sources/", file=sys.stderr)
        sys.exit(0)

    style_href = None
    if style_file.exists():
        # copy or reference relative path from docs to style
        rel = os.path.relpath(style_file, DOCS)
        style_href = rel.replace('\\', '/')

    generated_files = []
    
    for md in md_files:
        with open(md, "r", encoding="utf-8") as f:
            md_text = f.read()

        print(f"Rendering {md} -> using API {api_url}")
        try:
            html = call_render_api(api_url, md_text)
        except Exception as e:
            print(f"Failed to render {md}: {e}", file=sys.stderr)
            continue

        title = md.stem
        page = make_page(title, html, style_href=style_href)

        out_path = DOCS / (md.stem + ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"Wrote {out_path}")
        generated_files.append(md.stem + ".html")

    # Generate index.html with two-panel layout
    if generated_files:
        index_page = make_index_page(generated_files, style_href=style_href)
        index_path = DOCS / "index.html"
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_page)
        print(f"Wrote {index_path}")
        print(f"\nGenerated {len(generated_files)} page(s). Open {index_path} in a browser.")
    else:
        print("No files were generated.", file=sys.stderr)


if __name__ == "__main__":
    main()
