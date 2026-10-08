"""
Generate the 5 BestRun EV source documents for Document Grounding (Exercise 3).
Run: python3 generate_docs.py
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os


OUT_DIR = os.path.dirname(os.path.abspath(__file__))

BLUE = (0, 60, 140)
DARK = (30, 30, 30)
MID = (80, 80, 80)
LIGHT_BG = (240, 244, 250)
WHITE = (255, 255, 255)
LINE = (200, 210, 225)


def safe(text):
    """Replace characters outside latin-1 with ASCII equivalents."""
    subs = {
        "—": "-", "–": "-",
        "‘": "'", "’": "'",
        "“": '"', "”": '"',
        "×": "x",
        "≤": "<=", "≥": ">=",
        "°": " deg",
        "é": "e",
    }
    for ch, rep in subs.items():
        text = text.replace(ch, rep)
    return text


class Doc(FPDF):
    def __init__(self, title, subtitle=""):
        super().__init__()
        self.doc_title = title
        self.doc_subtitle = subtitle
        self.set_margins(20, 20, 20)
        self.set_auto_page_break(auto=True, margin=20)
        self.add_page()
        self._header_block()

    def _header_block(self):
        self.set_fill_color(*BLUE)
        self.rect(0, 0, 210, 38, "F")
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*WHITE)
        self.set_xy(20, 10)
        self.cell(0, 8, "BestRun EV", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", "", 10)
        self.set_xy(20, 20)
        self.cell(0, 6, safe(self.doc_title), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        if self.doc_subtitle:
            self.set_xy(20, 27)
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 5, safe(self.doc_subtitle))
        self.set_text_color(*DARK)
        self.set_y(45)

    def h1(self, text):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*BLUE)
        self.set_fill_color(*LIGHT_BG)
        self.cell(0, 8, safe(text), fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*BLUE)
        self.set_line_width(0.5)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(3)
        self.set_text_color(*DARK)

    def h2(self, text):
        self.ln(2)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*BLUE)
        self.cell(0, 6, safe(text), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*DARK)

    def body(self, text):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*MID)
        self.multi_cell(0, 5, safe(text))
        self.ln(1)
        self.set_text_color(*DARK)

    def bullet(self, text):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*MID)
        self.set_x(self.l_margin + 4)
        self.multi_cell(0, 5, safe("- " + text))
        self.set_x(self.l_margin)
        self.set_text_color(*DARK)

    def kv(self, key, value):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*DARK)
        self.cell(58, 5, safe(key + ":"))
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*MID)
        self.multi_cell(112, 5, safe(value))
        self.set_text_color(*DARK)

    def table(self, headers, rows, col_widths=None):
        if col_widths is None:
            w = 170 // len(headers)
            col_widths = [w] * len(headers)
        self.set_fill_color(*BLUE)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 8)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 6, safe(h), border=1, fill=True)
        self.ln()
        self.set_text_color(*DARK)
        self.set_font("Helvetica", "", 8)
        for ri, row in enumerate(rows):
            self.set_fill_color(*LIGHT_BG if ri % 2 == 0 else WHITE)
            for i, val in enumerate(row):
                self.cell(col_widths[i], 5, safe(str(val)), border=1, fill=True)
            self.ln()
        self.ln(2)

    def note(self, text):
        self.set_fill_color(255, 248, 225)
        self.set_draw_color(200, 160, 0)
        self.set_line_width(0.3)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 80, 0)
        self.multi_cell(0, 5, safe("Note: " + text), border=1, fill=True)
        self.set_text_color(*DARK)
        self.set_draw_color(*LINE)
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*MID)
        self.cell(
            0, 5,
            safe("BestRun EV - " + self.doc_title + " - CONFIDENTIAL - For authorized dealer use only"),
            align="C",
        )
        self.cell(0, 5, f"Page {self.page_no()}", align="R")


# ─────────────────────────────────────────────
# Document 1: Apex Series Technical Spec Sheet
# ─────────────────────────────────────────────
def doc1():
    pdf = Doc(
        "Apex Series Technical Spec Sheet",
        "Product Launch Reference - Authorized Dealers Only",
    )

    pdf.h1("Overview")
    pdf.body(
        "This document provides the complete technical specifications for the three models in the "
        "BestRun EV Apex Series. All figures are measured under standard test conditions (ISO 4210 / "
        "ECE R85) unless otherwise noted. Range figures use the WLTP Urban cycle."
    )

    models = [
        ("Apex City", [
            ("Category", "Urban commuter electric scooter"),
            ("Motor", "500 W hub motor (rear wheel)"),
            ("Peak Power", "750 W"),
            ("Battery", "36 V / 14.5 Ah Lithium-Ion (522 Wh)"),
            ("Range - Eco Mode", "85 km"),
            ("Range - Standard Mode", "60 km"),
            ("Top Speed", "25 km/h (EU regulation compliant)"),
            ("Charging Time (0-100%)", "4.5 hours (standard charger, 2A)"),
            ("Charging Time (0-80%)", "3.0 hours (standard charger, 2A)"),
            ("Frame", "6061 Aluminium alloy"),
            ("Weight (excl. battery)", "18.5 kg"),
            ("Weight (incl. battery)", "22.0 kg"),
            ("Max Rider Weight", "120 kg"),
            ("Wheel Size", "10 inch pneumatic"),
            ("Brakes", "Front & rear hydraulic disc, 160 mm rotors"),
            ("Suspension", "Front telescopic fork, 60 mm travel"),
            ("IP Rating", "IP54 (splash resistant)"),
            ("Colors", "Midnight Black, Pearl White, Urban Grey, Coral Red"),
            ("Dimensions (L x W x H)", "1,820 x 580 x 1,200 mm"),
            ("Folded Dimensions", "1,150 x 540 x 500 mm"),
            ("Connectivity", "Bluetooth 5.0, BestRun EV app (iOS / Android)"),
            ("Display", '3.5" TFT color display'),
            ("Lights", "LED front (800 lm) and rear (integrated)"),
            ("Warranty", "2 years frame, 1 year battery, 1 year electronics"),
        ]),
        ("Apex Trail", [
            ("Category", "Adventure electric bike"),
            ("Motor", "250 W mid-drive motor (Bafang M400)"),
            ("Peak Power", "500 W"),
            ("Battery", "48 V / 17.5 Ah Lithium-Ion (840 Wh)"),
            ("Range - Eco Mode", "140 km"),
            ("Range - Standard Mode", "95 km"),
            ("Range - Sport Mode", "60 km"),
            ("Top Speed", "25 km/h (pedelec, EU compliant)"),
            ("Charging Time (0-100%)", "5.5 hours (standard charger, 4A)"),
            ("Charging Time (0-80%)", "3.5 hours (standard charger, 4A)"),
            ("Frame", "6061 Aluminium alloy, hydroformed"),
            ("Weight (excl. battery)", "24.0 kg"),
            ("Weight (incl. battery)", "27.5 kg"),
            ("Max Rider Weight", "135 kg"),
            ("Wheel Size", "29 inch (front), 27.5 inch (rear), tubeless ready"),
            ("Brakes", "Shimano hydraulic disc, 180 mm rotors (front), 160 mm (rear)"),
            ("Suspension", "RockShox front fork, 120 mm travel; rear hardtail"),
            ("Drivetrain", "Shimano Deore 1x10 speed, 11-51T cassette"),
            ("IP Rating", "IP65 (water and dust resistant)"),
            ("Colors", "Forest Green, Slate Grey, Burnt Orange"),
            ("Dimensions (L x W x H)", "1,920 x 700 x 1,100 mm"),
            ("Connectivity", "ANT+ / Bluetooth, BestRun EV app"),
            ("Display", "Bafang DPC18 color display"),
            ("Warranty", "2 years frame, 2 years battery, 1 year drivetrain"),
        ]),
        ("Apex Pro", [
            ("Category", "Performance off-road electric bike"),
            ("Motor", "750 W mid-drive motor (BestRun EV proprietary BRD-750)"),
            ("Peak Power", "1,200 W"),
            ("Battery", "48 V / 25 Ah LFP (Lithium Iron Phosphate) - 1,200 Wh"),
            ("Battery Chemistry", "LFP (LiFePO4) - new for Apex Series"),
            ("Range - Eco Mode", "200 km"),
            ("Range - Standard Mode", "140 km"),
            ("Range - Sport Mode", "90 km"),
            ("Range - Turbo Mode", "60 km"),
            ("Top Speed", "25 km/h (EU pedelec); 45 km/h (speed pedelec variant, separate SKU)"),
            ("Charging Time (0-100%)", "3.5 hours (fast charger, 8A - included)"),
            ("Charging Time (0-80%)", "2.5 hours (fast charger, 8A)"),
            ("Charging Time (0-100%, standard)", "6.5 hours (standard 4A charger)"),
            ("Frame", "Carbon fibre composite (main triangle), 6061 aluminium (rear)"),
            ("Weight (excl. battery)", "26.5 kg"),
            ("Weight (incl. battery)", "31.0 kg"),
            ("Max Rider Weight", "140 kg"),
            ("Wheel Size", "29 inch front and rear, tubeless"),
            ("Brakes", "Magura MT5e hydraulic disc, 203 mm rotors (F&R)"),
            ("Suspension", "Fox 36 Performance front fork, 150 mm travel; Fox Float DPS rear shock, 55 mm"),
            ("Drivetrain", "Shimano XT 1x12 speed, 10-51T cassette"),
            ("IP Rating", "IP67 (submersion resistant to 1 m for 30 min)"),
            ("Colors", "Apex Blue (signature), Carbon Black, Alpine White"),
            ("Dimensions (L x W x H)", "1,980 x 760 x 1,150 mm"),
            ("Connectivity", "BLE 5.2 + ANT+, BestRun EV Pro app, OTA firmware updates"),
            ("Display", '4.2" high-brightness color TFT, 1,000 nit'),
            ("Lights", "Supernova integrated LED system (front 1,200 lm, rear brake light)"),
            ("Warranty", "3 years frame, 3 years battery, 2 years motor, 1 year electronics"),
        ]),
    ]

    for model_name, specs in models:
        pdf.h1(model_name)
        for k, v in specs:
            pdf.kv(k, v)
        pdf.ln(3)

    pdf.h1("Color Availability by Model")
    pdf.table(
        ["Color", "Apex City", "Apex Trail", "Apex Pro"],
        [
            ["Midnight Black", "Yes", "No", "No"],
            ["Pearl White", "Yes", "No", "No"],
            ["Urban Grey", "Yes", "No", "No"],
            ["Coral Red", "Yes", "No", "No"],
            ["Forest Green", "No", "Yes", "No"],
            ["Slate Grey", "No", "Yes", "No"],
            ["Burnt Orange", "No", "Yes", "No"],
            ["Apex Blue (signature)", "No", "No", "Yes"],
            ["Carbon Black", "No", "No", "Yes"],
            ["Alpine White", "No", "No", "Yes"],
        ],
        [60, 37, 37, 37],
    )

    pdf.note(
        "All range figures are measured under WLTP Urban cycle at 20 deg C with a 75 kg rider. "
        "Real-world range varies with rider weight, terrain, temperature, and assist level. "
        "The Apex Pro speed pedelec variant (45 km/h) is a separate SKU and subject to type approval per market."
    )

    pdf.output(os.path.join(OUT_DIR, "01_Apex_Series_Technical_Spec_Sheet.pdf"))
    print("Created: 01_Apex_Series_Technical_Spec_Sheet.pdf")


# ─────────────────────────────────────────────
# Document 2: Apex Pro Battery & Drive Technology Guide
# ─────────────────────────────────────────────
def doc2():
    pdf = Doc(
        "Apex Pro Battery & Drive Technology Guide",
        "Technical Reference for Authorized Dealers - Apex Series Launch",
    )

    pdf.h1("Introduction")
    pdf.body(
        "The Apex Pro introduces BestRun EV's first production use of Lithium Iron Phosphate (LFP) "
        "battery chemistry and the proprietary BRD-750 mid-drive motor system. This guide provides "
        "dealers with the technical background needed to confidently present and service the Apex Pro."
    )

    pdf.h1("1. LFP Battery Technology")
    pdf.h2("1.1 Why LFP?")
    pdf.body(
        "Previous BestRun EV models used NMC (Nickel Manganese Cobalt) chemistry. The Apex Pro "
        "switches to LFP for three reasons:"
    )
    for point in [
        "Thermal stability: LFP cells do not enter thermal runaway under the same conditions as NMC, "
        "making them safer for high-performance use and storage in warm climates.",
        "Cycle life: LFP delivers 2,000+ full charge cycles before reaching 80% capacity retention, "
        "versus 800-1,000 for typical NMC. At one charge per day, this is over 5 years of daily use.",
        "Flat discharge curve: LFP maintains a near-constant voltage (~3.2 V/cell) through 80% of "
        "its discharge, delivering more consistent power output than NMC.",
    ]:
        pdf.bullet(point)
    pdf.ln(2)

    pdf.h2("1.2 Battery Pack Specifications")
    pdf.table(
        ["Parameter", "Value"],
        [
            ["Chemistry", "LFP (LiFePO4)"],
            ["Nominal Voltage", "48 V"],
            ["Capacity", "25 Ah"],
            ["Energy", "1,200 Wh"],
            ["Cell Configuration", "16S2P (16 series, 2 parallel)"],
            ["Cell Supplier", "CATL (tier 1 EV supplier)"],
            ["Nominal Cell Voltage", "3.2 V"],
            ["Max Charge Voltage", "3.65 V/cell (58.4 V pack)"],
            ["Min Discharge Voltage", "2.8 V/cell (44.8 V pack)"],
            ["Max Continuous Discharge Current", "60 A"],
            ["Peak Discharge Current (5 s)", "120 A"],
            ["Operating Temperature", "-20 deg C to +60 deg C (discharge); 0 to +45 deg C (charge)"],
            ["Storage Temperature", "-20 deg C to +35 deg C recommended"],
            ["IP Rating", "IP67"],
            ["Weight", "4.5 kg"],
            ["Dimensions", "420 x 95 x 75 mm (integrated downtube)"],
        ],
        [85, 85],
    )

    pdf.h2("1.3 Charging System")
    pdf.body(
        "The Apex Pro ships with a dedicated 8A fast charger (BestRun EV Part No. CHR-8A-48V). "
        "The Battery Management System (BMS) handles all charge termination."
    )
    pdf.table(
        ["Charger", "Input", "Output", "0-80%", "0-100%"],
        [
            ["Fast Charger (included)", "100-240V AC, 50/60Hz", "54.4V / 8A (435W)", "~2.5 h", "~3.5 h"],
            ["Standard Charger (optional)", "100-240V AC, 50/60Hz", "54.4V / 4A (218W)", "~5.0 h", "~6.5 h"],
            ["Dual-port Fast Charger (opt.)", "100-240V AC, 50/60Hz", "54.4V / 12A (650W)", "~1.8 h", "~2.5 h"],
        ],
        [48, 45, 40, 19, 19],
    )
    pdf.note(
        "Charging below 0 deg C is not supported. The BMS will refuse to accept charge current if the "
        "battery temperature is below 0 deg C. Allow the battery to warm up indoors before charging. "
        "Charging above 45 deg C will throttle input current to protect cell longevity."
    )

    pdf.h2("1.4 Range Calculations")
    pdf.body(
        "The 200 km Eco Mode range is calculated at 6 Wh/km (WLTP Urban, flat terrain, 75 kg rider, "
        "20 deg C). The table below shows estimated range under common real-world conditions:"
    )
    pdf.table(
        ["Condition", "Wh/km", "Eco Range", "Standard Range"],
        [
            ["WLTP Urban (reference)", "6.0", "200 km", "140 km"],
            ["Mixed urban/suburban", "7.5", "160 km", "112 km"],
            ["Hilly terrain (+200m/100km)", "9.0", "133 km", "93 km"],
            ["Heavy off-road (trail)", "12.0", "100 km", "70 km"],
            ["Cold weather (0 deg C)", "8.5", "141 km", "99 km"],
            ["Heavy rider (100 kg)", "7.0", "171 km", "120 km"],
        ],
        [72, 25, 37, 37],
    )

    pdf.h1("2. BRD-750 Mid-Drive Motor")
    pdf.h2("2.1 Motor Overview")
    pdf.body(
        "The BRD-750 is BestRun EV's first proprietary mid-drive motor, developed in partnership with "
        "the BestRun EV R&D centre in Munich. Mid-drive placement (at the bottom bracket) provides "
        "superior weight distribution and allows the rider to use the bike's own gearing for optimal "
        "efficiency across all terrain."
    )
    pdf.table(
        ["Parameter", "Value"],
        [
            ["Rated Power", "750 W (EU pedelec); 1,000 W (non-EU markets)"],
            ["Peak Power (5 s)", "1,200 W"],
            ["Rated Torque", "95 Nm"],
            ["Peak Torque", "120 Nm"],
            ["Cadence Sensor", "12-magnet cadence + torque sensor (dual)"],
            ["Gear Sensor", "Integrated automatic gear shift detection"],
            ["Efficiency (peak)", "92%"],
            ["Weight", "3.2 kg"],
            ["Bottom Bracket Standard", "73 mm threaded (BSA)"],
            ["Noise Level", "<55 dB(A) at rated load"],
        ],
        [85, 85],
    )

    pdf.h2("2.2 Assist Modes")
    pdf.table(
        ["Mode", "Max Motor Contribution", "Typical Use Case"],
        [
            ["Eco", "35% of rider input", "Long-distance commuting, maximum range"],
            ["Standard", "100% of rider input", "Everyday mixed riding"],
            ["Sport", "200% of rider input", "Hills, headwinds, moderate off-road"],
            ["Turbo", "340% of rider input", "Steep climbs, full off-road performance"],
            ["Walk Assist", "6 km/h constant", "Pushing the bike up ramps or steep sections"],
        ],
        [25, 55, 90],
    )

    pdf.h1("3. Battery Management System (BMS)")
    pdf.body("The integrated BMS monitors and protects the battery at all times. Key functions:")
    for point in [
        "Cell balancing: active balancing during charge and passive balancing during storage",
        "Overtemperature protection: cuts charge/discharge above 60 deg C cell temperature",
        "Overcurrent protection: limits peak current to 120 A; trips at 130 A",
        "Deep discharge protection: locks battery above 2.8 V/cell to prevent irreversible capacity loss",
        "State of health (SoH) reporting: available via BestRun EV Pro app (requires Bluetooth connection)",
        "Firmware updatable: BMS firmware updates delivered OTA via BestRun EV Pro app",
    ]:
        pdf.bullet(point)
    pdf.ln(2)

    pdf.h1("4. Service Intervals & Dealer Obligations")
    pdf.table(
        ["Service Item", "Interval", "Dealer Action"],
        [
            ["Drive system inspection", "Every 5,000 km or 12 months", "Check motor mount torque, clean drive unit"],
            ["Battery capacity check", "Every 12 months", "Run BestRun EV Diagnostic Tool, record SoH"],
            ["BMS firmware update", "When notified via app", "Connect laptop, run BestRun EV Service Tool"],
            ["Battery replacement", "When SoH < 70%", "Order via BestRun EV Parts Portal (BAT-PRO-LFP)"],
            ["Motor replacement", "On failure or >8,000 km if abnormal noise", "BRD-750 is dealer-replaceable; requires certified training"],
            ["Charging port inspection", "Every 5,000 km", "Check for corrosion, ensure IP67 seal intact"],
        ],
        [55, 47, 68],
    )
    pdf.note(
        "The BRD-750 motor and LFP battery require BestRun EV Apex-Certified Technician training "
        "before dealer-level service. Enrol via the dealer portal at bestrun-ev.com/dealer/training."
    )

    pdf.output(os.path.join(OUT_DIR, "02_Apex_Pro_Battery_Drive_Technology_Guide.pdf"))
    print("Created: 02_Apex_Pro_Battery_Drive_Technology_Guide.pdf")


# ─────────────────────────────────────────────
# Document 3: Dealer Commercial Handbook
# ─────────────────────────────────────────────
def doc3():
    pdf = Doc(
        "Dealer Commercial Handbook",
        "Apex Series Launch Edition - Authorized Dealers Only",
    )

    pdf.h1("1. Introduction")
    pdf.body(
        "This handbook sets out the commercial terms, pricing structure, and ordering process for the "
        "BestRun EV Apex Series. It applies to all authorized BestRun EV dealers effective from the "
        "Apex Series launch date. Please keep this document accessible to your sales and ordering teams."
    )

    pdf.h1("2. Dealer Tiers")
    pdf.body(
        "BestRun EV operates a three-tier dealer network. Tier determines base margin, co-marketing "
        "budget, and minimum stock commitment."
    )
    pdf.table(
        ["Tier", "Annual Purchase Volume", "Base Margin", "Co-Mktg Budget", "Min. Stock (Apex)"],
        [
            ["Silver", "< EUR 150,000", "12%", "EUR 1,500 / year", "3 units"],
            ["Gold", "EUR 150,000 - 400,000", "15%", "EUR 4,000 / year", "8 units"],
            ["Platinum", "> EUR 400,000", "18%", "EUR 9,000 / year", "15 units"],
        ],
        [28, 48, 22, 38, 35],
    )
    pdf.note(
        "Tier is assessed annually on 1 January based on the prior calendar year's net invoice value. "
        "New dealers joining within 6 months of the Apex launch are provisionally assigned Silver tier "
        "with a 6-month review."
    )

    pdf.h1("3. Apex Series Dealer Pricing")
    pdf.h2("3.1 Recommended Retail Price (RRP)")
    pdf.table(
        ["Model", "RRP (EUR, incl. VAT)", "RRP (GBP, incl. VAT)", "RRP (SGD, incl. GST)"],
        [
            ["Apex City", "EUR 1,990", "GBP 1,699", "SGD 2,950"],
            ["Apex Trail", "EUR 3,490", "GBP 2,999", "SGD 5,150"],
            ["Apex Pro", "EUR 5,990", "GBP 5,199", "SGD 8,800"],
            ["Apex Pro (Speed Pedelec)", "EUR 6,490", "GBP 5,699", "SGD 9,550"],
        ],
        [45, 42, 42, 43],
    )

    pdf.h2("3.2 Dealer Net Price (ex-VAT, EUR, per unit)")
    pdf.table(
        ["Model", "RRP ex-VAT", "Silver Net (12%)", "Gold Net (15%)", "Platinum Net (18%)"],
        [
            ["Apex City", "EUR 1,672", "EUR 1,471", "EUR 1,421", "EUR 1,371"],
            ["Apex Trail", "EUR 2,933", "EUR 2,581", "EUR 2,493", "EUR 2,405"],
            ["Apex Pro", "EUR 5,034", "EUR 4,430", "EUR 4,279", "EUR 4,128"],
            ["Apex Pro (Speed)", "EUR 5,454", "EUR 4,800", "EUR 4,636", "EUR 4,472"],
        ],
        [35, 32, 38, 38, 29],
    )

    pdf.h1("4. Ordering Process")
    for step, title, desc in [
        ("1", "Place order via portal",
         "Log in to bestrun-ev.com/dealer and navigate to Order > New Order. "
         "Select model, variant, color, and quantity. The portal shows live inventory availability."),
        ("2", "Order confirmation",
         "Automatic email confirmation within 15 minutes. Includes order reference number, "
         "estimated delivery window, and invoice preview."),
        ("3", "Payment",
         "Standard payment terms are Net 30 from invoice date. Upfront payment attracts a 3% "
         "discount (applied at checkout). Net 60 terms available for Gold and Platinum dealers on request."),
        ("4", "Delivery",
         "Standard delivery: 5-10 business days (EU), 7-14 days (UK), 10-21 days (APAC). "
         "Express delivery available at cost for an additional EUR 45 per unit (EU only)."),
        ("5", "Receipt and inspection",
         "Inspect all units on delivery. Report damage within 48 hours via the dealer portal. "
         "Photos required for claims."),
    ]:
        pdf.h2(f"Step {step}: {title}")
        pdf.body(desc)

    pdf.h2("Minimum Order Quantities")
    pdf.table(
        ["Model", "MOQ (single order)", "Notes"],
        [
            ["Apex City", "1 unit", "No MOQ restriction"],
            ["Apex Trail", "1 unit", "No MOQ restriction"],
            ["Apex Pro", "2 units", "Initial launch period (first 6 months post-launch)"],
            ["Apex Pro Speed Pedelec", "1 unit", "Subject to market type approval"],
        ],
        [40, 35, 97],
    )

    pdf.h1("5. Co-Marketing Programme")
    pdf.body(
        "BestRun EV co-funds dealer marketing activities for the Apex Series launch. Eligible activities:"
    )
    for item in [
        "In-store Apex Series launch events (up to 50% co-funded)",
        "Social media advertising featuring Apex Series (up to 50% co-funded)",
        "Local press/print advertising (up to 30% co-funded)",
        "Test-ride day organisation - BestRun EV provides demo units for approved events",
        "BestRun EV-branded display materials (ordered via dealer portal, shipped free)",
    ]:
        pdf.bullet(item)
    pdf.ln(2)
    pdf.body(
        "To claim co-marketing funds: submit a campaign brief via the dealer portal before the activity. "
        "Post-activity, upload receipts and a short performance report. Claims processed within 30 days."
    )

    pdf.h1("6. Returns & Cancellations")
    pdf.table(
        ["Scenario", "Policy"],
        [
            ["Order cancellation before shipment", "Full refund; cancel via portal up to 24 h before dispatch"],
            ["Return: unopened, undamaged (within 30 days)", "Full refund less 5% restocking fee"],
            ["Return: opened, undamaged (within 14 days)", "80% refund; unit must be in resaleable condition"],
            ["Return: defective unit (warranty)", "Full replacement or refund; see Warranty Guide"],
            ["Apex Pro (launch period MOQ)", "No cancellation once production slot confirmed (> 7 days post-order)"],
        ],
        [75, 97],
    )

    pdf.output(os.path.join(OUT_DIR, "03_Dealer_Commercial_Handbook.pdf"))
    print("Created: 03_Dealer_Commercial_Handbook.pdf")


# ─────────────────────────────────────────────
# Document 4: Apex Pre-Order Discount Policy
# ─────────────────────────────────────────────
def doc4():
    pdf = Doc(
        "Apex Pre-Order Discount Policy",
        "Valid for Pre-Orders Placed Before Official Launch Date - Authorized Dealers Only",
    )

    pdf.h1("1. Policy Overview")
    pdf.body(
        "BestRun EV offers a structured pre-order discount programme to encourage early stock "
        "commitments ahead of the Apex Series launch. Discounts are applied to the dealer net "
        "price at checkout on the pre-order portal. This document describes all discount tiers, "
        "bonus conditions, model-specific exceptions, and stacking rules."
    )
    pdf.note(
        "Pre-order discounts are applied on top of the standard dealer tier margin. "
        "They are not available on standard (post-launch) orders."
    )

    pdf.h1("2. Base Discount Matrix")
    pdf.body(
        "The base pre-order discount is determined by two factors: (1) the total quantity of units "
        "ordered across all Apex models in a single pre-order, and (2) the selected payment terms."
    )
    pdf.table(
        ["Order Quantity", "Upfront Payment", "Net 30", "Net 60"],
        [
            ["1-4 units", "3%", "1%", "0%"],
            ["5-9 units", "7%", "5%", "3%"],
            ["10-19 units", "10%", "8%", "5%"],
            ["20-49 units", "14%", "11%", "8%"],
            ["50+ units", "18%", "15%", "10%"],
        ],
        [50, 45, 38, 38],
    )
    pdf.body(
        "Example: A dealer ordering 12 units (any mix of Apex City, Trail, and Pro) with Net 30 "
        "payment terms receives an 8% pre-order discount on the dealer net price of all units in "
        "that order."
    )

    pdf.h1("3. Additional Bonus Conditions")

    pdf.h2("3.1 Early Bird Bonus (+2%)")
    pdf.body(
        "An additional 2% discount applies to any pre-order submitted at least 60 days before "
        "the official Apex Series launch date."
    )
    for point in [
        "The launch date is communicated via the dealer portal and your regional account manager.",
        "Eligibility is calculated from the pre-order submission timestamp (portal server time, CET).",
        "The early bird bonus applies to the entire order, not individual line items.",
    ]:
        pdf.bullet(point)
    pdf.ln(2)

    pdf.h2("3.2 First Pre-Order Bonus (+1%)")
    pdf.body(
        "An additional 1% discount applies to dealers placing their first-ever pre-order with "
        "BestRun EV. This bonus is a one-time entitlement per dealer account."
    )
    for point in [
        "Eligibility is determined automatically by the pre-order system based on dealer account history.",
        "Dealers who previously placed a pre-order for any BestRun EV product are not eligible.",
        "The first pre-order bonus applies to the entire order.",
    ]:
        pdf.bullet(point)
    pdf.ln(2)

    pdf.h1("4. Model-Specific Exceptions")

    pdf.h2("4.1 Apex Pro - Discount Cap (10%)")
    pdf.body(
        "Due to constrained initial production allocation, the total pre-order discount applicable "
        "to Apex Pro units is capped at 10%, regardless of order quantity, payment terms, or "
        "bonus eligibility."
    )
    pdf.table(
        ["Scenario", "Calculated Discount", "Applied (Apex Pro)"],
        [
            ["20 units, upfront, no bonuses", "14%", "10% (capped)"],
            ["12 units, upfront, early bird", "10% + 2% = 12%", "10% (capped)"],
            ["50 units, upfront, early bird + first order", "18% + 2% + 1% = 21%", "10% (capped)"],
            ["10 units, net 30, no bonuses", "8%", "8% (under cap - no adjustment)"],
        ],
        [84, 45, 42],
    )
    pdf.note(
        "The Apex Pro cap applies per unit of Apex Pro ordered. If a pre-order contains both "
        "Apex Trail and Apex Pro units, the Apex Trail units receive the full calculated discount; "
        "only Apex Pro units are subject to the 10% cap."
    )

    pdf.h1("5. Stacking Rules")
    for rule in [
        "The base matrix discount, early bird bonus (+2%), and first pre-order bonus (+1%) stack additively.",
        "The Apex Pro cap (10%) is applied after all stacking - it is a ceiling, not a starting point.",
        "Pre-order discounts stack on top of the dealer tier margin (Silver/Gold/Platinum). They do not replace it.",
        "No other promotional discounts apply during the pre-order window. Pre-order discounts cannot be "
        "combined with any other active BestRun EV promotional offer.",
    ]:
        pdf.bullet(rule)
    pdf.ln(2)

    pdf.h1("6. Worked Examples")

    pdf.h2("Example A - Apex Trail, 12 units, upfront, early bird")
    pdf.body("Dealer: Gold tier. Order: 12 Apex Trail, upfront payment. Order date: 75 days before launch.")
    pdf.table(
        ["Component", "Value"],
        [
            ["Base discount (10-19 units, upfront)", "10%"],
            ["Early bird bonus (75 days > 60 days)", "+2%"],
            ["First pre-order bonus", "Not applicable (existing dealer)"],
            ["Total pre-order discount", "12%"],
            ["Apex Pro cap", "N/A (no Apex Pro in order)"],
            ["Final discount applied", "12% on all 12 Apex Trail units"],
        ],
        [95, 77],
    )

    pdf.h2("Example B - Apex Pro, 5 units, upfront, first order")
    pdf.body("Dealer: Silver tier. Order: 5 Apex Pro, upfront payment. Order date: 30 days before launch (first pre-order).")
    pdf.table(
        ["Component", "Value"],
        [
            ["Base discount (5-9 units, upfront)", "7%"],
            ["Early bird bonus (30 days < 60 days)", "Not applicable"],
            ["First pre-order bonus", "+1%"],
            ["Stacked total before cap", "8%"],
            ["Apex Pro cap check (8% < 10%)", "Under cap - no adjustment"],
            ["Final discount applied", "8% on all 5 Apex Pro units"],
        ],
        [95, 77],
    )

    pdf.h2("Example C - Mixed order, Apex Pro + Apex Trail, 30 units")
    pdf.body("Dealer: Platinum tier. Order: 20 Apex Pro + 10 Apex Trail, upfront payment. 65 days before launch (first pre-order).")
    pdf.table(
        ["Component", "Value"],
        [
            ["Base discount (30 units total, upfront)", "14%"],
            ["Early bird bonus (65 days > 60 days)", "+2%"],
            ["First pre-order bonus", "+1%"],
            ["Stacked total before cap", "17%"],
            ["Applied to Apex Trail (10 units)", "17% - no cap"],
            ["Applied to Apex Pro (20 units)", "10% - capped at 10%"],
        ],
        [95, 77],
    )

    pdf.h1("7. Pre-Order Validity & Confirmation")
    pdf.body(
        "A pre-order is considered binding once the dealer receives an email confirmation with a "
        "pre-order reference number. The discount rate is locked at the time of submission and "
        "cannot be changed after confirmation. If a pre-order is cancelled and re-submitted, "
        "the new submission date applies for early bird eligibility."
    )

    pdf.output(os.path.join(OUT_DIR, "04_Apex_Pre-Order_Discount_Policy.pdf"))
    print("Created: 04_Apex_Pre-Order_Discount_Policy.pdf")


# ─────────────────────────────────────────────
# Document 5: After-Sales & Warranty Guide
# ─────────────────────────────────────────────
def doc5():
    pdf = Doc(
        "After-Sales & Warranty Guide",
        "Apex Series - Authorized Dealer Reference",
    )

    pdf.h1("1. Warranty Terms by Model")
    pdf.table(
        ["Component", "Apex City", "Apex Trail", "Apex Pro"],
        [
            ["Frame & fork", "2 years", "2 years", "3 years"],
            ["Battery pack", "1 yr / 300 cycles", "2 yr / 500 cycles", "3 yr / 1,000 cycles"],
            ["Motor", "1 year", "1 year", "2 years"],
            ["Electronics & display", "1 year", "1 year", "1 year"],
            ["Drivetrain (chain, cassette)", "Not covered", "6 months", "1 year"],
            ["Suspension (fork/shock)", "Not covered", "1 yr (seals)", "2 yr (seals + internals)"],
            ["Brakes (pads, rotors)", "Not covered", "Not covered", "Not covered"],
            ["Tires & tubes", "Not covered", "Not covered", "Not covered"],
        ],
        [58, 30, 30, 30],
    )
    pdf.note(
        "Battery warranty is the shorter of the time period or cycle count. "
        "Warranty is valid from the date of original retail purchase (end customer). "
        "Dealer stock held unsold is covered from the dealer invoice date."
    )

    pdf.h1("2. Warranty Conditions")
    pdf.h2("2.1 What the warranty covers")
    for item in [
        "Manufacturing defects in materials and workmanship",
        "Battery capacity falling below 70% of rated capacity within the warranty period "
        "(verified by BestRun EV Diagnostic Tool)",
        "Motor failure not caused by impact, submersion beyond IP rating, or unauthorised modification",
        "Electronic faults not caused by water ingress beyond IP rating, incorrect charging, or physical damage",
    ]:
        pdf.bullet(item)
    pdf.ln(2)

    pdf.h2("2.2 What the warranty does NOT cover")
    for item in [
        "Normal wear items: brake pads, tires, tubes, chains, cables, grips, saddles",
        "Damage from accidents, impacts, or rider error",
        "Damage from use outside the stated IP rating",
        "Battery degradation from improper storage (e.g., stored fully discharged for >3 months)",
        "Modifications or repairs carried out by non-authorised technicians",
        "Cosmetic damage (scratches, paint chips) not affecting function",
        "Products with a removed or tampered serial number",
    ]:
        pdf.bullet(item)
    pdf.ln(2)

    pdf.h1("3. Warranty Claims Process")
    for step, title, desc in [
        ("1", "Dealer assessment",
         "Inspect the unit and reproduce the fault. Log the fault via the dealer portal "
         "(Service > New Warranty Claim). Include: serial number, purchase date, fault description, and photos."),
        ("2", "BestRun EV approval",
         "BestRun EV Warranty Team reviews and responds within 2 business days. "
         "Approval is required before any work begins. Unauthorized work will not be reimbursed."),
        ("3", "Repair or replacement",
         "On approval: carry out the authorised repair using BestRun EV genuine parts. "
         "For total replacement, BestRun EV ships a replacement unit and arranges collection of the faulty unit."),
        ("4", "Labour reimbursement",
         "Approved warranty labour is reimbursed at the current BestRun EV Warranty Labour Rate "
         "(EUR 75/hour Gold and Platinum dealers; EUR 65/hour Silver). Submit labour record via portal."),
        ("5", "Parts",
         "Warranty replacement parts are shipped free of charge to the dealer. Non-warranty parts "
         "are ordered via the Parts Portal and invoiced at dealer price."),
    ]:
        pdf.h2(f"Step {step}: {title}")
        pdf.body(desc)

    pdf.h1("4. Common Issues & Troubleshooting")
    pdf.h2("Apex City")
    pdf.table(
        ["Symptom", "Likely Cause", "Action"],
        [
            ["Motor cuts out at low speed", "Throttle calibration drift", "Recalibrate via BestRun EV app > Settings > Throttle Reset"],
            ["Battery drains faster than expected", "Cold weather or cell aging", "Check SoH in app; if SoH <80%, raise warranty claim"],
            ["Display shows error E03", "BMS over-temperature", "Allow battery to cool 20 min; charge in cooler environment"],
            ["Rear brake rubbing", "Pad wear or rotor alignment", "Adjust or replace pads; not a warranty item"],
        ],
        [45, 42, 85],
    )

    pdf.h2("Apex Trail")
    pdf.table(
        ["Symptom", "Likely Cause", "Action"],
        [
            ["Drivetrain noise under load", "Chain wear or derailleur adjustment", "Check chain wear indicator; adjust derailleur limit screws"],
            ["Motor assistance stutters at cadence", "Cadence sensor magnet alignment", "Inspect magnet on crank arm; re-align if >3 mm from sensor"],
            ["Fork feels harsh on small bumps", "Low air pressure in fork", "Check and adjust fork pressure per RockShox chart for rider weight"],
            ["Display shows error E07", "Speed sensor fault", "Check sensor cable connector at motor; re-seat if loose"],
        ],
        [48, 48, 76],
    )

    pdf.h2("Apex Pro")
    pdf.table(
        ["Symptom", "Likely Cause", "Action"],
        [
            ["Range significantly below expected", "Cold weather, heavy terrain, or SoH decline", "Check SoH via Pro app; if SoH <80% within warranty, raise claim"],
            ["Motor noise (grinding at high torque)", "BRD-750 bearing wear", "Do not continue riding; raise warranty claim - motor replacement required"],
            ["Charging stops at <80%", "BMS high-temperature protection", "Charge in ambient <30 deg C; check for fan obstruction near motor"],
            ["App shows 'BMS Update Required'", "BMS firmware update pending", "Connect to BestRun EV Pro app on Wi-Fi; run update (approx. 8 min)"],
            ["Display error E12", "LFP cell imbalance detected", "Run full charge cycle to allow active balancing; if persists, raise claim"],
        ],
        [50, 50, 72],
    )

    pdf.h1("5. Service Schedule")
    pdf.table(
        ["Service", "Apex City", "Apex Trail", "Apex Pro"],
        [
            ["Basic service (brakes, tyres, bolts)", "1,000 km / 12 mo", "1,500 km / 12 mo", "2,000 km / 12 mo"],
            ["Full service (drivetrain, suspension)", "Not applicable", "3,000 km / 24 mo", "3,000 km / 24 mo"],
            ["Battery capacity check", "Every 12 mo", "Every 12 mo", "Every 12 mo"],
            ["Motor inspection", "2,000 km / 12 mo", "3,000 km / 12 mo", "5,000 km / 12 mo"],
            ["BMS firmware check", "Via app, as notified", "Via app, as notified", "Via app, as notified"],
            ["Fork service (seal replacement)", "Not applicable", "100 h use or 24 mo", "100 h use or 12 mo"],
        ],
        [57, 33, 33, 33],
    )

    pdf.h1("6. Spare Parts Ordering")
    pdf.body(
        "Genuine BestRun EV parts are ordered via the dealer portal at bestrun-ev.com/dealer/parts. "
        "Key parts for Apex Series:"
    )
    pdf.table(
        ["Part", "Part Number", "Models", "Lead Time"],
        [
            ["LFP Battery Pack (48V/25Ah)", "BAT-PRO-LFP", "Apex Pro", "5-7 business days"],
            ["NMC Battery Pack (48V/17.5Ah)", "BAT-TRL-NMC", "Apex Trail", "5-7 business days"],
            ["NMC Battery Pack (36V/14.5Ah)", "BAT-CTY-NMC", "Apex City", "5-7 business days"],
            ["BRD-750 Motor Unit", "MOT-BRD750", "Apex Pro", "7-10 business days"],
            ["Bafang M400 Motor Unit", "MOT-BAF400", "Apex Trail", "5-7 business days"],
            ["Apex Pro Fast Charger (8A)", "CHR-8A-48V", "Apex Pro", "3-5 business days"],
            ["Apex Trail/City Charger (4A)", "CHR-4A-48V", "Apex Trail, City", "3-5 business days"],
            ["Apex Pro Display (4.2\")", "DSP-PRO-42", "Apex Pro", "5-7 business days"],
            ["Apex Pro Brake Set (Magura MT5e)", "BRK-MT5E-203", "Apex Pro", "3-5 business days"],
            ["Apex Trail Brake Set (Shimano)", "BRK-SHM-180", "Apex Trail", "3-5 business days"],
        ],
        [60, 34, 34, 44],
    )

    pdf.output(os.path.join(OUT_DIR, "05_After-Sales_Warranty_Guide.pdf"))
    print("Created: 05_After-Sales_Warranty_Guide.pdf")


if __name__ == "__main__":
    doc1()
    doc2()
    doc3()
    doc4()
    doc5()
    print("\nAll 5 documents generated successfully.")
