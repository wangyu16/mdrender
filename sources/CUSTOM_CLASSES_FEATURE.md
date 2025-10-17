# Custom Classes Feature Documentation

## Overview

The markdown renderer now supports creating HTML div and span elements with custom CSS classes directly in your markdown. This allows you to apply custom styling and semantic meaning to your content without writing raw HTML.

## Features

### 1. Div Blocks with Classes
Create block-level containers with custom CSS classes.

### 2. Span Elements with Classes
Create inline elements with custom CSS classes.

## Syntax

### Div Block Syntax

```markdown
:::CLASSNAME
content here
can be multi-line
supports all markdown formatting
:::
```

**Renders to:**
```html
<div class="CLASSNAME">content here can be multi-line supports all markdown formatting</div>
```

### Span Inline Syntax

```markdown
{.CLASSNAME}content{/}
```

**Renders to:**
```html
<span class="CLASSNAME">content</span>
```

## Examples

### Alert Boxes

#### Markdown:
```markdown
:::alert
⚠️ This is an important alert message!
:::
```

#### HTML Output:
```html
<div class="alert">⚠️ This is an important alert message!</div>
```

### Colored Text

#### Markdown:
```markdown
Status: {.red}Error{/}, {.blue}Processing{/}, {.green}Success{/}
```

#### HTML Output:
```html
<p>Status: <span class="red">Error</span>, <span class="blue">Processing</span>, <span class="green">Success</span></p>
```

### Card Components

#### Markdown:
```markdown
:::card
## Welcome!
This is a **card** component.
It supports *all* markdown formatting.
:::
```

#### HTML Output:
```html
<div class="card">## Welcome! This is a <strong>card</strong> component. It supports <em>all</em> markdown formatting.</div>
```

## Use Cases

### 1. Alert/Warning Messages

```markdown
:::warning
⚠️ Warning: This action cannot be undone!
:::

:::success
✅ Success! Your changes have been saved.
:::

:::info
ℹ️ Pro tip: Use keyboard shortcuts to save time!
:::
```

### 2. Colored Inline Text

```markdown
The status is {.green}active{/} and the priority is {.red}high{/}.
```

### 3. Badges and Labels

```markdown
Version {.badge}2.0{/} is now available!

{.label-new}NEW{/} Feature added in this release.
```

### 4. Custom Containers

```markdown
:::container
This is a custom container with specific styling.
:::

:::sidebar
This could be a sidebar element.
:::

:::footer
Footer content goes here.
:::
```

### 5. Highlighting Important Text

```markdown
This is {.highlight}very important{/} information that you should read carefully.
```

### 6. Combined Usage

```markdown
:::card
## Product Features

- {.green}Fast{/} performance
- {.blue}Secure{/} by default
- {.red}Simple{/} to use

Try it today! {.badge}NEW{/}
:::
```

## Class Name Rules

Valid class names must:
- Contain only letters (a-z, A-Z), numbers (0-9), hyphens (-), and underscores (_)
- Examples: `alert`, `my-class`, `info_box`, `class123`

Invalid class names:
- Cannot contain spaces: `my class` ❌
- Cannot contain special characters: `my@class` ❌
- Cannot start with numbers: `123class` (technically valid in HTML5, but avoid)

## CSS Styling

To style your custom classes, add CSS to your HTML page:

```html
<style>
    .alert {
        background: #fff3cd;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
        color: #856404;
    }
    
    .warning {
        background: #f8d7da;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    
    .success {
        background: #d4edda;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    
    .highlight {
        background: yellow;
        padding: 2px 4px;
        font-weight: bold;
    }
    
    .red {
        color: #dc3545;
        font-weight: bold;
    }
    
    .blue {
        color: #007bff;
        font-weight: bold;
    }
    
    .green {
        color: #28a745;
        font-weight: bold;
    }
    
    .badge {
        background: #6c757d;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }
</style>
```

## Nesting

You can nest span elements inside div blocks:

```markdown
:::container
This has {.red}red text{/} and {.blue}blue text{/}.
You can mix {.highlight}highlighted{/} content too!
:::
```

## Multi-line Content

Div blocks support multi-line content with full markdown:

```markdown
:::card
# Heading

This is a paragraph with **bold** and *italic* text.

- List item 1
- List item 2

[Link](https://example.com)
:::
```

## Technical Implementation

### Location
Implemented in `/src/parser.js`:

**Span with class (inline):**
- Added to `customRules` array
- Pattern: `/\{\.([a-zA-Z0-9_-]+)\}(.+?)\{\/\}/g`
- Line ~27

**Div with class (block-level):**
- Added to `parseMarkdown` function
- Handles block detection and parsing
- Lines ~171-207
- Cleanup at end of file: Lines ~369-372

### Parsing Logic

#### Div Blocks:
1. **Opening tag detection**: Matches `:::CLASSNAME` pattern
2. **Content accumulation**: Collects all lines until closing tag
3. **Closing tag detection**: Matches `:::` pattern
4. **Inline parsing**: Processes markdown within content
5. **HTML generation**: Creates `<div class="CLASSNAME">content</div>`

#### Span Elements:
1. **Pattern matching**: Uses regex to find `{.CLASSNAME}content{/}`
2. **Extraction**: Captures class name and content
3. **Replacement**: Replaces with `<span class="CLASSNAME">content</span>`

## Browser Compatibility

✅ All modern browsers support standard HTML div and span elements:
- Chrome/Edge (all versions)
- Firefox (all versions)
- Safari (all versions)
- Mobile browsers

## Testing

### Automated Tests

Run the test suite:
```bash
npm test
```

Tests include:
- ✅ Span with class
- ✅ Div with class (single line)
- ✅ Div with class (multi-line)
- ✅ Div with inline markdown
- ✅ Nested span in div

### Visual Testing

Open the demo page:
```bash
open custom-classes-demo.html
```

### Manual Testing

```javascript
import { parseMarkdown } from './src/parser.js';

// Test span
const html1 = parseMarkdown('This is {.red}red{/} text');
console.log(html1); // Should include <span class="red">red</span>

// Test div
const html2 = parseMarkdown(':::alert\nWarning message\n:::');
console.log(html2); // Should include <div class="alert">Warning message</div>
```

## Common Patterns

### Bootstrap-style Alerts

```markdown
:::alert-primary
Primary alert
:::

:::alert-success
Success alert
:::

:::alert-danger
Danger alert
:::

:::alert-warning
Warning alert
:::
```

### Semantic HTML

```markdown
:::article
Main article content
:::

:::aside
Sidebar content
:::

:::section
Section content
:::
```

### Custom Components

```markdown
:::hero
# Welcome to Our Site
{.lead}The best solution for your needs{/}
:::

:::features
- {.icon-check}Feature 1{/}
- {.icon-check}Feature 2{/}
- {.icon-check}Feature 3{/}
:::
```

## Limitations

1. **No attributes beyond class**: Currently only supports class names, not id, style, or other attributes
2. **Single class only**: Cannot add multiple classes (e.g., `:::class1 class2:::` not supported)
3. **No self-closing**: Div blocks must have both opening `:::CLASS` and closing `:::`
4. **Class name restrictions**: Must match pattern `[a-zA-Z0-9_-]+`

## Future Enhancements

Potential improvements for future versions:

1. **Multiple classes**: `:::alert warning:::` or `{.red bold}text{/}`
2. **ID support**: `:::#myid.myclass:::`
3. **Data attributes**: `:::alert data-type="warning":::`
4. **Inline styles**: `{.red style="font-size:20px"}text{/}`
5. **Shorthand syntax**: `:::alert-warning:::` expands to `:::alert warning:::`

## Migration from Raw HTML

### Before (Raw HTML):
```html
<div class="alert">Warning message</div>
<span class="badge">NEW</span>
```

### After (Markdown):
```markdown
:::alert
Warning message
:::

{.badge}NEW{/}
```

## Best Practices

### ✅ DO:
- Use semantic class names (`alert`, `warning`, `success`)
- Define CSS styles for your classes
- Keep class names short and descriptive
- Use div blocks for multi-line content
- Use span for inline content

### ❌ DON'T:
- Don't use spaces in class names
- Don't forget the closing `:::` or `{/}`
- Don't nest div blocks (not currently supported)
- Don't mix with raw HTML `<div>` tags unnecessarily

## Examples in Context

### Blog Post with Alerts

```markdown
# How to Use Our API

:::info
This guide assumes you have an API key. If not, [sign up here](signup).
:::

## Getting Started

First, install the library:

:::code
npm install our-api
:::

:::warning
⚠️ Never commit your API key to version control!
:::

## Basic Usage

Here's a simple example with {.highlight}highlighted{/} important parts.
```

### Documentation with Color-coded Text

```markdown
# Status Codes

- {.green}200 OK{/} - Request succeeded
- {.blue}301 Moved{/} - Resource moved permanently
- {.yellow}401 Unauthorized{/} - Authentication required
- {.red}500 Error{/} - Server error
```

### Product Features

```markdown
:::card
## Premium Plan {.badge}Popular{/}

- {.green}✓{/} Unlimited storage
- {.green}✓{/} 24/7 support
- {.green}✓{/} Advanced features

{.price}$29/month{/}
:::
```

## API Usage

### Client-Side

```javascript
import { parseMarkdown } from './src/parser.js';

const markdown = `:::alert
This is an alert
:::

Text with {.red}color{/}`;

const html = parseMarkdown(markdown);
document.getElementById('content').innerHTML = html;
```

### Server-Side (Cloudflare Workers)

```javascript
// POST request
{
  "markdown": ":::warning\nImportant message\n:::\n\nWith {.highlight}highlighted{/} text"
}

// Response
{
  "html": "<div class=\"warning\">Important message</div>\n<p>With <span class=\"highlight\">highlighted</span> text</p>"
}
```

## Support

If you encounter issues:

1. Verify syntax matches the pattern exactly
2. Check that class names are valid (alphanumeric, hyphens, underscores)
3. Ensure opening and closing tags match
4. Test with `custom-classes-demo.html`
5. Run `npm test` to verify functionality

---

**Version**: 1.0.0  
**Last Updated**: October 17, 2025  
**Feature Status**: ✅ Production Ready
