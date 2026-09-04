# 🎨 AgentUI-Skills — God-Level UI/UX Engineering Skills for AI Agents

> **Battle-tested UI/UX design systems, autonomous linter, component recipes, and aesthetic rules for Google Antigravity, Claude Code, Cursor, and Windsurf.**  
> Engineered by **[VelorioLabs](https://github.com/VelorioLabs)**.

[![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)](LICENSE)
[![Version: 2.0.0](https://img.shields.io/badge/Version-2.0.0%20Elite-00ff88.svg)]()
[![Supported Agents](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Windsurf-purple.svg)]()
[![Themes](https://img.shields.io/badge/Themes-Cyberpunk%20%7C%20Linear%20%7C%20Glass%20%7C%20Cosmic%20%7C%20Neo-00f0ff.svg)]()

---

## 🌟 The Problem This Solves

By default, AI coding assistants (Claude, Cursor, Copilot, Antigravity) generate generic, flat, boring 2014-era web interfaces:
- ❌ Flat dull gray backgrounds (`#111` / `#222`) without lighting or depth
- ❌ Single generic sans-serif fonts with zero visual hierarchy
- ❌ Static, rigid vertical boxes instead of dynamic Bento Grids
- ❌ Dead buttons without hover lifts or active click compressions
- ❌ Uninspired UI components that scream *"an AI wrote this"*

**`AgentUI-Skills`** is a complete design brain upgrade for AI coding assistants. It enforces modern aesthetics, layered depth, typography pairing, and micro-interactions on every line of frontend code.

---

## ⚡ Key Superpowers

* 🎨 **6 Master Design Systems**:
  - 🌌 **Cyberpunk / Dark Ops HUD** (OSINT, crypto, devtools, audio DAWs)
  - ⚡ **Linear / Vercel Minimalist Dark** (SaaS, cloud portals, issue trackers)
  - 💎 **Glassmorphism 2.0 / Vision Pro** (Creative portfolios, consumer web apps)
  - 🪐 **Deep Space Cosmic** (AI platforms, spatial computing)
  - 🏛️ **Neobrutalism Electric** (Viral apps, bold consumer fintech)
  - 🌿 **Nordic Clean Light** (Documentation, editorial, wellness)
* 🎛️ **Dual Typography Architecture**: Interface body (`Inter` / `Plus Jakarta Sans`) paired with Monospace (`JetBrains Mono` / `Fira Code`) for metrics, tags, badges, and code.
* 📦 **Bento Grid Layouts**: Asymmetric, visually dynamic card hierarchies with glowing spotlight illumination.
* 🔍 **Autonomous UI Linter CLI**: Static analysis engine that scans your web code, detects lazy AI anti-patterns, and scores design quality from Grade F to Grade S (God Level).
* 🌐 **Interactive In-Browser Showcase**: Visual playground with live theme switching, Command Palette (`Cmd+K`), and 1-click recipe copying.

---

## 🚀 1-Click Installation into Any Project

```bash
git clone https://github.com/VelorioLabs/AgentUI-Skills.git
cd AgentUI-Skills

# Install for all supported agents:
python install.py --agent all --target /path/to/your/project

# Or install specifically for your favorite agent:
python install.py --agent antigravity --target /path/to/your/project
python install.py --agent cursor --target /path/to/your/project
python install.py --agent claude --target /path/to/your/project
```

---

## 🛠️ CLI Usage & Design Linter

```bash
# Audit any frontend file or project directory:
python -m agentui.cli audit ./src

# List all available design themes and component templates:
python -m agentui.cli list

# Export ready-to-copy code for a component:
python -m agentui.cli add bento-card
python -m agentui.cli add command-palette
python -m agentui.cli add navbar
python -m agentui.cli add status-pill

# Output design tokens for a theme:
python -m agentui.cli theme cyberpunk
```

---

## 📁 Repository Structure

```text
AgentUI-Skills/
├── skills/
│   └── vibe-ui-designer/
│       ├── SKILL.md                          # Antigravity Master Skill definition
│       └── references/
│           ├── theme-tokens.md               # Exact CSS & Tailwind variables for all 6 themes
│           ├── component-recipes.md          # 12 production-grade component recipes
│           ├── animation-keyframes.md        # CSS keyframes (radar sweeps, border glows)
│           └── design-audit-checklist.md     # 25-point design audit rubric
├── cursor/
│   ├── .cursorrules                          # Legacy Cursor rule file
│   └── .cursor/rules/
│       ├── ui-designer.mdc                   # Modern Cursor MDC design rule
│       ├── tailwind-patterns.mdc             # Tailwind CSS component recipes
│       └── accessibility-wcag.mdc            # WCAG AA/AAA accessibility checks
├── claude/
│   ├── CLAUDE.md                             # Claude Code system guidelines
│   └── .claude/
│       ├── ui-designer.md                    # Extended Claude UI instructions
│       └── component-guidelines.md           # Component architecture specs
├── windsurf/
│   └── .windsurfrules                        # Windsurf IDE design rule
├── .github/
│   └── copilot-instructions.md               # GitHub Copilot UI/UX instructions
├── agentui/                                  # Python CLI & Linter Package
│   ├── cli.py                                # CLI entry point
│   ├── linter.py                             # 25-point UI static analysis engine
│   ├── templates.py                          # Ready-to-inject component templates
│   └── tokens.py                             # Master design tokens & theme exports
├── showcase/                                 # Interactive Component Playground
│   ├── index.html                            # Interactive web preview
│   ├── style.css                             # Dynamic theme styles
│   └── app.js                                # Theme switcher & command palette
├── tests/                                    # Automated Test Suite (100% Pass)
│   ├── test_cli.py
│   ├── test_linter.py
│   ├── test_templates.py
│   └── test_tokens.py
├── install.py                                # Universal cross-agent installer
├── pyproject.toml                            # Python package manifest
├── LICENSE                                   # MIT License
└── README.md                                 # Documentation
```

---

## 🧪 Automated Testing

```bash
python -m unittest discover -s tests
# 7 tests passed (100% success rate)
```

---

## 📄 License

Licensed under the **MIT License**. Copyright (c) 2026 **[VelorioLabs](https://github.com/VelorioLabs)**.
