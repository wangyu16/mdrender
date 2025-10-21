# Responsive Layout - Visual Guide

## Layout Behavior by Screen Size

### Wide Screen (Desktop > 1200px)
```
┌─────────────────────────────────────────────────────────────────┐
│                                                    🎨 Theme: [...▼]│
│                                                                   │
│  ┌─────────────┐  ┌─────────────────────────────────────┐       │
│  │             │  │                                       │       │
│  │  Contents   │  │         Content Area                 │       │
│  │  ═════════  │  │    (max-width: 1400px centered)      │       │
│  │             │  │                                       │       │
│  │  • Page 1   │  │  Lorem ipsum dolor sit amet...       │       │
│  │  • Page 2   │  │  Consectetur adipiscing elit...      │       │
│  │  • Page 3   │  │                                       │       │
│  │  • Page 4   │  │  [Content rendered here]             │       │
│  │             │  │                                       │       │
│  │             │  │                                       │       │
│  │ (Always     │  │                                       │       │
│  │  Visible)   │  │                                       │       │
│  │             │  │                                       │       │
│  └─────────────┘  └─────────────────────────────────────┘       │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

Features:
- ☰ Toggle button HIDDEN
- Sidebar always visible
- Content centered with max-width
- Professional two-panel layout
```

### Narrow Screen (Tablet/Laptop ≤ 1200px) - Sidebar Hidden
```
┌──────────────────────────────────────────────┐
│                            🎨 Theme: [...▼]  │
│                                              │
│  ☰                                           │
│                                              │
│  ┌────────────────────────────────────────┐ │
│  │                                        │ │
│  │     Full-Width Content Area            │ │
│  │                                        │ │
│  │  Lorem ipsum dolor sit amet...         │ │
│  │  Consectetur adipiscing elit...        │ │
│  │                                        │ │
│  │  [Content uses full width]             │ │
│  │                                        │ │
│  │                                        │ │
│  └────────────────────────────────────────┘ │
│                                              │
└──────────────────────────────────────────────┘

Features:
- ☰ Toggle button VISIBLE (top-left)
- Sidebar hidden (more screen space)
- Content uses full width
- Click ☰ to show sidebar
```

### Narrow Screen - Sidebar Visible (After clicking ☰)
```
┌──────────────────────────────────────────────┐
│                            🎨 Theme: [...▼]  │
│                                              │
│  ☰ ┌─────────────┐                          │
│    │             │                           │
│    │  Contents   │  ┌───────────────┐       │
│    │  ═════════  │  │ Content       │       │
│    │             │  │               │       │
│    │  • Page 1   │  │ Lorem ipsum..│       │
│    │  • Page 2   │  │               │       │
│    │  • Page 3   │  │ [Partially    │       │
│    │  • Page 4   │  │  hidden by    │       │
│    │             │  │  sidebar]     │       │
│    │ (Fixed      │  │               │       │
│    │  Overlay)   │  └───────────────┘       │
│    │             │                           │
│    └─────────────┘                           │
│                                              │
└──────────────────────────────────────────────┘

Features:
- ☰ Toggle button still visible
- Sidebar slides in from left
- Fixed overlay (z-index: 999)
- Click ☰ again to hide
- Preference saved to localStorage
```

### Mobile (≤ 768px) - Sidebar Hidden
```
┌──────────────────────┐
│   🎨        │
│  Theme:    │
│   [...▼]    │
│                      │
│  ☰                   │
│                      │
│ ┌──────────────────┐ │
│ │                  │ │
│ │  Content Area    │ │
│ │                  │ │
│ │ Lorem ipsum...   │ │
│ │                  │ │
│ │ [Full width]     │ │
│ │                  │ │
│ │                  │ │
│ └──────────────────┘ │
│                      │
└──────────────────────┘

Features:
- Compact theme selector
- Smaller toggle button
- Touch-optimized spacing
- Full-width content
```

## UI Elements

### Sidebar Toggle Button (☰)
```
┌──────────┐
│    ☰     │  ← Default state (gray/white)
└──────────┘

┌──────────┐
│    ☰     │  ← Hover state (blue background)
└──────────┘
   (blue)

Position:
- Desktop: (20px, 80px) from top-left
- Mobile:  (10px, 70px) from top-left
- Size: Compact, touch-friendly
- Z-index: 1001 (stays on top)
```

### Theme Selector
```
┌─────────────────────┐
│ 🎨 Theme: [▼]       │  ← Top-right corner
└─────────────────────┘

Dropdown options:
• Professional
• Minimalist
• Dark Mode
• Vibrant
• Academic
• Modern Gradient
• Serif Academic
• Minimal Dark
• Modern Dark
```

## Sidebar States

### 1. Visible (Default on Wide Screens)
```css
.sidebar {
  transform: translateX(0);
  /* Fully visible */
}
```

### 2. Hidden (Default on Narrow Screens)
```css
.sidebar.hidden {
  transform: translateX(-100%);
  /* Slides off screen to the left */
}
```

## User Interaction Flow

```
User opens site on narrow screen (≤1200px)
              ↓
    Sidebar hidden by default
              ↓
    Toggle button (☰) visible
              ↓
    User clicks ☰ button
              ↓
    Sidebar slides in from left
              ↓
    User browses navigation
              ↓
    User clicks ☰ again
              ↓
    Sidebar slides out to left
              ↓
    Preference saved to localStorage
              ↓
    Next visit: sidebar state restored
```

## Content Width Behavior

### Wide Screen (>1400px viewport)
```
┌────────────────────────────────────────────────────────────┐
│  Sidebar  │        Content (max 1400px)        │  Margin   │
│    280px  │          centered content          │   Auto    │
└────────────────────────────────────────────────────────────┘
           ←──────── 1400px max-width ────────→
```

### Medium Screen (1200px-1400px viewport)
```
┌──────────────────────────────────────┐
│     Content fills available space    │
│    (slightly less than 1400px)       │
└──────────────────────────────────────┘
```

### Narrow Screen (≤1200px viewport)
```
┌─────────────────────────────────┐
│  Content fills full width       │
│  (sidebar hidden or overlay)    │
└─────────────────────────────────┘
```

## Animation Sequence

### Sidebar Toggle Animation
```
Frame 1: Sidebar hidden
┌────┬─────────────┐
│ ☰  │   Content   │
│    │             │
└────┴─────────────┘

Frame 2: User clicks ☰
┌────┬─────────────┐
│ ☰ ┌┴──────────┐  │
│   │ Contents  │  │
│   │ sliding   │  │
└───┴───────────┴──┘

Frame 3: Sidebar visible
┌────┬──────────┬──┐
│ ☰  │ Contents │ │
│    │ • Page 1 │ │
│    │ • Page 2 │ │
└────┴──────────┴──┘

Transition: 0.3s ease
Property: transform: translateX()
```

## localStorage Data

```javascript
// Key-Value pairs stored
{
  "sidebar-visible": "true",    // or "false"
  "preferred-theme": "style_template1.css"  // existing feature
}

// Example usage
localStorage.getItem('sidebar-visible')  // Returns: "true" or "false"
localStorage.setItem('sidebar-visible', 'false')  // Hides sidebar
```

## Responsive Breakpoints

```
 0px                768px              1200px              ∞
  ├──────────────────┼───────────────────┼─────────────────→
  │     Mobile       │   Narrow Screen   │   Wide Screen   │
  │                  │                   │                 │
  │ • Compact UI     │ • Toggle visible  │ • No toggle     │
  │ • Small toggle   │ • Sidebar hides   │ • Sidebar fixed │
  │ • Full-width     │ • Full-width      │ • Max 1400px    │
  │   content        │   content         │   content       │
```

## CSS Class States

```html
<!-- Wide screen -->
<aside class="sidebar" id="sidebar">
  <!-- Always visible -->
</aside>

<!-- Narrow screen, sidebar hidden -->
<aside class="sidebar hidden" id="sidebar">
  <!-- transform: translateX(-100%) -->
</aside>

<!-- Narrow screen, sidebar visible -->
<aside class="sidebar" id="sidebar">
  <!-- Fixed overlay, transform: translateX(0) -->
</aside>
```

## Z-Index Layers

```
     Layer 5: (1001) Sidebar toggle button ☰
              ↑
     Layer 4: (1000) Theme selector 🎨
              ↑
     Layer 3: (999)  Sidebar (when overlay on narrow screens)
              ↑
     Layer 2: (1)    Content area
              ↑
     Layer 1: (0)    Body background
```

## Testing Checklist

### Desktop (>1200px)
- [ ] Sidebar is visible
- [ ] Toggle button is hidden
- [ ] Content is centered with max-width
- [ ] Theme selector works

### Tablet/Laptop (≤1200px)
- [ ] Toggle button appears
- [ ] Sidebar hidden by default (first visit)
- [ ] Click toggle shows sidebar
- [ ] Click toggle again hides sidebar
- [ ] Preference persists on reload

### Mobile (≤768px)
- [ ] Compact theme selector
- [ ] Smaller toggle button
- [ ] Touch-friendly targets
- [ ] Sidebar overlay works

### All Sizes
- [ ] Smooth animations
- [ ] No layout shifts
- [ ] Accessible via keyboard
- [ ] localStorage saves preferences

## Keyboard Accessibility

```
Tab → Reaches toggle button (☰)
Enter/Space → Toggles sidebar
Tab → Navigate to theme selector
Tab → Navigate to sidebar links (when visible)
```

## Summary

The responsive layout provides:
✅ Optimal content width on all screens
✅ Automatic sidebar management
✅ User control via toggle button
✅ Smooth animations
✅ Persistent preferences
✅ Professional appearance
✅ Touch-friendly on mobile
✅ Keyboard accessible
