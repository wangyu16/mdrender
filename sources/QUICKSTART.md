# Quick Start Guide

## Prerequisites

Before you begin, you need to install Node.js, which includes npm (Node Package Manager).

### Installing Node.js

1. **Download Node.js:**
   - Go to https://nodejs.org/
   - Download the LTS (Long Term Support) version
   - Run the installer and follow the installation wizard

2. **Verify Installation:**
   Open a command prompt and run:
   ```bash
   node --version
   npm --version
   ```
   
   You should see version numbers for both commands.

## Setup Steps

1. **Install Dependencies:**
   ```bash
   npm install
   ```

2. **Run Tests:**
   ```bash
   npm test
   ```

3. **Start Local Development Server:**
   ```bash
   npm run dev
   ```
   
   Your function will be available at: http://localhost:8787

4. **Test the Function:**
   - Open `demo.html` in your browser
   - Or use curl:
     ```bash
     curl -X POST http://localhost:8787/api/render -H "Content-Type: application/json" -d "{\"markdown\": \"# Hello World\"}"
     ```

## Project Structure

```
markdown-render/
├── src/
│   ├── index.js      # Main serverless function handler
│   ├── parser.js     # Markdown parser with extensible rules
│   └── math.js       # KaTeX integration for math/chemical equations
├── test/
│   └── test.js       # Test suite
├── demo.html         # Full featured demo
├── simple-example.html  # Simple usage example
├── package.json      # Project dependencies
├── wrangler.toml     # Cloudflare Workers config
├── vercel.json       # Vercel config
├── README.md         # Project overview
├── DEPLOYMENT.md     # Detailed deployment guide
└── DENO_DEPLOY.md    # Deno Deploy instructions
```

## Features Overview

### Markdown Support
- ✅ Headers (H1-H6)
- ✅ Bold, Italic, Bold+Italic
- ✅ Inline code and code blocks
- ✅ Links and images
- ✅ Unordered and ordered lists
- ✅ Tables
- ✅ Blockquotes
- ✅ Horizontal rules

### Math & Science
- ✅ Inline math: `$E = mc^2$`
- ✅ Block math: `$$\int x dx$$`
- ✅ Chemical equations: `$\ce{H2O}$`
- ✅ Matrices and complex equations

### Extensibility
- ✅ Custom syntax rules (see `src/parser.js`)
- ✅ Easy to add new patterns
- ✅ Example rules included (highlight, underline)

## Usage Patterns

### Pattern 1: Direct HTML Integration
```html
<div id="content" data-markdown>
# Your Markdown Here
Math: $E = mc^2$
</div>
<script>
  // Fetch and render
  fetch('YOUR_API_URL/api/render', {
    method: 'POST',
    body: JSON.stringify({ markdown: '...' })
  });
</script>
```

### Pattern 2: Dynamic Content
```javascript
async function renderMarkdown(text) {
  const response = await fetch('YOUR_API_URL/api/render', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ markdown: text })
  });
  const { html } = await response.json();
  return html;
}
```

### Pattern 3: Static Site Generation
Pre-render markdown at build time and serve static HTML.

## Customization Examples

### Adding Custom Syntax

Edit `src/parser.js`:

```javascript
export const customRules = [
  // Strikethrough: ~~text~~
  {
    name: 'strikethrough',
    pattern: /~~(.+?)~~/g,
    replace: '<del>$1</del>'
  },
  // Spoiler: ||text||
  {
    name: 'spoiler',
    pattern: /\|\|(.+?)\|\|/g,
    replace: '<span class="spoiler">$1</span>'
  },
  // Custom alert: !!! text
  {
    name: 'alert',
    pattern: /^!!! (.+)$/gm,
    replace: '<div class="alert">$1</div>'
  }
];
```

### Adding Custom Math Macros

Edit `src/math.js` to add KaTeX macros:

```javascript
katex.renderToString(equation, {
  displayMode: true,
  macros: {
    "\\RR": "\\mathbb{R}",
    "\\NN": "\\mathbb{N}"
  }
});
```

## Next Steps

1. **Install Node.js** (if not already installed)
2. **Run `npm install`** to install dependencies
3. **Run `npm test`** to verify everything works
4. **Start development** with `npm run dev`
5. **Deploy** to your preferred platform (see DEPLOYMENT.md)

## Getting Help

- Check `README.md` for feature overview
- Check `DEPLOYMENT.md` for deployment instructions
- Review `demo.html` for usage examples
- Look at `test/test.js` for API examples

## Common Issues

### "npm is not recognized"
- Install Node.js from https://nodejs.org/

### "Module not found"
- Run `npm install` to install dependencies

### "Port already in use"
- Change the port in wrangler.toml or kill the process using port 8787

### Math not rendering
- Make sure KaTeX CSS is included in your HTML
- Check browser console for errors
- Verify LaTeX syntax is correct

## License

MIT - Feel free to use in your projects!
