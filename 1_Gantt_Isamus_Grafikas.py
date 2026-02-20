# -*- coding: utf-8 -*-
"""1_Gantt_Isamus_Grafikas.py

Sugeneruoja išsamų „EGZOTIC SOS“ projekto Ganto grafiką (PDF).

Duomenys (užduotys, datos, etapų pavadinimai) paimti iš pateikto Word dokumento
„EGZOTIC SOS informacinė sistema: egzotinių gyvūnų registras ir sveikatos valdymas“,
4 lentelės (projekto įgyvendinimo grafikas ir atsakomybės).

Techniniai reikalavimai:
- Baltas fonas
- Tamsiai mėlyna / violetinė spalvų paletė
- Horizontalioje ašyje – datos, vertikalioje – užduotys
- Kiekvienas etapas turi savo spalvą
- Pabaigoje: plt.savefig('1_Gantt_Isamus_Grafikas.pdf')
"""

import textwrap
from datetime import datetime
import matplotlib

# Saugus backend (tinka ir be grafinės aplinkos)
matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def d(date_str: str) -> datetime:
    """Konvertuoja YYYY-MM-DD į datetime."""
    return datetime.strptime(date_str, "%Y-%m-%d")


# -----------------------------
# Duomenys iš Word (4 lentelė)
# -----------------------------
# Pastaba: pateikiami ir etapai, ir jų užduotys (su numeracija 1.1, 1.2, ...).
TASKS = [
    # 1. Inicijavimas
    {"id": "1", "task": "Inicijavimas (etapas)", "stage": "Inicijavimas", "start": d("2025-11-01"), "end": d("2025-11-21"), "kind": "stage"},
    {"id": "1.1", "task": "Projekto inicijavimo susitikimas su užsakovu ir projekto chartijos (tikslai, sėkmės kriterijai) patvirtinimas", "stage": "Inicijavimas", "start": d("2025-11-01"), "end": d("2025-11-07"), "kind": "task"},
    {"id": "1.2", "task": "Projekto valdymo struktūros parengimas (rolės, komunikacijos planas, Monday.com lentos struktūra, dokumentų saugykla)", "stage": "Inicijavimas", "start": d("2025-11-01"), "end": d("2025-11-14"), "kind": "task"},
    {"id": "1.3", "task": "Suinteresuotųjų šalių pirminė identifikacija ir įtraukimo plano gairės", "stage": "Inicijavimas", "start": d("2025-11-08"), "end": d("2025-11-21"), "kind": "task"},
    {"id": "1.4", "task": "Pradinė rizikų identifikacija ir rizikų registro šablono parengimas", "stage": "Inicijavimas", "start": d("2025-11-15"), "end": d("2025-11-21"), "kind": "task"},

    # 2. Analizė
    {"id": "2", "task": "Analizė (etapas)", "stage": "Analizė", "start": d("2025-11-10"), "end": d("2025-12-20"), "kind": "stage"},
    {"id": "2.1", "task": "Esamos situacijos ir procesų analizė (registro, sveikatos duomenų, SOS informavimo scenarijai)", "stage": "Analizė", "start": d("2025-11-10"), "end": d("2025-11-28"), "kind": "task"},
    {"id": "2.2", "task": "Reikalavimų rinkimas ir MVP apimties apibrėžimas (funkciniai reikalavimai, prioritetai, priėmimo kriterijų gairės)", "stage": "Analizė", "start": d("2025-11-17"), "end": d("2025-12-05"), "kind": "task"},
    {"id": "2.3", "task": "Nefunkcinių reikalavimų suformavimas (BDAR, saugumas, rolės, audito poreikis)", "stage": "Analizė", "start": d("2025-11-24"), "end": d("2025-12-12"), "kind": "task"},
    {"id": "2.4", "task": "UI/UX prototipo parengimo koordinavimas (naudotojų keliai, wireframe, patvirtinimas su užsakovu)", "stage": "Analizė", "start": d("2025-12-01"), "end": d("2025-12-19"), "kind": "task"},
    {"id": "2.5", "task": "Grafiko ir biudžeto prielaidų suvedimas (planavimo bazinė linija, darbų sekos logika)", "stage": "Analizė", "start": d("2025-12-08"), "end": d("2025-12-20"), "kind": "task"},

    # 3. Kūrimo koordinavimas
    {"id": "3", "task": "Kūrimo koordinavimas (etapas) (vyksta lygiagrečiai su turinio rengimu)", "stage": "Kūrimo koordinavimas", "start": d("2025-12-15"), "end": d("2026-04-30"), "kind": "stage"},
    {"id": "3.1", "task": "Techninės užduoties (SRS / backlog) parengimas ir perdavimas vykdytojui (programuotojams)", "stage": "Kūrimo koordinavimas", "start": d("2025-12-15"), "end": d("2026-01-10"), "kind": "task"},
    {"id": "3.2", "task": "Išorinių IT resursų įsigijimo/atrankos koordinavimas (sutartys, susitarimai, darbų apimtis)", "stage": "Kūrimo koordinavimas", "start": d("2025-12-15"), "end": d("2026-01-15"), "kind": "task"},
    {"id": "3.3", "task": "MVP kūrimo darbų koordinavimas sprintais (statuso peržiūros, priėmimo kriterijai, užduočių prioritetai)", "stage": "Kūrimo koordinavimas", "start": d("2026-01-16"), "end": d("2026-04-30"), "kind": "task"},
    {"id": "3.4", "task": "Infrastruktūros paruošimo koordinavimas (DEV/TEST/PROD aplinkos, atsarginės kopijos, domenas, SSL)", "stage": "Kūrimo koordinavimas", "start": d("2026-01-16"), "end": d("2026-02-15"), "kind": "task"},
    {"id": "3.5", "task": "Duomenų modelio ir turinio struktūros suderinimas su techniniu įgyvendinimu (objektai, turinio tipai, importas)", "stage": "Kūrimo koordinavimas", "start": d("2026-02-01"), "end": d("2026-02-28"), "kind": "task"},

    # 4. Turinio rengimas
    {"id": "4", "task": "Turinio rengimas (etapas) (vyksta lygiagrečiai su kūrimo koordinavimu)", "stage": "Turinio rengimas", "start": d("2025-12-15"), "end": d("2026-05-15"), "kind": "stage"},
    {"id": "4.1", "task": "Edukacinio turinio architektūros parengimas (rūšies kortelės šablonas, kategorijos, terminija)", "stage": "Turinio rengimas", "start": d("2025-12-15"), "end": d("2026-01-05"), "kind": "task"},
    {"id": "4.2", "task": "Edukacinių gidų rengimas (prioritetinės rūšys, laikymo sąlygos, mityba, dažniausi sveikatos klausimai)", "stage": "Turinio rengimas", "start": d("2026-01-06"), "end": d("2026-05-01"), "kind": "task"},
    {"id": "4.3", "task": "CITES ir teisėtumo dokumentacijos santraukų parengimas (informacinės atmintinės, dokumentų sąrašai)", "stage": "Turinio rengimas", "start": d("2026-02-01"), "end": d("2026-04-15"), "kind": "task"},
    {"id": "4.4", "task": "Turinio redagavimas ir kokybės kontrolė (šaltinių patikra, ekspertinė peržiūra, suvienodinimas)", "stage": "Turinio rengimas", "start": d("2026-03-01"), "end": d("2026-05-10"), "kind": "task"},
    {"id": "4.5", "task": "Pradinio turinio įkėlimo į testinę aplinką koordinavimas ir turinio migracijos patikra", "stage": "Turinio rengimas", "start": d("2026-04-15"), "end": d("2026-05-15"), "kind": "task"},

    # 5. Testavimas
    {"id": "5", "task": "Testavimas (etapas)", "stage": "Testavimas", "start": d("2026-05-01"), "end": d("2026-06-05"), "kind": "stage"},
    {"id": "5.1", "task": "Testavimo strategijos ir testų scenarijų parengimas (funkcinis, integracinis, priėmimo testai)", "stage": "Testavimas", "start": d("2026-05-01"), "end": d("2026-05-08"), "kind": "task"},
    {"id": "5.2", "task": "Beta testavimo organizavimas su užsakovu (UAT scenarijai, grįžtamasis ryšys, registravimas)", "stage": "Testavimas", "start": d("2026-05-09"), "end": d("2026-05-22"), "kind": "task"},
    {"id": "5.3", "task": "Defektų registravimas, prioritetizavimas ir taisymų koordinavimas (stabilizavimo sprintas)", "stage": "Testavimas", "start": d("2026-05-16"), "end": d("2026-06-05"), "kind": "task"},
    {"id": "5.4", "task": "BDAR atitikties patikra (privatumo informacija, sutikimai, duomenų subjektų teisės)", "stage": "Testavimas", "start": d("2026-05-20"), "end": d("2026-06-05"), "kind": "task"},
    {"id": "5.5", "task": "Turinio kokybės patikra prieš paleidimą (gidų užbaigimas, nuorodos, terminija)", "stage": "Testavimas", "start": d("2026-05-20"), "end": d("2026-06-05"), "kind": "task"},

    # 6. Paleidimas ir stabilizavimas
    {"id": "6", "task": "Paleidimas ir stabilizavimas (etapas)", "stage": "Paleidimas ir stabilizavimas", "start": d("2026-06-06"), "end": d("2026-06-15"), "kind": "stage"},
    {"id": "6.1", "task": "Produkcinės aplinkos parengimas ir konfigūracija (serveris, domenas, SSL, monitoringas, backup)", "stage": "Paleidimas ir stabilizavimas", "start": d("2026-06-06"), "end": d("2026-06-10"), "kind": "task"},
    {"id": "6.2", "task": "Naudotojų ir administratoriaus instrukcijų parengimas; vidinių procesų aprašai (registras, sveikata, SOS, turinio atnaujinimas)", "stage": "Paleidimas ir stabilizavimas", "start": d("2026-06-06"), "end": d("2026-06-12"), "kind": "task"},
    {"id": "6.3", "task": "Viešo paleidimo (soft launch) komunikacijos koordinavimas (žinutės, edukacinė komunikacija, rėmėjų informavimas)", "stage": "Paleidimas ir stabilizavimas", "start": d("2026-06-11"), "end": d("2026-06-15"), "kind": "task"},
    {"id": "6.4", "task": "Stabilizavimo laikotarpio stebėsena ir incidentų valdymo koordinavimas (pirmoji savaitė)", "stage": "Paleidimas ir stabilizavimas", "start": d("2026-06-11"), "end": d("2026-06-15"), "kind": "task"},
    {"id": "6.5", "task": "Projekto užbaigimas (lessons learned, galutinė ataskaita, rekomendacijos plėtrai)", "stage": "Paleidimas ir stabilizavimas", "start": d("2026-06-14"), "end": d("2026-06-15"), "kind": "task"},

    # Tęstinė veikla
    {"id": "T", "task": "Tęstinė veikla: projekto valdymas ir kontrolė", "stage": "Tęstinė veikla", "start": d("2025-11-01"), "end": d("2026-06-15"), "kind": "task"},
]

# Spalvos (tamsiai mėlyna / violetinė paletė)
STAGE_COLORS = {
    "Inicijavimas": "#0B1F3B",
    "Analizė": "#153B73",
    "Kūrimo koordinavimas": "#2B4F9E",
    "Turinio rengimas": "#4B2C7A",
    "Testavimas": "#5B2C83",
    "Paleidimas ir stabilizavimas": "#6B3FA0",
    "Tęstinė veikla": "#1F2A44",
}

# -----------------------------
# Grafiko braižymas
# -----------------------------
labels = [textwrap.fill(f"{t['id']}  {t['task']}", width=68) for t in TASKS]
n = len(TASKS)
fig_height = max(12, n * 0.55)

fig, ax = plt.subplots(figsize=(18, fig_height))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

for i, item in enumerate(TASKS):
    start_num = mdates.date2num(item["start"])
    end_num = mdates.date2num(item["end"])
    width = end_num - start_num

    color = STAGE_COLORS.get(item["stage"], "#2B4F9E")
    alpha = 0.35 if item["kind"] == "stage" else 0.92
    edge = "#FFFFFF" if item["kind"] == "stage" else "none"

    ax.barh(
        y=i,
        width=width,
        left=start_num,
        height=0.72,
        color=color,
        alpha=alpha,
        edgecolor=edge,
        linewidth=1.0 if item["kind"] == "stage" else 0.0,
    )

ax.set_yticks(range(n))
ax.set_yticklabels(labels, fontsize=8.5)
ax.invert_yaxis()

ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))

ax.grid(True, axis="x", which="major", linestyle="-", linewidth=0.6, color="#E6E6E6")
ax.grid(True, axis="x", which="minor", linestyle=":", linewidth=0.4, color="#F0F0F0")
ax.tick_params(axis="x", labelrotation=45)

min_start = min(t["start"] for t in TASKS)
max_end = max(t["end"] for t in TASKS)
ax.set_xlim(mdates.date2num(min_start) - 3, mdates.date2num(max_end) + 3)

ax.set_title(
    "„EGZOTIC SOS“ projekto įgyvendinimo planas – išsamus Ganto grafikas\n(2025-11-01 – 2026-06-15)",
    fontsize=14,
    pad=18,
    color="#0B1F3B",
    fontweight="bold",
)
ax.set_xlabel("Datos", fontsize=11, color="#0B1F3B")
ax.set_ylabel("Užduotys", fontsize=11, color="#0B1F3B")

legend_handles = [Patch(facecolor=c, edgecolor="none", label=s) for s, c in STAGE_COLORS.items()]
ax.legend(
    handles=legend_handles,
    loc="lower right",
    frameon=True,
    framealpha=0.95,
    facecolor="white",
    edgecolor="#DDDDDD",
    fontsize=9,
    title="Etapai",
    title_fontsize=10,
)

fig.subplots_adjust(left=0.40, right=0.98, top=0.92, bottom=0.08)
fig.text(
    0.01,
    0.01,
    "Duomenų šaltinis: projekto dokumento 4 lentelė (pradžios ir pabaigos datos, užduočių numeracija).",
    fontsize=9,
    color="#555555",
)

plt.savefig('1_Gantt_Isamus_Grafikas.pdf')
