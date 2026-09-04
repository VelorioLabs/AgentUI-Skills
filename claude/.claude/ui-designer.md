# Claude Code UI/UX Design Guidelines

Whenever writing HTML, CSS, React, Vue, or Tailwind components:
- **Aesthetic Benchmark**: Match the visual excellence of Linear, Stripe, Vercel, or Cyberpunk HUDs.
- **Color Depth**: Dark-mode first. Use deep navy/slate blacks (`#07090e`), not flat gray (`#222`). Layer with subtle radial gradients.
- **Glassmorphism**: Use translucent cards with `backdrop-filter: blur(12px)` and 1px semi-transparent borders (`rgba(255,255,255,0.08)`).
- **Typography**: Pair clean sans-serif (`Inter`) for body copy with monospace (`JetBrains Mono`) for badges, codes, and numerical readouts.
- **Interactions**: Include smooth transitions (`duration-200`), hover lifts (`-translate-y-0.5`), and glowing focus rings.
