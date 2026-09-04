---
name: vibe-ui-designer
description: >-
  World-class UI/UX design and frontend styling skill for AI agents (Antigravity, Claude, Cursor).
  Use whenever the user asks to design, build, or polish a user interface, webpage, web app,
  dashboard, or visual component. Enforces modern aesthetics (Linear/Vercel minimalist dark mode,
  Cyberpunk HUD, Glassmorphism 2.0, Bento Grids), prevents generic AI-looking designs, and provides
  battle-tested CSS/Tailwind component recipes, typography hierarchies, and micro-interactions.
---

# 🎨 VibeUI Designer — Master UI/UX Engineering Skill

> **Target Agents**: Antigravity, Claude Code, Cursor, Windsurf.  
> **Mission**: Eliminate boring, generic "AI-generated" web interfaces (flat gray boxes, harsh blue buttons, lack of hierarchy) and construct **world-class, visually magnetic, production-grade UIs**.

---

## ⚡ The 5 Commandments of Elite UI Design

### 1. Kill Flat Grays — Use Layered Depth & Radial Glows
* ❌ **Never** use plain `#111111` or `#000000` with flat borders.
* ✅ **Always** layer dark palettes:
  - Deep Base: `#07090e` or `#090d16` (slate/navy-tinted dark)
  - Subtle Radial Glows: `radial-gradient(circle at 10% 20%, rgba(0, 240, 255, 0.04) 0%, transparent 40%)`
  - Cards: `rgba(13, 20, 36, 0.75)` with `backdrop-filter: blur(16px)`
  - Glowing Borders: `border: 1px solid rgba(255, 255, 255, 0.08)` with hover state `border-color: rgba(0, 240, 255, 0.3)`

### 2. Typography Hierarchy & Dual Font Pairings
* Always combine two distinct typefaces:
  - **Display / Code / Monospace**: `'JetBrains Mono'`, `'Fira Code'`, or `'Space Mono'` for badges, timestamps, metrics, code, and system status tags.
  - **Body / Interface**: `'Inter'`, `'Plus Jakarta Sans'`, or `'Geist'` for headers, body copy, and navigation.
* Never use single uniform font weights. Vary:
  - Titles: `font-extrabold` (800) with subtle gradient text fill (`bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-blue-500`).
  - Section Labels: `text-xs font-mono uppercase tracking-widest text-slate-400`.
  - Body: `text-sm text-slate-300 font-normal leading-relaxed`.

### 3. Bento Grid & Asymmetric Card Layouts
* Replace vertical stacks of boring uniform boxes with responsive **Bento Grids**:
  - Hero Card (2 columns, 2 rows) containing dynamic visualizers or live metrics.
  - Supporting Cards with varying aspect ratios.
  - Integrated hover micro-transitions: `transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_0_25px_rgba(0,240,255,0.15)]`.

### 4. Interactive Micro-Affordances & Sensory Details
* **Pulsing Status Dots**: An active green/cyan dot with an animated pinging ring (`animate-ping`).
* **Tactile Buttons**: Subtle gradient background, inner border glow, and active click compression (`active:scale-95`).
* **Glass Inset Inputs**: Slightly darker inset background (`rgba(0, 0, 0, 0.3)`), crisp glowing outline on focus (`focus:ring-2 focus:ring-cyan-400/40`).

### 5. Never Leave Empty or Static States
* Add dynamic preview skeletons, smooth CSS keyframe shimmers, animated SVG waveforms, or canvas particle meshes.
* Provide copy-to-clipboard badges with instant visual feedback ("COPIED!").

---

## 🎨 Visual Themes & Palette Blueprints

### Theme A: 🌌 Cyberpunk / Dark Ops HUD (High Energy / Tech)
```css
:root {
  --bg-primary: #07090e;
  --bg-card: rgba(13, 19, 34, 0.85);
  --border-glow: rgba(0, 240, 255, 0.25);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --accent-cyan: #00f0ff;
  --accent-pink: #ff007f;
  --accent-green: #00ff88;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
}
```
* **Best For**: OSINT tools, audio/video studios, terminal dashboards, security apps, crypto/Web3.

### Theme B: ⚡ Linear / Vercel Minimalist Elegance (SaaS / DevTools)
```css
:root {
  --bg-primary: #000000;
  --bg-card: #0a0a0a;
  --border: rgba(255, 255, 255, 0.1);
  --border-hover: rgba(255, 255, 255, 0.25);
  --accent: #ffffff;
  --accent-muted: #a1a1aa;
  --badge-bg: rgba(255, 255, 255, 0.05);
}
```
* **Best For**: Developer productivity, task management, API docks, code explorers, analytics.

### Theme C: 💎 Glassmorphism 2.0 (Consumer / Modern Web)
```css
:root {
  --bg-base: #0f172a;
  --glass-surface: rgba(255, 255, 255, 0.03);
  --glass-border: rgba(255, 255, 255, 0.12);
  --glass-blur: blur(20px);
  --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
```
* **Best For**: Consumer utilities, converters, mail clients, file drops, creative portfolios.

---

## 🧩 Battle-Tested Component Recipes

### 1. Master Glassmorphic Card (Tailwind)
```html
<div class="relative overflow-hidden rounded-2xl border border-white/10 bg-slate-900/60 p-6 backdrop-blur-xl transition-all duration-300 hover:border-cyan-500/30 hover:shadow-2xl hover:shadow-cyan-500/10">
  <div class="absolute -right-12 -top-12 h-32 w-32 rounded-full bg-cyan-500/10 blur-2xl"></div>
  <div class="relative z-10">
    <!-- Content goes here -->
  </div>
</div>
```

### 2. Futuristic Pulse Status Pill
```html
<div class="inline-flex items-center gap-2 rounded-full border border-emerald-500/30 bg-emerald-500/10 px-3 py-1 font-mono text-xs font-semibold text-emerald-400">
  <span class="relative flex h-2 w-2">
    <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
    <span class="relative inline-flex h-2 w-2 rounded-full bg-emerald-500"></span>
  </span>
  <span>SYSTEM ACTIVE</span>
</div>
```

### 3. Glowing Action Button
```html
<button class="relative group overflow-hidden rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 px-6 py-3 font-mono text-sm font-bold text-slate-950 transition-all duration-300 hover:scale-[1.02] hover:shadow-[0_0_25px_rgba(0,240,255,0.4)] active:scale-95">
  <span class="relative z-10 flex items-center gap-2">
    <span>INITIALIZE ENGINE</span>
    <span>⚡</span>
  </span>
</button>
```

---

## 📋 Pre-Flight UI Checklist for Agents

Before completing any frontend or UI code task, verify:
- [ ] **Dual Font Loaded**: Google Fonts included (e.g. `Inter` + `JetBrains Mono`).
- [ ] **No Generic White Background**: Dark canvas with subtle gradient accents or radial glows.
- [ ] **Tactile Hover States**: Every button, card, and tab has a visible `:hover` and `:active` transition.
- [ ] **Responsive Padding**: Clean spacing scale (`p-4 sm:p-6 lg:p-8`), no horizontal scroll overflow.
- [ ] **Visual Contrast**: Text is legible (WCAG compliant) with high contrast against the dark card.
- [ ] **Sensory Feedback**: Icons (Lucide / Heroicons / Emojis) used thoughtfully beside labels.
