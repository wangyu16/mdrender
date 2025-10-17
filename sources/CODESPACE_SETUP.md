# Codespace Configuration Guide

This document explains the Codespace setup for the mdrender project.

## Overview

The mdrender project is a static website generator that converts Markdown files into a beautiful two-panel HTML website suitable for teaching materials, handouts, study guides, and research summaries.

## Codespace Configuration

### DevContainer Setup

The project includes a `.devcontainer/devcontainer.json` configuration that:

1. **Base Image**: Uses `mcr.microsoft.com/devcontainers/python:3.11`
   - Provides Python 3.11 environment
   - Includes common Python development tools

2. **Features**:
   - Docker-in-Docker support for containerized workflows

3. **VS Code Extensions** (automatically installed):
   - `ms-python.python` - Python language support
   - `esbenp.prettier-vscode` - Code formatting
   - `ms-vscode-remote.remote-containers` - Remote container support

4. **Post-Create Command**:
   - Automatically runs `pip install -r requirements.txt`
   - Installs the `requests` library needed for API calls

### Alternative: Alpine Linux Container

If you're using an Alpine Linux container (as in the current environment):

```bash
# Install Python and required packages
sudo apk add py3-pip py3-requests

# Or install via pip
python3 -m pip install -r requirements.txt
```

## Project Structure

```
mdrender/
├── .devcontainer/
│   └── devcontainer.json       # Codespace configuration
├── docs/                       # Generated website output
│   ├── index.html             # Main page with navigation
│   └── *.html                 # Individual content pages
├── sources/                    # Markdown source files
│   ├── index.md
│   └── *.md
├── style/                      # CSS themes
│   └── style_template1.css    # Default two-panel theme
├── scripts/
│   └── generate_site.py       # Site generator script
├── temp/
│   └── demo.html              # API usage example
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## How It Works

### 1. Markdown to HTML Conversion

The generator script (`scripts/generate_site.py`) uses a publicly available Cloudflare Workers API to convert Markdown to HTML:

- **API URL**: `https://markdown-render.fishdream-82.workers.dev/api/render`
- **Method**: POST
- **Payload**: `{"markdown": "...", "includeKatexCSS": false}`
- **Response**: `{"html": "..."}`

### 2. Two-Panel Layout

The generated website features:

- **Left Sidebar**: 
  - Dark-themed navigation panel
  - Lists all source documents
  - Highlights active selection
  - Fixed width (280px) with scroll

- **Right Content Panel**:
  - Clean white background
  - Displays selected content
  - Maximum width 900px for readability
  - Full KaTeX math support

### 3. Dynamic Content Loading

The main `index.html` uses JavaScript to:
- Load content files dynamically without page refresh
- Update navigation highlight
- Parse and extract main content from loaded pages

## Usage

### Generate the Website

```bash
# Basic usage (uses defaults)
python3 scripts/generate_site.py

# Custom style theme
python3 scripts/generate_site.py --style custom_theme.css

# Custom API endpoint
python3 scripts/generate_site.py --api-url https://your-api.com/render
```

### Preview the Website

```bash
# Start a local web server
cd docs
python3 -m http.server 8000

# Open in browser
# http://localhost:8000/index.html
```

### Add New Content

1. Create a new `.md` file in the `sources/` directory
2. Run the generator script
3. The new page will automatically appear in the navigation

## Customization

### Creating a New Style Theme

1. Copy `style/style_template1.css` to a new file
2. Modify the CSS variables and styles:
   - `.sidebar` - Navigation panel styling
   - `.content` - Main content area
   - Typography, colors, spacing

3. Generate with your theme:
   ```bash
   python3 scripts/generate_site.py --style your_theme.css
   ```

### Key CSS Classes

- `.container` - Main flex container
- `.sidebar` - Left navigation panel
- `.content` - Right content area
- `nav a.active` - Active navigation link
- Code blocks, tables, blockquotes have custom styling

## Dependencies

### Python Packages

- **requests**: HTTP library for API calls
  - Used to POST markdown to the render API
  - Handles JSON payloads and responses

### External Resources

- **KaTeX CSS**: Math rendering support
  - CDN: `https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css`
  - Automatically included in generated pages

## Troubleshooting

### Issue: Module 'requests' not found

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
# or
sudo apk add py3-requests  # Alpine Linux
```

### Issue: Permission denied (Alpine)

**Solution**: Use sudo for system package installation
```bash
sudo apk add py3-pip py3-requests
```

### Issue: API call fails

**Check**:
1. Internet connectivity
2. API endpoint is accessible
3. Request timeout (default 30s)

### Issue: CSS not loading

**Check**:
1. Relative path in `docs/*.html` points correctly to `../style/`
2. Style file exists in `style/` directory
3. Browser developer console for 404 errors

## Best Practices

1. **Organize Sources**: Use subdirectories in `sources/` for better organization
2. **Meaningful Filenames**: Use descriptive names (e.g., `lecture-01-intro.md`)
3. **Test Locally**: Preview before deploying
4. **Version Control**: Commit source files, optionally ignore `docs/`
5. **Math Equations**: Use KaTeX syntax for mathematical notation

## Deployment

The generated `docs/` folder contains static HTML files that can be deployed to:

- **GitHub Pages**: Enable in repository settings
- **Netlify**: Drag and drop the `docs/` folder
- **Vercel**: Deploy as a static site
- **Any web server**: Copy files to web root

## Future Enhancements

Potential improvements:
- Search functionality across all pages
- Dark mode toggle
- PDF export of rendered pages
- Custom navigation hierarchy
- Tags and categories
- Breadcrumb navigation

---

For more information, see [README.md](README.md)
