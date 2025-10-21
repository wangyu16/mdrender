# mdrender
Create web pages for documents, handouts, study guides, etc. from markdown files.

## Features

- 🎨 **Nine Modern Style Templates** - Choose from professional, minimalist, dark mode, vibrant, academic, and more
- 🎯 **Dynamic Theme Switcher** - Users can change themes on the fly with a built-in dropdown selector
- 💾 **Theme Persistence** - User's theme preference is saved in localStorage and persists across sessions
- 📝 **Markdown to HTML** - Converts markdown files using a Cloudflare Workers API
- 🎭 **Two-Panel Layout** - Left sidebar navigation with right content panel
- 📱 **Responsive Design** - Auto-collapsing sidebar on narrow screens with toggle button
- � **Optimized Content Width** - Maximum width of 1400px for better readability
- �💅 **Custom CSS Classes** - Special styles for callouts, tips, warnings, and more
- 📐 **KaTeX Math Support** - Beautiful mathematical equations rendering
- � **Smart Layout** - Automatically adapts to screen size with saved preferences

Development environment
-----------------------

This repo includes a VS Code devcontainer configuration in `.devcontainer/` to help
you get started in Codespaces or local containers. The devcontainer image provides
Python 3.11 and will run `pip install -r requirements.txt` after the container is created.

Quick start
-----------

1. Open the repository in Codespaces or Remote - Containers in VS Code.
2. Run the generator:

```bash
python scripts/generate_site.py
```

This will read all `.md` files from the `sources/` directory, call the remote Cloudflare 
render API to convert markdown to HTML, and write the resulting HTML files to `docs/`, 
applying the CSS from the `style/` directory.

The generated website features a two-panel layout:
- **Left panel**: Navigation menu listing all source files
- **Right panel**: Content display area
- **Theme Selector**: Floating dropdown in the top-right corner to switch between themes instantly

Open `docs/index.html` in a web browser to view the generated site.

Style Templates
---------------

Choose from nine professionally designed themes:

### Template 1: Two-Panel Professional (Default)
```bash
python scripts/generate_site.py
# or
python scripts/generate_site.py --style style_template1.css
```
- Clean, modern layout with blue accents
- Best for: Technical documentation, tutorials

### Template 2: Minimalist Clean
```bash
python scripts/generate_site.py --style style_template2_minimalist.css
```
- Ultra-minimal black and white design
- Best for: Essays, blogs, long-form content

### Template 3: Dark Mode Professional
```bash
python scripts/generate_site.py --style style_template3_dark.css
```
- Full dark mode with blue gradients
- Best for: Code documentation, developer resources

### Template 4: Vibrant Colorful
```bash
python scripts/generate_site.py --style style_template4_vibrant.css
```
- Purple/pink gradients with energetic design
- Best for: Creative content, portfolios, presentations

### Template 5: Academic Professional
```bash
python scripts/generate_site.py --style style_template5_academic.css
```
- Traditional scholarly appearance with serif fonts
- Best for: Research papers, academic writing

### Template 6: Modern Gradient (NEW)
```bash
python scripts/generate_site.py --style style_template6_modern_gradient.css
```
- Contemporary purple gradient theme with Inter font
- Best for: Tech documentation, SaaS product docs, developer portfolios

### Template 7: Serif Academic (NEW)
```bash
python scripts/generate_site.py --style style_template7_serif_academic.css
```
- Classical scholarly design with Merriweather and Montserrat fonts
- Best for: Research papers, formal documentation, educational materials

### Template 8: Minimal Dark (NEW)
```bash
python scripts/generate_site.py --style style_template8_minimal_dark.css
```
- Elegant OLED-friendly dark mode with Lato and Raleway fonts
- Best for: Night-time reading, developer documentation, low-light environments

### Template 9: Modern Dark Professional (NEW)
```bash
python scripts/generate_site.py --style style_template9_modern_dark.css
```
- Purple gradient dark theme with Inter font and gradient effects
- Best for: Modern SaaS docs, API references, tech startup documentation

See `docs/STYLE_TEMPLATES_GUIDE.md` for detailed comparisons and `docs/NEW_THEMES_GUIDE.md` for information about the new templates.

Dynamic Theme Switching
-----------------------

The generated website includes a **built-in theme switcher** that allows users to change themes without regenerating the site:

### Features
- 🎨 **Dropdown selector** in the top-right corner with all 9 themes
- 💾 **localStorage persistence** - theme preference is saved automatically
- 🔄 **Instant switching** - no page reload required
- 📱 **Mobile-friendly** - responsive design on all devices

### How It Works
1. Users click the theme dropdown in the top-right corner
2. Select any of the nine available themes
3. The page style changes instantly
4. Preference is saved in browser localStorage
5. Theme persists across page refreshes and visits

### Technical Details
- Uses JavaScript to swap CSS files dynamically
- Stores preference in `localStorage.setItem('preferred-theme', themeName)`
- Automatically loads saved preference on page load
- Falls back to the default theme generated during build

**Note:** The theme selector is only available in the main `index.html` page. Individual content pages use the style specified during generation.

Responsive Layout
-----------------

The website automatically adapts to different screen sizes for optimal viewing:

### Features
- 📏 **Maximum Content Width**: 1400px for comfortable reading on large screens
- 🔲 **Auto-Collapsing Sidebar**: Hides automatically on screens ≤1200px wide
- ☰ **Toggle Button**: Hamburger menu in top-left to show/hide navigation
- 💾 **State Persistence**: Remembers sidebar preference via localStorage
- 📱 **Mobile Optimized**: Compact controls and touch-friendly design

### Behavior by Screen Size

**Wide Screens (>1200px)**
- Sidebar always visible
- Content centered with max-width
- Toggle button hidden
- Traditional two-panel layout

**Narrow Screens (≤1200px)**
- Sidebar hidden by default
- Toggle button (☰) appears
- Click to show/hide sidebar
- Full-width content area

**Mobile (≤768px)**
- Compact theme selector
- Smaller toggle button
- Optimized spacing
- Touch-friendly controls

See `RESPONSIVE_LAYOUT_FEATURE.md` for detailed technical documentation.

Custom CSS Classes
------------------

All templates support special CSS classes for enhanced styling:

### Div Block Classes
- `.callout` - Important information boxes
- `.tip` - Helpful hints (blue themed)
- `.warning` - Caution notices (yellow/orange themed)
- `.note` - Supplementary information
- `.highlight-box` - Featured content
- `.quote-box` - Stylized quotations
- `.alert` - Urgent messages (red themed)
- `.success` - Positive feedback (green themed)

### Span Inline Classes
- `.highlight` - Highlighted text with bright background
- `.emphasis` - Strong emphasis with themed color
- `.subtle` - Muted text for less important info
- `.badge` - Status labels (pill-shaped)
- `.tag` - Category tags (light background)

**Example Usage:**
```markdown
:::tip
💡 This is a helpful tip with special styling!
:::

This sentence has {.highlight}highlighted text{/} and a {.badge}NEW{/} badge.
```

See `sources/CUSTOM_CLASSES_FEATURE.md` for comprehensive examples.

Options
-------

```bash
python scripts/generate_site.py --style <css-filename> --api-url <custom-api-url>
```

- `--style`: CSS file from `style/` directory (default: `style_template1.css`)
- `--api-url`: Custom markdown render API endpoint (default: Cloudflare Workers API)

Project Structure
-----------------

```
mdrender/
├── .devcontainer/          # Codespace configuration
├── docs/                   # Generated website output
│   ├── index.html         # Main page with navigation
│   └── *.html             # Individual content pages
├── sources/                # Markdown source files
│   ├── index.md
│   ├── CUSTOM_CLASSES_FEATURE.md
│   └── *.md
├── style/                  # CSS theme templates
│   ├── style_template1.css               # Professional (default)
│   ├── style_template2_minimalist.css    # Minimalist
│   ├── style_template3_dark.css          # Dark mode
│   ├── style_template4_vibrant.css       # Vibrant colorful
│   └── style_template5_academic.css      # Academic
├── scripts/
│   └── generate_site.py   # Site generator script
├── temp/
│   └── custom-classes-demo.html  # Interactive class showcase
└── README.md
```

Contributing
------------

To add a new style template:

1. Copy an existing template from `style/`
2. Rename it (e.g., `style_template_custom.css`)
3. Customize colors, fonts, spacing, and custom classes
4. Generate with `--style style_template_custom.css`

All templates should include:
- Two-panel layout (`.container`, `.sidebar`, `.content`)
- Responsive design (`@media` queries)
- Custom class support (`.callout`, `.tip`, etc.)
- KaTeX math styling
- Navigation highlighting

License
-------

See LICENSE file for details.
