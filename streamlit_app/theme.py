"""
theme.py — AntonIA · Mar.IA Group
Sistema de diseño centralizado: colores, tipografía, CSS compartido.

Todos los módulos deben importar colores desde aquí.
NUNCA definir colores directamente en cada módulo.
"""

# ── Paleta principal ──────────────────────────────────────────
GOLD       = "#c9963a"
GOLD_HOVER = "#e0ab4a"
GOLD_DIM   = "rgba(201,150,58,0.12)"
GOLD_DIM2  = "rgba(201,150,58,0.06)"
DARK       = "#141210"
CARD       = "#1e1b16"
CARD2      = "#221e17"
MUTED      = "#a09070"
WHITE      = "#f5f0e8"
GREEN      = "#22c55e"
RED        = "#ef4444"
BLUE       = "#3b82f6"
PARCHMENT  = "#f0e9dc"

# ── Tipografía ────────────────────────────────────────────────
FONT_SERIF  = "'Playfair Display', Georgia, serif"
FONT_SANS   = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"

# ── Alias compatibles (para módulos que usaban _GOLD etc.) ───
_GOLD  = GOLD
_DARK  = DARK
_CARD  = CARD
_CARD2 = CARD2
_MUTED = MUTED
_WHITE = WHITE
_GREEN = GREEN
_RED   = RED
_BLUE  = BLUE
