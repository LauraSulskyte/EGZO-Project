# -*- coding: utf-8 -*-
"""2_Strategija_ir_Problematika.py

Vizualizuoja:
1) Projekto trilypį tikslą (Apimtis, Laikas, Biudžetas)
2) Sprendžiamą problematiką

Visi teiginiai/duomenys paimti iš pateikto Word dokumento skyriaus:
- 3.2 Pamatuojami (SMART) tikslai
- 3.3 Sprendžiama problematika
- 6 Projekto įgyvendinimo planas (laikotarpis)
- 7.2 Preliminarus biudžetas

Techniniai reikalavimai:
- Baltas fonas
- Tamsiai mėlyna / violetinė spalvų paletė
- Pabaigoje: plt.savefig('2_Strategija_ir_Problematika.pdf')
"""

import textwrap
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon


def wrap(txt: str, width: int) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in txt.split("\n"))


# -----------------------------
# Faktai iš dokumento
# -----------------------------
# Apimtis (MVP funkcijos) – pagal SMART tikslą (iki 2026-06-01)
SCOPE_BULLETS = [
    "Vartotojo registracija ir prisijungimas",
    "Egzotinių gyvūnų registras su unikaliu identifikatoriumi",
    "Sveikatos kortelė (vizitai, skiepai, diagnozės, pastabos)",
    "Edukacinių gidų biblioteka",
    "Prieglaudų globotinių skelbimai (peržiūra ir kontaktas)",
]

# Laikas – pagal projekto laikotarpį (2025-11-01–2026-06-15) ir SMART terminus
TIME_LINES = [
    "Projekto laikotarpis: 2025-11-01 – 2026-06-15",
    "MVP viešas paleidimas: iki 2026-06-01",
]

# Biudžetas – pagal 7.2 skyriaus teiginį (neviršija 8 000 Eur) ir 5 lentelės sumas
# (Suma apskaičiuojama iš lentelės eilučių: 5850 + 83.88 + 13.99 + 0 + 650 + 350 + 600 + 150)
BUDGET_TOTAL_EUR = 7697.87
BUDGET_CAP_EUR = 8000.00
BUDGET_HIGHLIGHTS = [
    "Programavimo darbai: 5 850,00 Eur",
    "BDAR dokumentacijos paketas: 650,00 Eur",
    "Socialinių tinklų reklamos biudžetas: 600,00 Eur",
]

# Problematika – pagal 3.3 skyrių (4 punktai)
PROBLEMS = [
    (
        "1) Žinių ir kompetencijos trūkumas",
        "Dalis savininkų įsigyja egzotinius gyvūnus neįvertinę specifinių poreikių (temperatūra, drėgmė, mityba, elgsena). Dėl to dažnėja sveikatos sutrikimai ir gyvūnų atidavimas prieglaudoms.",
    ),
    (
        "2) Duomenų fragmentiškumas",
        "Sveikatos, procedūrų ir priežiūros istorija dažnai fiksuojama nenuosekliai (skirtingose vietose, užrašuose ar išvis nefiksuojama). Keičiantis globėjui informacija prarandama, todėl nukenčia gydymo ir priežiūros kokybė.",
    ),
    (
        "3) Ribota specializuota pagalba",
        "Egzotinių gyvūnų specialistų ir organizacijų, galinčių padėti, nėra daug, o informacija apie pagalbos galimybes ne visada lengvai randama. Dėl to sprendimai dažnai vėluoja.",
    ),
    (
        "4) Silpnas reagavimo mechanizmas",
        "Trūksta paprasto būdo greitai pranešti apie rastą, pabėgusį ar netinkamai laikomą egzotinį gyvūną ir koordinuoti savanorių bei prieglaudų veiksmus.",
    ),
]

# -----------------------------
# Stilius / spalvos
# -----------------------------
C_DARK_BLUE = "#0B1F3B"
C_BLUE = "#2B4F9E"
C_VIOLET = "#5B2C83"
C_LIGHT_BLUE = "#EEF4FF"
C_LIGHT_VIOLET = "#F4EEFF"
C_BORDER = "#D6D6D6"


fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor("white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Pavadinimas
ax.text(
    0.5,
    0.965,
    "„EGZOTIC SOS“: trilypis tikslas (Apimtis–Laikas–Biudžetas) ir sprendžiama problematika",
    ha="center",
    va="top",
    fontsize=16,
    fontweight="bold",
    color=C_DARK_BLUE,
)

# Skyriai (antraštės)
ax.text(0.28, 0.90, "Trilypis tikslas", ha="center", va="center", fontsize=13, fontweight="bold", color=C_DARK_BLUE)
ax.text(0.79, 0.90, "Sprendžiama problematika", ha="center", va="center", fontsize=13, fontweight="bold", color=C_DARK_BLUE)

# -----------------------------
# Kairė: trikampis (Apimtis, Laikas, Biudžetas)
# -----------------------------
tri = Polygon([(0.28, 0.84), (0.10, 0.55), (0.46, 0.55)], closed=True, facecolor="#FFFFFF", edgecolor=C_BORDER, linewidth=1.5)
ax.add_patch(tri)
# Linijos (akcentas)
ax.plot([0.28, 0.10], [0.84, 0.55], color=C_BLUE, linewidth=2)
ax.plot([0.28, 0.46], [0.84, 0.55], color=C_VIOLET, linewidth=2)
ax.plot([0.10, 0.46], [0.55, 0.55], color=C_DARK_BLUE, linewidth=2)

# Apimtis (viršus)
box_scope = Rectangle((0.14, 0.73), 0.28, 0.14, facecolor=C_LIGHT_BLUE, edgecolor=C_BORDER, linewidth=1.2)
ax.add_patch(box_scope)
ax.text(0.28, 0.855, "APIMTIS", ha="center", va="center", fontsize=11, fontweight="bold", color=C_DARK_BLUE)
scope_text = "• " + "\n• ".join(SCOPE_BULLETS)
ax.text(0.155, 0.835, wrap(scope_text, 45), ha="left", va="top", fontsize=9.5, color=C_DARK_BLUE)

# Laikas (kairė apačia)
box_time = Rectangle((0.03, 0.49), 0.24, 0.12, facecolor=C_LIGHT_VIOLET, edgecolor=C_BORDER, linewidth=1.2)
ax.add_patch(box_time)
ax.text(0.15, 0.595, "LAIKAS", ha="center", va="center", fontsize=11, fontweight="bold", color=C_DARK_BLUE)
time_text = "\n".join(TIME_LINES)
ax.text(0.045, 0.575, wrap(time_text, 32), ha="left", va="top", fontsize=9.5, color=C_DARK_BLUE)

# Biudžetas (dešinė apačia)
box_budget = Rectangle((0.29, 0.49), 0.24, 0.12, facecolor=C_LIGHT_BLUE, edgecolor=C_BORDER, linewidth=1.2)
ax.add_patch(box_budget)
ax.text(0.41, 0.595, "BIUDŽETAS", ha="center", va="center", fontsize=11, fontweight="bold", color=C_DARK_BLUE)

budget_lines = [
    f"Preliminarus MVP biudžetas: {BUDGET_TOTAL_EUR:,.2f} Eur".replace(",", "X").replace(".", ",").replace("X", " "),
    f"Neviršija {BUDGET_CAP_EUR:,.0f} Eur".replace(",", " "),
    "\n".join(BUDGET_HIGHLIGHTS),
]
budget_text = "\n".join(budget_lines)
ax.text(0.305, 0.575, wrap(budget_text, 34), ha="left", va="top", fontsize=9.5, color=C_DARK_BLUE)

# -----------------------------
# Dešinė: problematika (4 blokai)
# -----------------------------
# Išdėstymas 2x2 (didesni blokai, kad tilptų tekstas)
box_w = 0.18
box_h = 0.165
x0 = 0.60
y0 = 0.72
gap_x = 0.02
gap_y = 0.03

problem_positions = [
    (x0, y0),  # 1
    (x0 + box_w + gap_x, y0),  # 2
    (x0, y0 - box_h - gap_y),  # 3
    (x0 + box_w + gap_x, y0 - box_h - gap_y),  # 4
]

for (title, body), (x, y) in zip(PROBLEMS, problem_positions):
    fill = C_LIGHT_VIOLET if "1)" in title or "3)" in title else C_LIGHT_BLUE
    rect = Rectangle((x, y), box_w, box_h, facecolor=fill, edgecolor=C_BORDER, linewidth=1.2)
    ax.add_patch(rect)
    ax.text(x + box_w / 2, y + box_h - 0.02, title, ha="center", va="top", fontsize=10, fontweight="bold", color=C_DARK_BLUE)
    ax.text(x + 0.01, y + box_h - 0.05, wrap(body, 34), ha="left", va="top", fontsize=8.8, color=C_DARK_BLUE)

# Pastaba (šaltinių nuoroda į dokumento skyrius)
ax.text(
    0.02,
    0.03,
    "Duomenų šaltinis: projekto dokumento 3.2–3.3, 6 ir 7.2 skyriai (formuluotės, terminai, biudžeto eilutės).",
    ha="left",
    va="bottom",
    fontsize=9,
    color="#555555",
)

plt.savefig('2_Strategija_ir_Problematika.pdf')
