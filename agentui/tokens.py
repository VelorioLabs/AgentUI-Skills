"""Design System Tokens and Theme Exports."""
from typing import Dict, Any

THEMES: Dict[str, Dict[str, Any]] = {
    "cyberpunk": {
        "name": "Cyberpunk Dark Ops HUD",
        "bg_base": "#07090e",
        "bg_surface": "rgba(13, 19, 34, 0.85)",
        "accent_primary": "#00f0ff",
        "accent_secondary": "#ff007f",
        "accent_status": "#00ff88",
        "border": "rgba(0, 240, 255, 0.35)",
        "font_interface": "'Inter', sans-serif",
        "font_mono": "'JetBrains Mono', monospace"
    },
    "linear": {
        "name": "Linear Minimalist Dark",
        "bg_base": "#000000",
        "bg_surface": "#0a0a0a",
        "accent_primary": "#ffffff",
        "accent_secondary": "#71717a",
        "accent_status": "#10b981",
        "border": "rgba(255, 255, 255, 0.08)",
        "font_interface": "'Inter', sans-serif",
        "font_mono": "'JetBrains Mono', monospace"
    },
    "glassmorphism": {
        "name": "Glassmorphism 2.0 / Vision Pro",
        "bg_base": "#0f172a",
        "bg_surface": "rgba(255, 255, 255, 0.04)",
        "accent_primary": "#38bdf8",
        "accent_secondary": "#818cf8",
        "accent_status": "#34d399",
        "border": "rgba(255, 255, 255, 0.12)",
        "font_interface": "'Plus Jakarta Sans', sans-serif",
        "font_mono": "'JetBrains Mono', monospace"
    },
    "cosmic": {
        "name": "Deep Space Cosmic",
        "bg_base": "#06040d",
        "bg_surface": "rgba(20, 14, 38, 0.75)",
        "accent_primary": "#a855f7",
        "accent_secondary": "#6366f1",
        "accent_status": "#38bdf8",
        "border": "rgba(168, 85, 247, 0.35)",
        "font_interface": "'Inter', sans-serif",
        "font_mono": "'Fira Code', monospace"
    },
    "neobrutalism": {
        "name": "Neobrutalism Electric",
        "bg_base": "#fef08a",
        "bg_surface": "#ffffff",
        "accent_primary": "#ff5252",
        "accent_secondary": "#00e5ff",
        "accent_status": "#00e676",
        "border": "2.5px solid #000000",
        "font_interface": "'Inter', sans-serif",
        "font_mono": "'Space Mono', monospace"
    },
    "nordic": {
        "name": "Nordic Clean Light",
        "bg_base": "#fafafa",
        "bg_surface": "#ffffff",
        "accent_primary": "#18181b",
        "accent_secondary": "#71717a",
        "accent_status": "#059669",
        "border": "#e4e4e7",
        "font_interface": "'Geist', sans-serif",
        "font_mono": "'JetBrains Mono', monospace"
    }
}

def get_theme(theme_name: str) -> Dict[str, Any]:
    return THEMES.get(theme_name.lower(), THEMES["cyberpunk"])
