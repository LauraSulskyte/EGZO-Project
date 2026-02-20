# -*- coding: utf-8 -*-
"""3_Biudzetas_ir_KPI.py

Vizualizuoja:
1) Projekto „EGZOTIC SOS“ MVP biudžeto paskirstymą
2) Pamatuojamus (SMART) tikslus / KPI

Duomenys paimti tik iš pateikto Word dokumento:
- 7.2 Projekto „EGZOTIC SOS“ preliminarus biudžetas (5 lentelė)
- 3.2 Pamatuojami (SMART) tikslai

Techniniai reikalavimai:
- Baltas fonas
- Tamsiai mėlyna / violetinė spalvų paletė
- Pabaigoje: plt.savefig('3_Biudzetas_ir_KPI.pdf')
"""

import textwrap
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def lt_money(x: float) -> str:
    """Formatuoja skaičių į lietuvišką pinigų formatą (tarpai tūkstančiams, kablelis centams)."""
    s = f"{x:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", " ") + " Eur"


def wrap(txt: str, width: int) -> str:
    return "\n".join(textwrap.fill(line, width=width) for line in txt.split("\n"))


# -----------------------------
# Biudžeto duomenys (5 lentelė)
# -----------------------------
# Eilučių sumos (Eur):
# - Programavimo darbai: 5 850,00
# - Serverių nuoma: 83,88
# - Domenas (.lt): 13,99
# - SSL sertifikatas (Let's Encrypt): 0,00
# - BDAR dokumentacijos paketas: 650,00
# - Teisinė konsultacija: 350,00
# - Socialinių tinklų reklama: 600,00
# - Vizualinė komunikacija: 150,00

budget_items = [
    ("IT kūrimas", "Programavimo darbai (MVP: registras, sveikata, SOS, admin, testai)", 5850.00),
    ("Infrastruktūra", "Serverių nuoma (cloud/VPS) – 12 mėn.", 83.88),
    ("Infrastruktūra", "Domenas (.lt) – 1 metai", 13.99),
    ("Infrastruktūra", "SSL sertifikatas (TLS) – Let's Encrypt", 0.00),
    ("Teisinė atitiktis", "BDAR dokumentacijos paketas", 650.00),
    ("Teisinė atitiktis", "Teisinė konsultacija (BDAR rizikų, sutarčių ir procesų peržiūra)", 350.00),
    ("Rinkodara ir komunikacija", "Socialinių tinklų reklamos biudžetas (žinomumo startas) – 3 mėn.", 600.00),
    ("Rinkodara ir komunikacija", "Vizualinė komunikacija (banerių/šablonų parengimas)", 150.00),
]

# Kategorijų sumos (apskaičiuojamos iš lentelės eilučių)
category_totals = {}
for cat, _, amount in budget_items:
    category_totals[cat] = category_totals.get(cat, 0.0) + amount

categories = list(category_totals.keys())
values = [category_totals[c] for c in categories]
total_budget = sum(values)

# -----------------------------
# KPI duomenys (SMART tikslai)
# -----------------------------
kpis = [
    {
        "kpi": "MVP viešas paleidimas",
        "target": "Iki 2026-06-01 sukurti ir viešai paleisti MVP su funkcijomis: vartotojo registracija ir prisijungimas; egzotinių gyvūnų registras su unikaliu identifikatoriumi; sveikatos kortelė (vizitai, skiepai, diagnozės, pastabos); edukacinių gidų biblioteka; prieglaudų globotinių skelbimai (peržiūra ir kontaktas).",
        "deadline": "2026-06-01",
    },
    {
        "kpi": "Naudotojų pritraukimas",
        "target": "Per 6 mėnesius po paleidimo pasiekti ≥ 300 registruotų naudotojų, iš kurių ≥ 100 aktyvūs (bent 1 prisijungimas per mėnesį).",
        "deadline": "Per 6 mėn. po paleidimo",
    },
    {
        "kpi": "Edukacijos turinys",
        "target": "Iki 2026-06-01 platformoje pateikti patikrintus priežiūros aprašus ne mažiau kaip 40 egzotinių gyvūnų rūšių, suskirstytų į pagrindines grupes (ropliai, paukščiai, graužikai ir kt.).",
        "deadline": "2026-06-01",
    },
    {
        "kpi": "BDAR atitiktis",
        "target": "Iki 2026-05-15 užtikrinti atitiktį BDAR ir LR duomenų apsaugos reikalavimams: parengta privatumo informacija; įdiegtas sutikimų valdymas; prieigos rolės; duomenų ištrynimo funkcija; šifravimas; atsarginės kopijos.",
        "deadline": "2026-05-15",
    },
    {
        "kpi": "Partnerystės",
        "target": "Iki 2026-03-01 pasirašyti bent 3 bendradarbiavimo susitarimus / ketinimų protokolus su: VšĮ „Egzotic SOS“; bent viena veterinarijos klinika, dirbančia su egzotiniais gyvūnais; bent viena gyvūnų gerovės ar švietimo organizacija.",
        "deadline": "2026-03-01",
    },
]

# -----------------------------
# Stilius / spalvos
# -----------------------------
C_DARK_BLUE = "#0B1F3B"
C_BLUE = "#2B4F9E"
C_VIOLET = "#5B2C83"
C_VIOLET_2 = "#6B3FA0"
C_LIGHT_BLUE = "#EEF4FF"
C_LIGHT_VIOLET = "#F4EEFF"
C_BORDER = "#D6D6D6"

palette = [C_DARK_BLUE, C_BLUE, C_VIOLET, C_VIOLET_2]

# -----------------------------
# Maketas: viršuje biudžetas, apačioje KPI lentelė
# -----------------------------
fig = plt.figure(figsize=(16, 11))
fig.patch.set_facecolor("white")

gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.35], hspace=0.18)

# --- Biudžetas (donut) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor("white")
ax1.set_title("MVP biudžeto paskirstymas pagal sąnaudų kategorijas", fontsize=14, fontweight="bold", color=C_DARK_BLUE, pad=12)

wedges, _ = ax1.pie(
    values,
    startangle=90,
    colors=palette[: len(values)],
    wedgeprops=dict(width=0.42, edgecolor="white"),
)

ax1.text(
    0,
    0,
    wrap(f"Iš viso\n{lt_money(total_budget)}", 18),
    ha="center",
    va="center",
    fontsize=12,
    color=C_DARK_BLUE,
    fontweight="bold",
)

legend_labels = [f"{c}: {lt_money(v)}" for c, v in zip(categories, values)]
ax1.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=True, facecolor="white", edgecolor=C_BORDER, fontsize=10)

ax1.set_aspect("equal")

# --- KPI lentelė (infografiko stiliaus) ---
ax2 = fig.add_subplot(gs[1, 0])
ax2.set_facecolor("white")
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis("off")

ax2.text(
    0.5,
    0.98,
    "Pamatuojami tikslai (KPI / SMART)",
    ha="center",
    va="top",
    fontsize=14,
    fontweight="bold",
    color=C_DARK_BLUE,
)

# Lentelės geometrija
left = 0.02
right = 0.98
top = 0.92
bottom = 0.06

# Stulpeliai: KPI | Tikslas | Terminas
col_x = [left, 0.22, 0.82, right]  # 3 stulpeliai
header_h = 0.10
rows = len(kpis)
row_h = (top - bottom - header_h) / rows

# Antraštės fonas
ax2.add_patch(Rectangle((left, top - header_h), right - left, header_h, facecolor=C_DARK_BLUE, edgecolor=C_DARK_BLUE))
ax2.text((col_x[0] + col_x[1]) / 2, top - header_h / 2, "KPI", ha="center", va="center", fontsize=11, color="white", fontweight="bold")
ax2.text((col_x[1] + col_x[2]) / 2, top - header_h / 2, "Tikslas", ha="center", va="center", fontsize=11, color="white", fontweight="bold")
ax2.text((col_x[2] + col_x[3]) / 2, top - header_h / 2, "Terminas", ha="center", va="center", fontsize=11, color="white", fontweight="bold")

# Linijos tarp stulpelių (header)
for x in col_x[1:-1]:
    ax2.plot([x, x], [top - header_h, top], color="white", linewidth=1.0)

# Eilutės
for i, item in enumerate(kpis):
    y0 = top - header_h - (i + 1) * row_h
    fill = C_LIGHT_BLUE if i % 2 == 0 else C_LIGHT_VIOLET
    ax2.add_patch(Rectangle((left, y0), right - left, row_h, facecolor=fill, edgecolor=C_BORDER, linewidth=1.0))

    # stulpelių vertikalios linijos
    for x in col_x[1:-1]:
        ax2.plot([x, x], [y0, y0 + row_h], color=C_BORDER, linewidth=1.0)

    # Tekstai (su wrap)
    kpi_txt = wrap(item["kpi"], 18)
    target_txt = wrap(item["target"], 72)
    deadline_txt = wrap(item["deadline"], 18)

    ax2.text(col_x[0] + 0.01, y0 + row_h - 0.02, kpi_txt, ha="left", va="top", fontsize=10, color=C_DARK_BLUE, fontweight="bold")
    ax2.text(col_x[1] + 0.01, y0 + row_h - 0.02, target_txt, ha="left", va="top", fontsize=9.2, color=C_DARK_BLUE)
    ax2.text(col_x[2] + 0.01, y0 + row_h - 0.02, deadline_txt, ha="left", va="top", fontsize=10, color=C_DARK_BLUE)

# Šaltinio pastaba
ax2.text(
    0.02,
    0.01,
    "Duomenų šaltinis: 5 lentelė (biudžetas) ir 3.2 skyrius (SMART tikslai).",
    ha="left",
    va="bottom",
    fontsize=9,
    color="#555555",
)

plt.savefig('3_Biudzetas_ir_KPI.pdf')
