# Responsive Layout Feature

## Overview

The mdrender site now includes responsive layout features that improve usability on different screen sizes, particularly on narrow screens and tablets.

## New Features

### 1. Maximum Content Width

The content panel now has a maximum width of **1400px**, which:
- Prevents content from becoming too wide on large screens
- Improves readability by maintaining optimal line length
- Centers the content automatically within the available space

**Benefits:**
- Better readability (optimal line length for comfortable reading)
- Professional appearance on ultra-wide monitors
- Consistent user experience across different screen sizes

### 2. Automatic Sidebar Collapsing

On screens **≤1200px wide**, the sidebar automatically:
- Becomes collapsible
- Hides by default on first visit (saved to localStorage)
- Shows a toggle button (☰) in the top-left corner
- Remembers user preference across page loads

**Screen Width Breakpoints:**
- **> 1200px**: Sidebar always visible, toggle button hidden
- **≤ 1200px**: Sidebar collapsible, toggle button visible
- **≤ 768px**: Mobile-optimized UI with smaller toggle button

### 3. Sidebar Toggle Button

A floating toggle button appears on narrow screens that:
- **Location**: Top-left corner (below theme selector)
- **Icon**: Hamburger menu (☰)
- **Function**: Shows/hides the navigation sidebar
- **State Persistence**: Remembers user preference via localStorage
- **Visual Feedback**: Hover effects and smooth animations

**Button Features:**
- Semi-transparent background with blur effect
- Smooth hover transitions (changes to blue)
- Positioned at (20px, 80px) on desktop, (10px, 70px) on mobile
- Z-index of 1001 to stay above other elements

## User Experience

### Wide Screens (Desktop)
- Sidebar is always visible
- Content is centered with max-width of 1400px
- Toggle button is hidden
- Traditional two-panel layout

### Narrow Screens (Tablet/Small Laptop)
- Sidebar is hidden by default
- Toggle button appears in top-left
- Click toggle to show/hide sidebar
- Preference saved to localStorage
- Full-width content area when sidebar is hidden

### Mobile Screens (≤768px)
- Compact theme selector
- Smaller toggle button
- Reduced padding for content
- Optimized for touch interactions

## Technical Implementation

### CSS Media Queries

```css
/* Narrow screens - sidebar toggle enabled */
@media (max-width: 1200px) {
  .sidebar-toggle {
    display: block;
  }
  
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    z-index: 999;
  }
  
  .sidebar.hidden {
    transform: translateX(-100%);
  }
}

/* Mobile optimizations */
@media (max-width: 768px) {
  .sidebar-toggle {
    top: 70px;
    left: 10px;
    padding: 8px 12px;
    font-size: 18px;
  }
}
```

### JavaScript Functionality

#### Auto-detect Screen Width
```javascript
function checkScreenWidth() {
  if (window.innerWidth <= 1200) {
    const savedState = localStorage.getItem('sidebar-visible');
    if (savedState === null) {
      // First time on narrow screen, hide by default
      sidebar.classList.add('hidden');
      sidebarVisible = false;
    } else {
      // Restore saved preference
      sidebarVisible = savedState === 'true';
      if (!sidebarVisible) {
        sidebar.classList.add('hidden');
      }
    }
  } else {
    // Wide screen, always show sidebar
    sidebar.classList.remove('hidden');
    sidebarVisible = true;
  }
}
```

#### Toggle Button Handler
```javascript
sidebarToggle.addEventListener('click', () => {
  sidebarVisible = !sidebarVisible;
  sidebar.classList.toggle('hidden');
  
  // Save state to localStorage
  localStorage.setItem('sidebar-visible', sidebarVisible);
});
```

#### Resize Handler (Debounced)
```javascript
let resizeTimeout;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimeout);
  resizeTimeout = setTimeout(checkScreenWidth, 150);
});
```

## localStorage Keys

The feature uses localStorage to persist user preferences:

| Key | Value | Purpose |
|-----|-------|---------|
| `sidebar-visible` | `'true'` or `'false'` | Remembers if user wants sidebar visible on narrow screens |
| `preferred-theme` | Theme filename | Remembers selected theme (existing feature) |

## Accessibility

### Features
- **ARIA Label**: Toggle button includes `aria-label="Toggle sidebar"`
- **Keyboard Accessible**: Button can be activated via keyboard
- **Semantic HTML**: Proper use of `<aside>`, `<nav>`, and `<main>` elements
- **Visual Feedback**: Clear hover and active states
- **No Motion Sickness**: Smooth, professional transitions (0.3s ease)

### Screen Readers
- Sidebar marked with semantic `<aside>` tag
- Navigation clearly marked with `<nav>` element
- Button has descriptive aria-label

## Browser Compatibility

### Supported Features
- CSS Flexbox (all modern browsers)
- CSS Transforms (all modern browsers)
- localStorage API (all modern browsers)
- CSS Media Queries (all modern browsers)
- backdrop-filter (modern browsers, graceful degradation)

### Tested On
- ✅ Chrome/Edge (Chromium)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Considerations

### Optimizations
1. **Debounced Resize Handler**: Prevents excessive recalculations during window resize
2. **CSS Transitions**: Hardware-accelerated transforms for smooth animations
3. **localStorage**: Minimal data storage, instant retrieval
4. **No JavaScript During Scroll**: Toggle functionality doesn't affect scroll performance

### CSS Performance
- Uses `transform: translateX()` for smooth GPU-accelerated animations
- Transitions limited to 0.3s for responsiveness
- No layout recalculations during toggle

## Usage Examples

### Example 1: Desktop User
1. Opens site on 1920px monitor
2. Sees sidebar on left, content centered with max-width
3. No toggle button visible
4. Professional, spacious layout

### Example 2: Tablet User (Landscape)
1. Opens site on 1024px tablet
2. Sidebar is hidden by default
3. Sees toggle button (☰) in top-left
4. Clicks toggle to open sidebar
5. Browses navigation
6. Clicks toggle again to close
7. Preference saved for next visit

### Example 3: Mobile User
1. Opens site on 375px phone
2. Compact theme selector in top-right
3. Toggle button visible in top-left
4. Sidebar hidden to maximize content space
5. Can toggle sidebar when needed
6. Full-width content for comfortable reading

## Integration with Existing Features

### Theme Switcher
- Toggle button positioned below theme selector
- Both use similar styling (semi-transparent, blur effect)
- Consistent z-index management
- No visual conflicts

### Custom Classes
- All custom classes (`.callout`, `.tip`, etc.) work with new layout
- Responsive padding adjustments
- No horizontal overflow issues

### Code Blocks
- Prism.js syntax highlighting remains functional
- Code blocks respect max-width constraint
- Horizontal scrolling only when necessary

## Future Enhancements

Potential improvements for future versions:

1. **Swipe Gestures**: Add touch swipe to open/close sidebar on mobile
2. **Keyboard Shortcuts**: Add hotkey (e.g., `Ctrl+B`) to toggle sidebar
3. **Adjustable Width**: Allow users to drag sidebar edge to resize
4. **Mini Sidebar**: Collapsed sidebar showing only icons
5. **Smooth Content Shift**: Animate content when sidebar opens/closes
6. **Sidebar Position**: Option to move sidebar to right side
7. **Multiple Breakpoints**: More granular responsive behavior
8. **Print Optimization**: Hide sidebar and controls when printing

## Troubleshooting

### Issue: Sidebar doesn't appear on narrow screens
**Solution**: Click the toggle button (☰) in the top-left corner

### Issue: Sidebar preference not saved
**Solution**: Check if localStorage is enabled in browser settings

### Issue: Toggle button overlaps with content
**Solution**: Toggle button has high z-index (1001) and should stay on top. If issue persists, check for conflicting custom CSS.

### Issue: Content too wide on large screens
**Solution**: Content now has max-width: 1400px. If still too wide, check if custom CSS is overriding this.

## Code Locations

### Files Modified
- `/workspaces/mdrender/scripts/generate_site.py`

### Key Sections
1. **CSS Styles** (lines ~170-270): Media queries and responsive styles
2. **HTML Structure** (lines ~280-310): Toggle button and sidebar markup
3. **JavaScript** (lines ~315-370): Toggle logic and screen width detection

## Summary

The responsive layout feature enhances the mdrender site by:

✅ Adding maximum content width (1400px) for better readability
✅ Auto-collapsing sidebar on narrow screens (≤1200px)
✅ Providing toggle button for sidebar control
✅ Saving user preferences via localStorage
✅ Maintaining compatibility with all existing features
✅ Following accessibility best practices
✅ Delivering smooth, professional animations

The feature is fully backward-compatible and enhances the user experience across all device sizes without breaking existing functionality.
