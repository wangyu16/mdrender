# New Style Templates - Design Inspiration Guide

This document describes the four new style templates added to the mdrender project, which were inspired by reference stylesheets provided in the `temp/` folder.

## Overview

The new templates maintain the two-panel layout architecture (sidebar navigation + content area) while incorporating modern design patterns from the reference stylesheets. All templates support:

- ✅ Custom CSS classes (8 div classes + 5 span classes)
- ✅ Theme switcher integration with localStorage persistence
- ✅ Responsive design for mobile and desktop
- ✅ KaTeX math rendering support
- ✅ Proper typography hierarchy
- ✅ Code syntax highlighting

---

## Template 6: Modern Gradient Light

**File:** `style_template6_modern_gradient.css`

**Inspiration:** Based on `modern-light.css` with purple gradient accents

**Key Features:**
- **Typography:** Inter font family for clean, modern readability
- **Colors:** Purple gradient theme (#8b5cf6 to #a78bfa)
- **Layout:** Wide content area (max-width: 900px) for comfortable reading
- **Design Philosophy:** Contemporary tech aesthetic with gradient effects
- **Special Elements:**
  - Gradient headings and borders
  - Smooth transitions and hover effects
  - CSS custom properties for easy customization
  - Shadow utilities for depth

**Best Use Cases:**
- Tech documentation
- Modern web development tutorials
- SaaS product documentation
- Developer portfolios

**Color Palette:**
- Primary: `#1e293b` (dark slate)
- Accent: `#8b5cf6` (purple)
- Secondary Accent: `#a78bfa` (light purple)
- Background: `#ffffff` (white)
- Surface: `#f8fafc` (light gray)

---

## Template 7: Serif Academic

**File:** `style_template7_serif_academic.css`

**Inspiration:** Based on `academic-light.css` with scholarly design

**Key Features:**
- **Typography:** Merriweather (body) + Montserrat (headings) for traditional scholarly feel
- **Colors:** Blue accent theme (#3498db) with professional gray tones
- **Layout:** Medium content width (max-width: 850px) optimized for long-form reading
- **Design Philosophy:** Classical academic style with modern touches
- **Special Elements:**
  - Justified text with hyphens for print-like appearance
  - Section markers (§) on horizontal rules
  - Drop-quote styling in blockquotes
  - Footnote-ready formatting

**Best Use Cases:**
- Research papers
- Academic course materials
- Educational textbooks
- Formal documentation
- Thesis/dissertation materials

**Color Palette:**
- Primary: `#2c3e50` (dark blue-gray)
- Accent: `#3498db` (bright blue)
- Background: `#ffffff` (white)
- Surface: `#f8f9fa` (light gray)
- Sidebar: `#ecf0f1` (light gray-blue)

---

## Template 8: Minimal Elegant Dark

**File:** `style_template8_minimal_dark.css`

**Inspiration:** Based on `minimal-dark.css` with refined dark mode design

**Key Features:**
- **Typography:** Lato (body) + Raleway (headings) + JetBrains Mono (code)
- **Colors:** Blue accent (#64b5f6) on dark background (#121212)
- **Layout:** Moderate width (max-width: 800px) for focused reading
- **Design Philosophy:** Minimalist dark mode with OLED-friendly true black
- **Special Elements:**
  - Pure black backgrounds (#121212) for OLED screens
  - Subtle borders and shadows
  - Clean, distraction-free interface
  - Smooth color transitions

**Best Use Cases:**
- Night-time reading/coding
- Developer documentation
- Terminal-style documentation
- Privacy-focused content
- Low-light environments

**Color Palette:**
- Primary: `#e8e8e8` (light gray text)
- Accent: `#64b5f6` (blue)
- Background: `#121212` (true black)
- Surface: `#1e1e1e` (dark gray)
- Sidebar: `#0d0d0d` (darker black)

---

## Template 9: Modern Dark Professional

**File:** `style_template9_modern_dark.css`

**Inspiration:** Based on `modern-dark.css` with purple gradient theme

**Key Features:**
- **Typography:** Inter (body/headings) + JetBrains Mono (code)
- **Colors:** Purple gradient theme (#8b5cf6 to #a78bfa) on slate background
- **Layout:** Wider content (max-width: 900px) for comprehensive content
- **Design Philosophy:** Modern professional dark mode with gradient accents
- **Special Elements:**
  - Gradient text effects (WebKit background-clip)
  - Linear gradient borders and dividers
  - Gradient scrollbars
  - Box shadows with color glow effects
  - Smooth gradient transitions

**Best Use Cases:**
- Modern SaaS documentation
- Developer tools documentation
- Tech startup product docs
- API references
- Progressive web app documentation

**Color Palette:**
- Primary: `#f1f5f9` (light slate text)
- Accent: `#8b5cf6` (purple)
- Secondary Accent: `#a78bfa` (light purple)
- Background: `#0f172a` (dark slate)
- Surface: `#1e293b` (medium slate)

---

## Design Patterns Adopted

All new templates incorporate these modern CSS patterns from the reference stylesheets:

### 1. CSS Custom Properties (Variables)
```css
:root {
    --primary-color: #...;
    --accent-color: #...;
    --background: #...;
}
```
Benefits: Easy theming, consistent color usage, maintainability

### 2. Google Fonts Integration
All templates use `@import` to load web fonts for improved typography:
- Inter: Modern geometric sans-serif
- Lato: Friendly humanist sans-serif
- Raleway: Elegant display font
- Merriweather: Classic serif for body text
- Montserrat: Strong geometric headings
- JetBrains Mono: Developer-friendly monospace
- Fira Code: Code-focused monospace

### 3. Gradient Effects
Modern templates (6 & 9) use CSS gradients for:
- Background effects
- Text effects (via background-clip)
- Border decorations
- Button/badge styling
- Smooth color transitions

### 4. Dark Mode Optimization
Dark templates (8 & 9) implement:
- True black (#121212) for OLED screens
- Proper contrast ratios (WCAG compliant)
- Muted accent colors to reduce eye strain
- Subtle borders instead of harsh lines
- Gradient scrollbars

### 5. Custom Class Consistency
All templates maintain visual consistency for custom classes:
- `.callout`, `.tip`, `.warning`, `.note`: Informational boxes
- `.highlight-box`, `.quote-box`, `.alert`, `.success`: Content emphasis
- `.highlight`, `.emphasis`, `.subtle`, `.badge`, `.tag`: Inline styling

---

## Responsive Design

All new templates include mobile-friendly responsive breakpoints:

```css
@media (max-width: 768px) {
    .container { flex-direction: column; }
    .sidebar { width: 100%; }
    .content { padding: 40px 24px; }
}
```

**Mobile Changes:**
- Sidebar moves to top of page
- Navigation becomes horizontal/collapsible
- Content padding adjusts for smaller screens
- Font sizes scale appropriately

---

## Theme Selector Integration

All new themes are integrated into the theme selector dropdown in `index.html`:

```html
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
```

User preferences are persisted via localStorage for seamless experience across sessions.

---

## Testing Checklist

When testing new themes, verify:

- [ ] Theme selector dropdown includes all 9 templates
- [ ] Theme switching works without page reload
- [ ] localStorage saves theme preference
- [ ] All custom classes render correctly (`.callout`, `.tip`, etc.)
- [ ] Code blocks have proper syntax highlighting
- [ ] Math equations (KaTeX) display correctly
- [ ] Navigation sidebar is functional
- [ ] Content area scrolls properly
- [ ] Links and hover effects work
- [ ] Responsive design works on mobile (< 768px)
- [ ] Images display with proper styling
- [ ] Tables render with correct formatting
- [ ] Blockquotes have distinctive styling

---

## Future Enhancements

Potential improvements for the template system:

1. **Theme Variants:** Add light/dark variants for each theme
2. **Font Size Controls:** Add user-adjustable font size slider
3. **Contrast Modes:** High contrast variants for accessibility
4. **Print Styles:** Optimized CSS for printing documentation
5. **Export Themes:** Allow users to export custom theme configurations
6. **Theme Preview:** Add thumbnail previews in theme selector
7. **Syntax Highlighting:** Integrate Prism.js or Highlight.js themes
8. **Animation Options:** Toggle animations for reduced motion preferences

---

## Maintenance Notes

### Adding New Themes

To add a new theme:

1. Create CSS file in `style/` folder (e.g., `style_template10_custom.css`)
2. Follow the two-panel layout structure (`.container`, `.sidebar`, `.content`)
3. Implement all custom classes (`.callout`, `.tip`, etc.)
4. Add responsive breakpoints for mobile
5. Update theme selector in `scripts/generate_site.py`:
   ```python
   <option value="style_template10_custom.css">Custom Theme</option>
   ```
6. Regenerate site: `python3 scripts/generate_site.py`
7. Test theme switching and custom class rendering

### CSS Architecture

Each template should include:
- CSS reset/normalization
- CSS custom properties (`:root` variables)
- Container layout (`.container`, `.sidebar`, `.content`)
- Typography hierarchy (h1-h6, p, lists)
- Code styling (code, pre)
- Interactive elements (links, buttons)
- Custom classes (div and span)
- Responsive breakpoints
- Scrollbar styling (optional)

---

## Credits

**Reference Stylesheets:**
- `minimal-light.css` / `minimal-dark.css`: Inspired Templates 8
- `modern-light.css` / `modern-dark.css`: Inspired Templates 6, 9
- `academic-light.css` / `academic-dark.css`: Inspired Template 7

**Fonts:**
- Google Fonts (fonts.google.com)

**Icon/Emoji:**
- Unicode standard emoji for visual indicators

---

## Summary

The addition of four new templates expands the mdrender project from 5 to 9 professional themes, providing users with diverse visual options for their teaching materials:

1. **Professional** (Original) - Blue accent two-panel
2. **Minimalist** (Original) - Clean black/white
3. **Dark Mode** (Original) - Professional dark theme
4. **Vibrant** (Original) - Colorful purple/pink gradients
5. **Academic** (Original) - Serif fonts with navy/red
6. **Modern Gradient** (NEW) - Purple gradient light theme
7. **Serif Academic** (NEW) - Classical scholarly design
8. **Minimal Dark** (NEW) - Elegant OLED-friendly dark mode
9. **Modern Dark** (NEW) - Purple gradient dark professional

Each theme maintains full compatibility with the theme switcher, custom classes, and responsive design requirements.
