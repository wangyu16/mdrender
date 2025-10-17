# Style Templates Comparison Guide

This guide compares all five available style templates for the mdrender static site generator.

## Quick Reference Table

| Template | File Name | Style | Best For | Color Scheme |
|----------|-----------|-------|----------|--------------|
| **Template 1** | `style_template1.css` | Two-Panel Professional | Technical docs, tutorials | Blue on dark gray |
| **Template 2** | `style_template2_minimalist.css` | Minimalist Clean | Essays, blogs, long-form | Black, white, minimal |
| **Template 3** | `style_template3_dark.css` | Dark Mode Professional | Code docs, dev resources | Blue gradients on black |
| **Template 4** | `style_template4_vibrant.css` | Vibrant Colorful | Creative content, portfolios | Purple/pink gradients |
| **Template 5** | `style_template5_academic.css` | Academic Professional | Research papers, formal docs | Navy and red accents |

## Template Details

### Template 1: Two-Panel Professional (Default)

**File:** `style_template1.css`

**Characteristics:**
- Clean, modern two-panel layout
- Dark sidebar (#2c3e50) with light content area
- Blue accent color (#3498db)
- Sans-serif fonts (system fonts)
- Professional and approachable

**Use Cases:**
- Software documentation
- Technical tutorials
- Product guides
- Training materials

**Custom Classes:**
- Colored left borders on callout boxes
- Subtle backgrounds with shadows
- Blue active navigation highlight

---

### Template 2: Minimalist Clean

**File:** `style_template2_minimalist.css`

**Characteristics:**
- Ultra-minimal aesthetic
- Light gray sidebar (#fafafa) with thin border
- Black and white primary palette
- Subtle hover effects
- Inter/system font stack
- Maximum readability focus

**Use Cases:**
- Blog posts
- Essays and articles
- Long-form content
- Distraction-free reading

**Custom Classes:**
- Minimal borders and backgrounds
- Understated accent colors
- Clean, flat design elements

---

### Template 3: Dark Mode Professional

**File:** `style_template3_dark.css`

**Characteristics:**
- Full dark mode (#0a0a0a background)
- Blue gradient accents
- High contrast for readability
- Fira Sans font family
- Glowing effects and shadows
- Code-friendly styling

**Use Cases:**
- Developer documentation
- Code tutorials
- Technical blogs
- Late-night reading

**Custom Classes:**
- Gradient borders and backgrounds
- Vibrant accent colors on dark
- Enhanced code block styling
- Glowing hover effects

---

### Template 4: Vibrant Colorful

**File:** `style_template4_vibrant.css`

**Characteristics:**
- Purple/pink gradient themes
- Frosted glass sidebar effect
- Multiple gradient applications
- Poppins/Nunito fonts
- Playful and energetic
- High visual impact

**Use Cases:**
- Creative portfolios
- Design showcases
- Marketing materials
- Educational content for younger audiences

**Custom Classes:**
- Multiple gradient backgrounds
- Rainbow-like color palette
- Floating effects and shadows
- Bold, eye-catching design

---

### Template 5: Academic Professional

**File:** `style_template5_academic.css`

**Characteristics:**
- Traditional scholarly appearance
- Georgia serif fonts for body text
- Navy (#16213e) and red (#e94560) accents
- Formal typography
- Citation-friendly styles
- Print-like aesthetics

**Use Cases:**
- Research papers
- Academic writing
- Formal documentation
- Educational materials
- Conference papers

**Custom Classes:**
- Automatic "Note:", "Warning:" prefixes
- Serif quote styling
- Section markers (§)
- Academic color palette

## Custom Classes Support

All templates support the following custom classes:

### Div Block Classes

| Class | Purpose | Visual Style |
|-------|---------|--------------|
| `.callout` | Important information | Bordered box with distinct background |
| `.tip` | Helpful hints | Light blue/cyan themed |
| `.warning` | Cautions | Yellow/orange themed |
| `.note` | Supplementary info | Neutral themed |
| `.highlight-box` | Featured content | Bright/prominent styling |
| `.quote-box` | Quotations | Italic, styled borders |
| `.alert` | Urgent messages | Red/error themed |
| `.success` | Positive feedback | Green themed |

### Span Inline Classes

| Class | Purpose | Visual Style |
|-------|---------|--------------|
| `.highlight` | Text highlighting | Bright background |
| `.emphasis` | Strong emphasis | Bold, themed color |
| `.subtle` | De-emphasized text | Muted gray |
| `.badge` | Status labels | Pill-shaped, bold |
| `.tag` | Categories | Light background, border |

## Choosing the Right Template

### For Technical Documentation
- **Best:** Template 1 (Professional) or Template 3 (Dark)
- **Why:** Clear structure, code-friendly, familiar layout

### For Academic Writing
- **Best:** Template 5 (Academic)
- **Why:** Traditional typography, citation support, formal appearance

### For Creative Content
- **Best:** Template 4 (Vibrant)
- **Why:** Eye-catching, modern, engaging visuals

### For Long-Form Reading
- **Best:** Template 2 (Minimalist)
- **Why:** Distraction-free, maximum readability, clean design

### For Developer Resources
- **Best:** Template 3 (Dark)
- **Why:** Dark mode, syntax highlighting friendly, modern aesthetic

## How to Use Different Templates

### Command Line

```bash
# Default template (Template 1)
python3 scripts/generate_site.py

# Minimalist template
python3 scripts/generate_site.py --style style_template2_minimalist.css

# Dark mode template
python3 scripts/generate_site.py --style style_template3_dark.css

# Vibrant template
python3 scripts/generate_site.py --style style_template4_vibrant.css

# Academic template
python3 scripts/generate_site.py --style style_template5_academic.css
```

### Switching Templates

To change your site's appearance:

1. Regenerate with the desired template
2. All pages will use the new styling
3. Custom classes adapt automatically
4. No markdown changes needed!

## Customizing Templates

Each template can be customized by editing the CSS file in the `style/` directory:

1. Copy a template file (e.g., `style_template1.css`)
2. Rename it (e.g., `style_my_custom.css`)
3. Modify colors, fonts, spacing as needed
4. Generate with `--style style_my_custom.css`

### Key Variables to Customize

- **Sidebar colors:** `.sidebar { background: ... }`
- **Accent colors:** `.sidebar nav a.active { background: ... }`
- **Fonts:** `body { font-family: ... }`
- **Content width:** `main { max-width: ... }`
- **Custom class colors:** `.callout`, `.tip`, etc.

## Performance Notes

All templates:
- Use system fonts (no external font loading)
- Minimal CSS size (< 10KB each)
- No JavaScript required
- Mobile responsive
- Print-friendly

## Browser Compatibility

All templates support:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers
- Graceful degradation for older browsers

---

**Need help choosing?** Start with Template 1 (default) and experiment with others until you find your perfect match!
