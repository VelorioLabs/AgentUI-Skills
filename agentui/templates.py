"""Pre-Engineered UI Component Templates."""
from typing import Dict

TEMPLATES: Dict[str, str] = {
    "bento-card": """<div class="group relative overflow-hidden rounded-2xl border border-white/10 bg-slate-900/60 p-6 backdrop-blur-xl transition-all duration-300 hover:-translate-y-1 hover:border-cyan-500/30 hover:shadow-2xl hover:shadow-cyan-500/10">
  <div class="pointer-events-none absolute -right-16 -top-16 h-40 w-40 rounded-full bg-cyan-500/15 blur-3xl transition-transform duration-500 group-hover:scale-150"></div>
  <div class="relative z-10">
    <div class="flex items-center justify-between">
      <span class="font-mono text-xs font-semibold tracking-wider text-cyan-400">STATUS // ACTIVE</span>
      <span class="flex h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#00ff88]"></span>
    </div>
    <h3 class="mt-4 font-sans text-xl font-bold text-white group-hover:text-cyan-300 transition-colors">
      Component Title
    </h3>
    <p class="mt-2 text-sm leading-relaxed text-slate-400">
      High performance description with detailed feature highlights and live metrics.
    </p>
  </div>
</div>""",

    "command-palette": """<div class="fixed inset-0 z-50 flex items-start justify-center bg-black/60 p-4 pt-24 backdrop-blur-md">
  <div class="w-full max-w-xl overflow-hidden rounded-2xl border border-white/15 bg-slate-950/90 shadow-2xl shadow-black/80 backdrop-blur-2xl">
    <div class="flex items-center border-b border-white/10 px-4 py-3">
      <span class="text-slate-400 text-lg mr-3">🔍</span>
      <input type="text" placeholder="Type a command or search..." class="w-full bg-transparent font-mono text-sm text-white placeholder-slate-500 outline-none">
      <kbd class="rounded border border-white/20 bg-white/5 px-2 py-0.5 font-mono text-[10px] text-slate-400">ESC</kbd>
    </div>
  </div>
</div>""",

    "status-pill": """<div class="inline-flex items-center gap-2 rounded-full border border-emerald-500/30 bg-emerald-500/10 px-3 py-1 font-mono text-xs font-semibold text-emerald-400">
  <span class="relative flex h-2 w-2">
    <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
    <span class="relative inline-flex h-2 w-2 rounded-full bg-emerald-500"></span>
  </span>
  <span>SYSTEM ONLINE</span>
</div>""",

    "navbar": """<nav class="fixed top-5 left-1/2 -translate-x-1/2 z-50 flex items-center gap-6 rounded-full border border-white/10 bg-slate-950/70 px-6 py-2.5 shadow-2xl shadow-black/50 backdrop-blur-xl">
  <div class="flex items-center gap-2">
    <div class="h-3 w-3 rounded-full bg-cyan-400 shadow-[0_0_10px_#00f0ff]"></div>
    <span class="font-mono text-sm font-extrabold tracking-wider text-white">VIBE<span class="text-cyan-400">UI</span></span>
  </div>
</nav>"""
}

def get_template(name: str) -> str:
    return TEMPLATES.get(name.lower(), TEMPLATES["bento-card"])
