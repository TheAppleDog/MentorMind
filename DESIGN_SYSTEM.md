# MentorMind Design System & Style Guide

## 📐 Design Principles

1. **Modern Glassmorphism**: Semi-transparent elements with backdrop blur
2. **Smooth Animations**: All interactions have 0.2-0.5s transitions
3. **Gradient Aesthetics**: Vibrant color gradients for visual interest
4. **Depth & Shadows**: Layered shadows for visual hierarchy
5. **Responsive First**: Mobile-optimized layouts
6. **Accessibility**: High contrast ratios and clear typography

## 🎨 Color System

### Primary Palette
- **Primary Indigo**: `#6366f1` (RGB: 99, 102, 241)
- **Secondary Purple**: `#8b5cf6` (RGB: 139, 92, 246)
- **Primary Gradient**: `linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)`

### Semantic Colors
- **Success Green**: `#10b981` (RGB: 16, 185, 129)
- **Success Gradient**: `linear-gradient(135deg, #10b981 0%, #34d399 100%)`
- **Danger Red**: `#ef4444` (RGB: 239, 68, 68)
- **Danger Gradient**: `linear-gradient(135deg, #ef4444 0%, #f87171 100%)`
- **Warning Amber**: `#f59e0b` (RGB: 245, 158, 11)
- **Warm Gradient**: `linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%)`
- **Info Cyan**: `#06b6d4` (RGB: 6, 182, 212)

### Neutral Colors
- **Dark**: `#1f2937` (RGB: 31, 41, 55)
- **Gray**: `#6b7280` (RGB: 107, 114, 128)
- **Light**: `#f3f4f6` (RGB: 243, 244, 246)
- **White**: `#ffffff`

### Color Usage
```html
<!-- Primary Action -->
<button class="btn btn-primary">Primary Action</button>

<!-- Success/Positive -->
<button class="btn btn-success">Success Action</button>

<!-- Danger/Destructive -->
<button class="btn btn-danger">Delete</button>

<!-- Warning/Caution -->
<button class="btn btn-warning">Warning</button>

<!-- Info/Neutral -->
<button class="btn btn-info">Information</button>
```

## 📝 Typography

### Font Stack
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
```

### Font Sizes
- **h1**: 2.5rem (40px) - Page titles
- **h2**: 2rem (32px) - Section titles
- **h3**: 1.5rem (24px) - Subsections
- **h4**: 1.25rem (20px) - Card titles
- **h5**: 1.125rem (18px) - Labels
- **h6**: 1rem (16px) - Small titles
- **body**: 1rem (16px) - Regular text
- **small**: 0.875rem (14px) - Secondary text

### Font Weights
- **Regular**: 400 (body text, paragraphs)
- **Medium**: 500 (labels, buttons)
- **Semibold**: 600 (headings, card titles)
- **Bold**: 700 (emphasis, highlights)

### Line Heights
- **Headings**: 1.2
- **Body**: 1.5
- **Dense**: 1.3

## 🎯 Component Styling

### Cards

```html
<div class="card shadow-lg hover-lift">
    <div class="card-header bg-primary text-white">
        <h5>Card Title</h5>
    </div>
    <div class="card-body">
        <p>Card content goes here</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-sm btn-primary">Action</button>
    </div>
</div>
```

**Card Features:**
- Border radius: 12px
- Box shadow: `0 4px 6px -1px rgba(0, 0, 0, 0.1)`
- Hover effect: Lift 8px with enhanced shadow
- Background: `rgba(255, 255, 255, 0.9)` with backdrop blur
- Border: 1px solid `rgba(255, 255, 255, 0.5)`

### Buttons

#### Primary Button
```html
<button class="btn btn-primary">Primary Action</button>
```
- Background: Primary gradient
- Color: White
- Padding: 0.6rem 1.2rem
- Border radius: 8px
- Box shadow: `0 4px 15px rgba(99, 102, 241, 0.3)`

#### Secondary Button
```html
<button class="btn btn-outline-primary">Secondary Action</button>
```
- Border: 2px solid primary
- Background: Transparent
- Color: Primary
- On hover: Gradient background

#### Sizes
```html
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-lg">Large</button>
```

### Forms

```html
<form>
    <div class="mb-3">
        <label for="input" class="form-label">Label</label>
        <input type="text" class="form-control" id="input" placeholder="Placeholder">
    </div>
    <div class="mb-3">
        <label for="select" class="form-label">Select</label>
        <select class="form-select" id="select">
            <option>Option 1</option>
            <option>Option 2</option>
        </select>
    </div>
    <div class="mb-3">
        <textarea class="form-control" rows="3"></textarea>
    </div>
</form>
```

**Form Features:**
- Border: 2px solid `rgba(99, 102, 241, 0.2)`
- Border radius: 8px
- Focus effect: Border color primary, scale 1.02, glow effect
- Background: `rgba(255, 255, 255, 0.8)`

### Tables

```html
<div class="table-responsive">
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data 1</td>
                <td>Data 2</td>
            </tr>
        </tbody>
    </table>
</div>
```

**Table Features:**
- Header: Primary gradient background
- Hover rows: Scale 1.01 with background tint
- Borders: Subtle with 1px solid rgba
- Animations: Smooth transitions on row hover

### Badges

```html
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-danger">Danger</span>
```

**Badge Features:**
- Border radius: 20px (pill shape)
- Padding: 0.5rem 0.75rem
- Font weight: 600
- On hover: Scale 1.1

### Progress Bars

```html
<div class="progress">
    <div class="progress-bar" role="progressbar" 
         style="width: 75%;" aria-valuenow="75"></div>
</div>
```

**Progress Features:**
- Height: 8px
- Border radius: 10px
- Background: Primary gradient
- Glow effect: `0 0 20px rgba(99, 102, 241, 0.3)`

### Alerts

```html
<div class="alert alert-success">
    <i class="fas fa-check-circle"></i> Success message
</div>
<div class="alert alert-danger">
    <i class="fas fa-exclamation-circle"></i> Error message
</div>
<div class="alert alert-warning">
    <i class="fas fa-exclamation-triangle"></i> Warning message
</div>
<div class="alert alert-info">
    <i class="fas fa-info-circle"></i> Info message
</div>
```

**Alert Features:**
- Border left: 4px solid color
- Border radius: 10px
- Background: Semi-transparent color (0.1 opacity)
- Animation: slideInDown 0.4s ease-out

## ✨ Animation Library

### Fade In
```html
<div class="fade-in">Content fades in</div>
```
- Duration: 0.6s
- Timing: ease-out

### Slide In (Left/Right)
```html
<div class="slide-in-left">Slides from left</div>
<div class="slide-in-right">Slides from right</div>
```
- Duration: 0.6s
- Distance: 30px

### Bounce
```html
<i class="fas fa-star" style="animation: bounce 2s ease-in-out infinite;"></i>
```
- Duration: 2s
- Distance: 10px

### Pulse
```html
<div style="animation: pulse 2s ease-in-out infinite;">Pulsing element</div>
```
- Duration: 2s
- Opacity: 1 → 0.7 → 1

### Spin
```html
<i class="spinner-border"></i>
```
- Duration: 1s linear infinite

## 🎊 Confetti Effects

### Trigger on Success
```javascript
confetti.createConfetti(x, y, 30);
confetti.animate();
```

### Using Canvas Confetti Library
```javascript
confetti({
    particleCount: 100,
    spread: 70,
    origin: { y: 0.6 }
});
```

## 🔧 Spacing System

### Padding
- **xs**: 0.25rem
- **sm**: 0.5rem
- **md**: 1rem
- **lg**: 1.5rem
- **xl**: 2rem
- **xxl**: 3rem

### Margins
```html
<div class="mb-3">Margin bottom: 1rem</div>
<div class="mt-4">Margin top: 1.5rem</div>
<div class="mx-auto">Margin x auto</div>
<div class="p-4">Padding: 1.5rem</div>
```

## 🎯 Responsive Breakpoints

- **Extra small** (xs): < 576px - Phones
- **Small** (sm): ≥ 576px - Large phones
- **Medium** (md): ≥ 768px - Tablets
- **Large** (lg): ≥ 992px - Desktops
- **Extra large** (xl): ≥ 1200px - Large desktops

## 📊 Data Visualization Components

### Stat Card
```html
<div class="stat-card">
    <h6>Total Users</h6>
    <h3 class="text-primary">1,234</h3>
</div>
```

### Chart
```html
<canvas id="myChart"></canvas>
```

## 🌐 Layout Patterns

### Container
```html
<div class="container">
    <!-- Max width: 1320px -->
</div>
```

### Grid System (12 columns)
```html
<div class="row">
    <div class="col-md-6">50% width on medium+</div>
    <div class="col-md-6">50% width on medium+</div>
</div>
```

### Flexbox Utilities
```html
<div class="d-flex gap-3 align-items-center justify-content-between">
    <!-- Flex with gap, centered items, space between -->
</div>
```

## 🎨 Custom CSS Classes

### Utility Classes
```css
.text-gradient         /* Gradient text effect */
.shadow-glow          /* Colored shadow glow */
.hover-lift           /* Lift on hover animation */
.fade-in              /* Fade in animation */
.slide-in-left        /* Slide from left */
.slide-in-right       /* Slide from right */
.glassmorphic         /* Glass effect styling */
.blur-background      /* Backdrop blur effect */
```

## 📋 Best Practices

1. **Always use semantic HTML** - Use proper heading levels, form elements
2. **Include icons** - Use Font Awesome for visual context
3. **Add animations** - Every interaction should have smooth transitions
4. **Maintain contrast** - Ensure text is readable on backgrounds
5. **Test responsively** - Check all breakpoints
6. **Use gradients thoughtfully** - Not every element needs a gradient
7. **Keep animations subtle** - 0.3s is usually sufficient
8. **Provide feedback** - Show users what's happening with loading states
9. **Consistent spacing** - Use the spacing system consistently
10. **Accessible colors** - Ensure colorblind-friendly palette

## 🚀 Implementation Checklist

- [ ] Use appropriate heading levels
- [ ] Add icons to buttons and labels
- [ ] Apply hover states to interactive elements
- [ ] Include loading states for async actions
- [ ] Use gradients for primary actions
- [ ] Add shadow effects for depth
- [ ] Implement smooth transitions (0.3s)
- [ ] Test on mobile devices
- [ ] Verify color contrast ratios
- [ ] Add form validation feedback
- [ ] Include success/error messages
- [ ] Test keyboard navigation
- [ ] Add alt text to images
- [ ] Optimize animations for performance
- [ ] Use semantic color meanings

## 🎓 Example: Enhanced Login Form

```html
<div class="card shadow-lg hover-lift">
    <div class="card-header bg-gradient-primary text-white">
        <h2>Welcome Back</h2>
        <p class="text-white-50">Sign in to your account</p>
    </div>
    <form class="card-body">
        <div class="mb-3 fade-in">
            <label class="form-label">
                <i class="fas fa-envelope me-2 text-primary"></i>Email
            </label>
            <input type="email" class="form-control" placeholder="you@example.com">
        </div>
        <div class="mb-3 slide-in-right">
            <label class="form-label">
                <i class="fas fa-lock me-2 text-primary"></i>Password
            </label>
            <input type="password" class="form-control" placeholder="••••••••">
        </div>
        <button class="btn btn-primary btn-lg w-100">Sign In</button>
    </form>
</div>
```

---

**Version 1.0** | Created: Feb 11, 2026 | Last Updated: Feb 11, 2026
