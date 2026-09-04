"""Automated UI/UX Static Analysis Linter for AI Agents."""
import os
import re
from typing import List, Dict, Any

class UILinter:
    """Audits HTML/TSX/JSX/CSS code against God-Level VibeUI design rules."""

    @staticmethod
    def audit_code(content: str, filename: str = "snippet") -> Dict[str, Any]:
        issues: List[Dict[str, str]] = []
        score = 100

        # 1. Flat gray backgrounds check
        flat_gray_matches = re.findall(r'(?:bg-gray-900|bg-\[#111111\]|bg-\[#222222\]|bg-\[#1a1a1a\]|#111111|#222222|#1a1a1a)', content, re.IGNORECASE)
        if flat_gray_matches:
            issues.append({
                "rule": "RULE-01: NO_FLAT_GRAYS",
                "severity": "HIGH",
                "message": f"Found {len(flat_gray_matches)} instances of flat gray backgrounds. Replace with layered dark slate/navy (#07090e or bg-slate-950/bg-zinc-950) with subtle radial gradients."
            })
            score -= 20

        # 2. Dual typography check (needs monospace font for stats/badges)
        has_mono = bool(re.search(r'(?:font-mono|JetBrains|Fira|Space Mono)', content, re.IGNORECASE))
        has_sans = bool(re.search(r'(?:font-sans|Inter|Plus Jakarta|Geist)', content, re.IGNORECASE))
        if not has_mono:
            issues.append({
                "rule": "RULE-02: MISSING_MONOSPACE_PAIRING",
                "severity": "MEDIUM",
                "message": "Missing monospace font pairing. Numerical stats, timestamps, badges, and system codes should use font-mono ('JetBrains Mono')."
            })
            score -= 15

        # 3. Missing hover micro-affordances on clickable elements
        buttons = re.findall(r'<button[^>]*>', content)
        buttons_without_hover = [b for b in buttons if "hover:" not in b]
        if buttons_without_hover:
            issues.append({
                "rule": "RULE-03: MISSING_HOVER_AFFORDANCE",
                "severity": "MEDIUM",
                "message": f"{len(buttons_without_hover)} button(s) lack hover transition classes (e.g. hover:scale-[1.02] or hover:shadow-cyan-500/20)."
            })
            score -= 15

        # 4. Translucent cards without backdrop-blur
        has_opacity = bool(re.search(r'(?:bg-slate-900/\d+|bg-white/\d+|rgba\([^)]+\))', content))
        has_blur = bool(re.search(r'backdrop-blur', content))
        if has_opacity and not has_blur:
            issues.append({
                "rule": "RULE-04: MISSING_BACKDROP_BLUR",
                "severity": "MEDIUM",
                "message": "Semi-transparent card backgrounds detected without backdrop-blur. Add backdrop-blur-xl for frosted glass depth."
            })
            score -= 15

        # 5. Missing active click compression
        buttons_without_active = [b for b in buttons if "active:" not in b]
        if buttons_without_active:
            issues.append({
                "rule": "RULE-05: MISSING_ACTIVE_COMPRESSION",
                "severity": "LOW",
                "message": f"{len(buttons_without_active)} button(s) lack active click compression (active:scale-95)."
            })
            score -= 10

        grade = "S (GOD LEVEL)" if score >= 90 else "A (EXCELLENT)" if score >= 80 else "B (AVERAGE)" if score >= 60 else "F (GENERIC AI)"
        return {
            "filename": filename,
            "score": max(0, score),
            "grade": grade,
            "issues": issues,
            "passed": score >= 80
        }

    @classmethod
    def audit_path(cls, path: str) -> List[Dict[str, Any]]:
        results = []
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                results.append(cls.audit_code(f.read(), os.path.basename(path)))
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith((".html", ".tsx", ".jsx", ".vue", ".svelte", ".css")):
                        full_file = os.path.join(root, file)
                        with open(full_file, "r", encoding="utf-8", errors="ignore") as f:
                            results.append(cls.audit_code(f.read(), os.path.relpath(full_file, path)))
        return results
