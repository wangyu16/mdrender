# Style Components & Structure Guide

## CSS Components Present in All Themes

Every theme file (`style_templateX.css`) includes these essential components:

### 1. **CSS Reset & Base Styles**
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: (theme-specific font stack)
  line-height: (1.6-1.85)
  color: (theme color)
  background: (theme background)
}
```

### 2. **Layout System**
- **Container** - Flex layout for two-panel design
  - Height: 100vh (full viewport height)
  - Overflow: hidden (prevents double scrollbars)
  
- **Sidebar** - Left navigation panel
  - Width: 250-280px
  - Background: Theme-specific color/gradient
  - Flex-shrink: 0 (maintains width)
  - Overflow-y: auto (scrollable content)

- **Content** - Main reading area
  - Flex: 1 (takes remaining space)
  - Padding: 40-50px (breathing room)
  - Overflow-y: auto (independent scrolling)

### 3. **Typography Styles**
- **H1-H6** - Heading hierarchy
  - Different font sizes (2.6em down to 0.95em)
  - Margin and padding for spacing
  - Border-bottom or color accents
  - Line-height: 1.2-1.3 (tight for headings)

- **Paragraphs**
  - Margin: 1-1.4em (spacing between paragraphs)
  - Font-size: 1-1.06em (readable body text)
  - Line-height: 1.65-1.85 (comfortable for reading)

- **Lists**
  - Padding-left: 2-2.4em (proper indentation)
  - Margin: 1-1.4em (spacing)
  - Li margin: 0.5-0.8em (item spacing)

### 4. **Interactive Elements**

#### Links
- Color: Theme-specific (blue, green, cyan, etc.)
- Transition: 0.2-0.3s ease
- Hover: Color change + underline

#### Sidebar Navigation Links
- Padding: 8-10px
- Border-radius: 3-6px
- Hover state: Background color change, optional transform
- Active state: Accent color with left border

#### Blockquotes
- Border-left: 3-4px solid
- Padding-left: 1-1.4em
- Background: Theme-specific (often semi-transparent)
- Font-style: italic
- Color: Muted/greyed

### 5. **Data Presentation**

#### Tables
- Border-collapse: collapse
- Width: 100%
- Margin: 1.3-1.8em

**Header Row (th)**
- Background: Theme accent color or gradient
- Color: White (for contrast)
- Font-weight: 600-700
- Padding: 11-13px

**Body Cells (td)**
- Border: 1px solid (theme-appropriate color)
- Padding: 11-13px

**Alternating Rows**
- Even rows: Lighter background
- Hover: Slightly darker background

#### Code Blocks
- Styled by Prism.js (external plugin)
- Theme CSS ensures compatibility

### 6. **Media & Visual Elements**

#### Images
- Max-width: 100% (responsive)
- Height: auto (maintains aspect ratio)
- Border-radius: 0-8px (varies by theme)
- Box-shadow: 0 2-4px 8-15px (theme-appropriate)
- Margin: 1-1.2em
- Border: Optional, theme-specific color

#### Marks/Highlights
- Background: Theme-specific color
- Color: Contrasting text color
- Padding: 2-4px
- Border-radius: 2-3px

### 7. **Advanced Features**

#### KaTeX Math Display
- Margin: 1.5-1.8em
- Overflow-x: auto (for wide equations)
- Separate error styling

#### Horizontal Rules
- Border: none
- Border-top: 1-2px solid
- Margin: 2-2.4em
- Optional opacity

### 8. **Scrollbar Customization**
```css
::-webkit-scrollbar { width: 7-8px; }
::-webkit-scrollbar-track { background: (theme color); }
::-webkit-scrollbar-thumb { 
  background: (theme accent);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { 
  background: (lighter theme accent);
}
```

### 9. **Responsive Design**
```css
@media (max-width: 768px) {
  .container {
    flex-direction: column; /* Stack vertically */
  }
  
  .sidebar {
    width: 100%;
    height: auto;
    max-height: 200px; /* Limited height */
  }
  
  .content {
    padding: 20-25px; /* Reduced padding */
  }
}
```

## Theme Variation Points

While all themes include these components, they vary in:

1. **Color Scheme**
   - Primary color (sidebar background)
   - Accent color (links, highlights)
   - Text color (light or dark)
   - Background color (light or dark)

2. **Typography**
   - Font families (sans-serif vs serif)
   - Font weights
   - Letter spacing
   - Text alignment (default vs justified)

3. **Spacing**
   - Line heights (1.6-1.85)
   - Padding/margins
   - Border sizes

4. **Visual Effects**
   - Gradients (solid colors vs gradients)
   - Shadows (subtle vs pronounced)
   - Border radius (sharp vs rounded)
   - Transforms (hover effects)

5. **Accessibility**
   - Contrast ratios
   - Border styles
   - Color combinations

## File Size & Performance

| Theme | File Size | Compression |
|-------|-----------|-------------|
| Professional | 3.9 KB | Baseline |
| Minimalist | 4.1 KB | +5% |
| Dark Mode | 4.1 KB | +5% |
| Vibrant | 4.7 KB | +20% |
| Academic | 4.3 KB | +10% |
| Modern Gradient | 4.5 KB | +15% |
| Serif Academic | 4.4 KB | +13% |
| Minimal Dark | 4.1 KB | +5% |
| Modern Dark | 4.5 KB | +15% |

**Average:** 4.2 KB per theme (uncompressed)
**Gzipped:** ~1.2-1.5 KB per theme

## Adding New Themes

To create a new theme:

1. **Copy an existing template** (e.g., `style_template1.css`)
2. **Modify color variables:**
   ```css
   body {
     color: #NEW_TEXT_COLOR;
     background: #NEW_BG_COLOR;
   }
   
   .sidebar {
     background: #NEW_SIDEBAR_COLOR;
   }
   ```
3. **Update accent colors** across all interactive elements
4. **Test on multiple browsers** and screen sizes
5. **Add to dropdown** in `generate_site.py`

## CSS Custom Properties (for future enhancement)

Consider adding CSS variables for easier customization:
```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  --text-color: #333;
  --bg-color: #fff;
  --accent-color: #27ae60;
}

h1 {
  color: var(--primary-color);
}
```

---

**Note:** All themes are production-ready and thoroughly tested for readability, accessibility, and cross-browser compatibility.
