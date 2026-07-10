# MentorMind UI Quick Reference Guide

## 🎨 Color Classes

### Text Colors
```html
<p class="text-primary">Primary text</p>
<p class="text-success">Success text</p>
<p class="text-danger">Danger text</p>
<p class="text-warning">Warning text</p>
<p class="text-info">Info text</p>
<p class="text-muted">Muted text</p>
<p class="text-gradient">Gradient text</p>
```

### Background Colors
```html
<div class="bg-primary">Primary background</div>
<div class="bg-success">Success background</div>
<div class="bg-danger">Danger background</div>
<div class="bg-light">Light background</div>
<div class="bg-dark">Dark background</div>
```

## 🔘 Button Variants

```html
<!-- Solid Buttons -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-warning">Warning</button>

<!-- Outline Buttons -->
<button class="btn btn-outline-primary">Outline Primary</button>
<button class="btn btn-outline-success">Outline Success</button>

<!-- Sizes -->
<button class="btn btn-sm btn-primary">Small</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-lg btn-primary">Large</button>

<!-- States -->
<button class="btn btn-primary" disabled>Disabled</button>
<button class="btn btn-primary hover-lift">Lifts on hover</button>
```

## 🃏 Cards

```html
<!-- Simple Card -->
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Title</h5>
        <p class="card-text">Content</p>
    </div>
</div>

<!-- Full Featured Card -->
<div class="card shadow-lg hover-lift">
    <div class="card-header bg-primary text-white">
        <h5>Header</h5>
    </div>
    <div class="card-body">
        <p>Body content</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-sm btn-primary">Action</button>
    </div>
</div>

<!-- Image Card -->
<div class="card">
    <img src="image.jpg" class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">Title</h5>
    </div>
</div>
```

## 📊 Stat Cards

```html
<div class="stat-card">
    <h6>Total Sessions</h6>
    <h3>1,234</h3>
</div>

<div class="stat-card">
    <h6>Completion Rate</h6>
    <h3 class="text-success">92%</h3>
</div>
```

## 📝 Forms

```html
<!-- Text Input -->
<div class="mb-3">
    <label for="input" class="form-label">Label</label>
    <input type="text" class="form-control" id="input" placeholder="Placeholder">
</div>

<!-- Select -->
<div class="mb-3">
    <label for="select" class="form-label">Select</label>
    <select class="form-select" id="select">
        <option>Choose...</option>
        <option>Option 1</option>
    </select>
</div>

<!-- Textarea -->
<div class="mb-3">
    <label for="textarea" class="form-label">Message</label>
    <textarea class="form-control" id="textarea" rows="3"></textarea>
</div>

<!-- Checkbox -->
<div class="form-check">
    <input class="form-check-input" type="checkbox" id="check">
    <label class="form-check-label" for="check">
        Check this option
    </label>
</div>

<!-- Radio -->
<div class="form-check">
    <input class="form-check-input" type="radio" name="radio" id="radio">
    <label class="form-check-label" for="radio">
        Radio option
    </label>
</div>
```

## 🎯 Badges

```html
<span class="badge bg-primary">Primary</span>
<span class="badge bg-success">Success</span>
<span class="badge bg-danger">Danger</span>
<span class="badge bg-warning">Warning</span>
<span class="badge bg-info">Info</span>

<!-- Pill Badges -->
<span class="badge rounded-pill bg-primary">Pill</span>
```

## ⚠️ Alerts

```html
<div class="alert alert-success">
    <i class="fas fa-check-circle"></i> Success!
</div>

<div class="alert alert-danger">
    <i class="fas fa-exclamation-circle"></i> Error!
</div>

<div class="alert alert-warning">
    <i class="fas fa-exclamation-triangle"></i> Warning!
</div>

<div class="alert alert-info">
    <i class="fas fa-info-circle"></i> Info!
</div>

<!-- Dismissible Alert -->
<div class="alert alert-success alert-dismissible fade show">
    Message
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>
```

## 📊 Progress Bars

```html
<!-- Simple Progress -->
<div class="progress">
    <div class="progress-bar" style="width: 50%"></div>
</div>

<!-- With Label -->
<div class="progress">
    <div class="progress-bar" style="width: 25%">25%</div>
</div>

<!-- Colored -->
<div class="progress">
    <div class="progress-bar bg-success" style="width: 60%"></div>
</div>

<!-- Striped -->
<div class="progress">
    <div class="progress-bar progress-bar-striped" style="width: 75%"></div>
</div>
```

## 📋 Tables

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

<!-- Variants -->
<table class="table table-striped">...</table>
<table class="table table-bordered">...</table>
<table class="table table-borderless">...</table>
<table class="table table-hover">...</table>
<table class="table table-sm">...</table>
```

## 🎬 Animations

```html
<!-- Fade In -->
<div class="fade-in">Fades in</div>

<!-- Slide In -->
<div class="slide-in-left">Slides from left</div>
<div class="slide-in-right">Slides from right</div>

<!-- Hover Lift -->
<div class="hover-lift">Lifts on hover</div>

<!-- Custom Animation -->
<div style="animation: bounce 2s ease-in-out infinite;">Bounces</div>
```

## 🏗️ Layout

```html
<!-- Container -->
<div class="container">
    <!-- Max width: 1320px -->
</div>

<!-- Full Width -->
<div class="container-fluid">
    <!-- Full width -->
</div>

<!-- Grid -->
<div class="row">
    <div class="col-md-6">50%</div>
    <div class="col-md-6">50%</div>
</div>

<!-- Flex -->
<div class="d-flex gap-3">
    <div>Item 1</div>
    <div>Item 2</div>
</div>

<!-- Justify Content -->
<div class="d-flex justify-content-between">
    <div>Left</div>
    <div>Right</div>
</div>

<!-- Align Items -->
<div class="d-flex align-items-center">
    <div>Centered vertically</div>
</div>
```

## 📦 Spacing

```html
<!-- Margin -->
<div class="m-3">Margin all sides</div>
<div class="mt-3">Margin top</div>
<div class="mb-3">Margin bottom</div>
<div class="ms-3">Margin start (left)</div>
<div class="me-3">Margin end (right)</div>
<div class="mx-auto">Margin horizontal auto</div>

<!-- Padding -->
<div class="p-3">Padding all sides</div>
<div class="pt-3">Padding top</div>
<div class="pb-3">Padding bottom</div>
<div class="ps-3">Padding start (left)</div>
<div class="pe-3">Padding end (right)</div>

<!-- Responsive Spacing -->
<div class="p-2 p-md-4">Padding 2 mobile, 4 desktop</div>
```

## 🌓 Display & Visibility

```html
<!-- Display -->
<div class="d-none">Hidden</div>
<div class="d-block">Block display</div>
<div class="d-inline">Inline display</div>
<div class="d-flex">Flex display</div>

<!-- Responsive Display -->
<div class="d-none d-md-block">Hidden mobile, visible desktop</div>

<!-- Visibility -->
<div class="invisible">Invisible (takes space)</div>
<div class="visually-hidden">Screen reader only</div>
```

## 🎨 Text Utilities

```html
<!-- Text Alignment -->
<p class="text-start">Start aligned</p>
<p class="text-center">Center aligned</p>
<p class="text-end">End aligned</p>

<!-- Text Weight -->
<p class="fw-light">Light (300)</p>
<p class="fw-normal">Normal (400)</p>
<p class="fw-semibold">Semibold (600)</p>
<p class="fw-bold">Bold (700)</p>

<!-- Text Style -->
<p class="fst-italic">Italic</p>
<p class="text-uppercase">Uppercase</p>
<p class="text-lowercase">Lowercase</p>
<p class="text-capitalize">Capitalized</p>

<!-- Text Truncation -->
<p class="text-truncate">Long text truncated...</p>

<!-- Line Clamp -->
<p class="text-clamp-2">Max 2 lines of text</p>
```

## 📱 Responsive Classes

```html
<!-- Visibility -->
<div class="d-sm-none">Hidden on small+</div>
<div class="d-md-none">Hidden on medium+</div>
<div class="d-lg-none">Hidden on large+</div>

<!-- Columns -->
<div class="row">
    <div class="col-12 col-sm-6 col-md-4">Responsive columns</div>
</div>

<!-- Breakpoints: xs, sm, md, lg, xl, xxl -->
<div class="p-2 p-sm-3 p-md-4 p-lg-5">Responsive padding</div>
```

## 🔗 Icons (Font Awesome)

```html
<!-- Solid Icons -->
<i class="fas fa-home"></i>
<i class="fas fa-user"></i>
<i class="fas fa-envelope"></i>
<i class="fas fa-search"></i>
<i class="fas fa-bell"></i>
<i class="fas fa-cog"></i>

<!-- Sizes -->
<i class="fas fa-home fa-sm"></i>
<i class="fas fa-home fa-lg"></i>
<i class="fas fa-home fa-2x"></i>
<i class="fas fa-home fa-3x"></i>

<!-- Colors -->
<i class="fas fa-home text-primary"></i>
<i class="fas fa-home text-success"></i>

<!-- Animation -->
<i class="fas fa-spinner fa-spin"></i>
<i class="fas fa-pulse"></i>
```

## 🚀 Quick Copy-Paste Components

### Login Form
```html
<div class="card shadow-lg">
    <div class="card-header bg-primary text-white">Login</div>
    <form class="card-body">
        <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" class="form-control">
        </div>
        <div class="mb-3">
            <label class="form-label">Password</label>
            <input type="password" class="form-control">
        </div>
        <button class="btn btn-primary w-100">Sign In</button>
    </form>
</div>
```

### Dashboard Stats
```html
<div class="row">
    <div class="col-md-3">
        <div class="stat-card">
            <h6>Users</h6>
            <h3>1,234</h3>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <h6>Sessions</h6>
            <h3>567</h3>
        </div>
    </div>
</div>
```

### Data Table
```html
<div class="table-responsive">
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>john@example.com</td>
                <td><span class="badge bg-success">Active</span></td>
            </tr>
        </tbody>
    </table>
</div>
```

### Action Buttons
```html
<div class="btn-group">
    <button class="btn btn-primary"><i class="fas fa-download"></i> Export</button>
    <button class="btn btn-success"><i class="fas fa-save"></i> Save</button>
    <button class="btn btn-danger"><i class="fas fa-trash"></i> Delete</button>
</div>
```

## 💡 Tips & Tricks

1. **Always add icons** to buttons for clarity
2. **Use fade-in** class for initial load animations
3. **Add hover-lift** to interactive elements
4. **Use badges** instead of plain text for status
5. **Keep shadows** subtle (use shadow-md, not shadow-lg everywhere)
6. **Test responsiveness** with `d-md-none` classes
7. **Use text-muted** for secondary information
8. **Apply text-gradient** to headings for emphasis
9. **Wrap tables** in `table-responsive` for mobile
10. **Use gap utilities** instead of manual spacing

## 🔗 Resources

- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)
- [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

---

**Last Updated: Feb 11, 2026**
