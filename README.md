# 🎨 AgentUI-Skills — Master UI/UX Engineering Skills for AI Agents

> **Battle-tested UI/UX design skills, component recipes, and aesthetic rules for Antigravity, Claude Code, and Cursor.**  
> Built by **[VelorioLabs](https://github.com/VelorioLabs)**.

[![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)](LICENSE)
[![Agents: Antigravity | Claude | Cursor](https://img.shields.io/badge/Supported%20Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor-purple.svg)]()
[![Aesthetics: Cyberpunk & Linear Minimal](https://img.shields.io/badge/Aesthetics-Cyberpunk%20%7C%20Linear%20Minimal%20%7C%20Glassmorphic-00f0ff.svg)]()

---

## 🌟 What This Skill Does

Prevents AI coding assistants from generating boring, flat, generic, 2014-era web interfaces.  
When installed, your AI agent automatically adopts:

* 🌌 **Layered Dark-Mode Aesthetics**: Ambient radial lighting, glassmorphic card depth, and subtle glowing borders.
* 🎛️ **Dual Typography Pairings**: Sans-serif (`Inter`) for natural reading + Monospace (`JetBrains Mono`) for metrics, badges, and code.
* 📦 **Bento Grid Architecture**: Asymmetric, visually dynamic card hierarchies.
* ⚡ **Tactile Micro-Interactions**: Active click compression, glowing focus rings, smooth hover lifts, and animated status pills.

---

## 🚀 1-Click Installation

### For Google Antigravity
Clone or copy `skills/vibe-ui-designer` into your project's `.agents/skills/` or your global config `~/.gemini/config/skills/`:
```bash
python install.py --agent antigravity
```

### For Cursor
Drop the `.cursorrules` and `.cursor/rules/ui-designer.mdc` into your repository root:
```bash
python install.py --agent cursor
```

### For Claude Code
Add to your project's `CLAUDE.md` or `.claude/` instructions:
```bash
python install.py --agent claude
```

---

## 📁 Repository Structure

```text
AgentUI-Skills/
├── skills/
│   └── vibe-ui-designer/
│       ├── SKILL.md              # Official Antigravity Skill definition
│       └── references/
│           ├── color-palettes.md # Complete color tokens for Cyberpunk, Linear, Glass
│           └── component-cheatsheet.md # Tailwind & CSS component blueprints
├── cursor/
│   ├── .cursorrules              # Legacy Cursor rule file
│   └── .cursor/rules/
│       └── ui-designer.mdc       # Modern Cursor MDC rule
├── claude/
│   ├── CLAUDE.md                 # Claude Code project guidelines
│   └── .claude/
│       └── ui-designer.md        # Extended Claude system instruction
├── install.py                    # Multi-agent installer script
├── LICENSE                       # MIT License
└── README.md                     # Documentation
```

---

## 📄 License
Licensed under the **MIT License**. Copyright (c) 2026 **VelorioLabs**.
