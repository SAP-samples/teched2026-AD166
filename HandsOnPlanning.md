# AD166 - Hands-On Planning: SAP Build Work Zone Advanced + AI
## SAP TechEd 2026

---

## Reference: How AD165 Was Structured

AD165 ("Build It Yourself: Your Modern Digital Workplace") served as a useful baseline. Its pattern:

| Element | Detail |
|---|---|
| **Business scenario** | Build an "AI Center of Excellence" internal workspace |
| **Session length** | ~2 hours |
| **Exercise count** | 4 main + 1 optional |
| **AI coverage** | Light — AI feed post generation and text summarization in ex4 only |
| **End-user moment** | Single exercise at the end where participants "become" the end user |
| **Structure** | ex0 (optional intro) → ex1 (workspace setup) → ex2 (UI card) → ex3 (guided experience) → ex4 (end user AI) → ex5 (optional mobile) |

**Key deltas for AD166:**
- AD165 saved AI features for the very end; AD166 weaves AI throughout every exercise
- Joule was not used in AD165; it is the headline feature for AD166
- Document Grounding was not present in AD165; it gets a dedicated exercise
- AD165 was internal-facing; AD166 is **external-facing (B2B dealer portal)** — a meaningful upgrade in complexity and realism
- AD166 has **5 main exercises + 1 optional**, with guided experience and mobile both in the main flow

---

## Chosen Business Scenario: B2B Dealer Portal — BestRun EV

### The Company

**BestRun EV** is a premium electric mobility brand that designs and manufactures high-performance ebikes and electric scooters. They sell exclusively through an authorized dealer network of 200+ dealers across Europe and Asia-Pacific.

Their current dealer portal is a static website: a grid of downloadable PDF spec sheets, a quarterly price list sent by email, and a contact form. Dealers submit product questions by email and wait 24–48 hours for a response from their regional sales rep. Nobody is happy with this.

### The Trigger

BestRun EV is launching the **Apex Series** — their most significant product line in five years — in 90 days. Three new models:

| Model | Category | Positioning |
|---|---|---|
| **Apex City** | Urban commuter scooter | Entry-level, city-optimized, lightweight |
| **Apex Trail** | Adventure ebike | Mid-range, 140km range, all-terrain |
| **Apex Pro** | Performance off-road ebike | Flagship, new LFP battery, 200km range |

The dealer network needs to be trained on the new models immediately. With the Apex Pro featuring an entirely new battery and drive system, there are hundreds of technical and commercial questions dealers will ask before they can confidently sell. BestRun EV's digital team decides: **don't update the static portal again — migrate to SAP Build Work Zone and launch Apex on the new platform.**

### The Transformation Story

```
BEFORE                              AFTER
──────────────────────────────────  ────────────────────────────────────
Static website with PDF downloads   Dynamic SAP Build Work Zone portal
Quarterly email with price list     Live workspace with always-current docs
"Email us" for dealer questions     Joule answers questions instantly
Dealers download 40-page manuals    AI summarizes what dealers need in seconds
Generic product text on web pages   AI-assisted, carefully worded dealer comms
Order via email / phone             Structured pre-order via Guided Experience
Portal only on desktop              Accessible from Joule Work Mobile anywhere
```

### Why This Works for a Developer Audience

- Developers have built static dealer pages — they immediately recognize the "before" state
- Document Grounding is concrete: "What is the range of the Apex Pro in eco mode?" answered in seconds vs. digging through a PDF
- The "careful wording" requirement for external B2B content makes AI text generation feel like a quality gate, not just a convenience
- Joule workspace capabilities map directly to real admin tasks a portal owner performs
- The pre-order Guided Experience shows how a structured transactional workflow lives inside a workspace
- Joule Work Mobile demonstrates that the dealer portal isn't tied to a desktop browser

---

## Participant Personas

The hands-on has two persona moments — participants switch partway through:

**Persona 1 — Portal Admin at BestRun EV (exercises 1–4)**
You are a Digital Experience Manager at BestRun EV. You set up the new dealer portal on SAP Build Work Zone, build the Apex Series launch content, configure Document Grounding, and assemble the pre-order Guided Experience using pre-built UI cards.

**Persona 2 — Authorized Dealer (exercises 5–6)**
You are the owner of an authorized BestRun EV dealership in Amsterdam. You just received your portal invitation. You explore the workspace, ask product questions via Joule, use AI to summarize technical documents, submit a pre-order through the Guided Experience, and access the portal from your phone on Joule Work Mobile.

---

## Documents for Document Grounding (to be created as sample content)

| Document | Content | Why dealers need it |
|---|---|---|
| **Apex Series Technical Spec Sheet** | Dimensions, weight, motor specs, range figures, charging times, color options per model | First thing dealers ask about |
| **Apex Pro Battery & Drive Technology Guide** | LFP battery chemistry, range calculations, charging curve, battery management system, service intervals | New technology — no one knows it yet |
| **Dealer Commercial Handbook** | Pricing tiers, dealer margins, ordering process, minimum stock requirements, co-marketing budget | Commercial questions dominate early launch |
| **Apex Pre-Order Discount Policy** | Discount matrix by quantity tier × payment terms, early bird bonus, first-order bonus, model-specific conditions, stacking rules | Complex to memorise — ideal for Joule Q&A during the pre-order wizard |
| **After-Sales & Warranty Guide** | Warranty terms by model, common issues, service intervals, spare parts ordering | Critical for dealer confidence |
| **Apex Launch FAQ** | 30 most anticipated dealer questions with answers | Curated self-service document |

### Pre-Order Discount Policy: Document Structure

This document is intentionally complex — its structure is what makes Document Grounding feel essential rather than optional. A dealer cannot memorise it; Joule makes it instantly accessible mid-task.

**Discount matrix (quantity × payment terms):**

| Order Quantity | Upfront Payment | Net 30 | Net 60 |
|---|---|---|---|
| 1–4 units | 3% | 1% | 0% |
| 5–9 units | 7% | 5% | 3% |
| 10–19 units | 10% | 8% | 5% |
| 20–49 units | 14% | 11% | 8% |
| 50+ units | 18% | 15% | 10% |

**Additional conditions:**
- **Early bird bonus:** +2% if pre-order is submitted ≥ 60 days before official launch date
- **First pre-order bonus:** +1% for dealers placing their first-ever pre-order with BestRun EV
- **Apex Pro exception:** Discount capped at 10% for Apex Pro across all tiers due to constrained initial production allocation
- **Stacking rule:** Early bird and first-order bonuses stack with the base matrix discount; Apex Pro cap applies after stacking

**Sample Joule interactions this enables:**

> *Dealer:* "What discount do I get if I order 12 Apex Trail units with net 30 payment?"
> *Joule:* "For 10–19 units with Net 30 payment terms, your base pre-order discount is 8%. If you are submitting your order at least 60 days before the Apex Series launch, you qualify for an additional 2% early bird bonus — bringing your total discount to 10%."

> *Dealer:* "Can I get a higher discount on the Apex Pro if I order 25 units upfront?"
> *Joule:* "The Apex Pro pre-order discount is capped at 10% regardless of order quantity or payment terms, due to the limited initial production run. For 20–49 units with upfront payment on other models, the standard discount would be 14%."

> *Dealer:* "Does the first-order bonus apply to me?"
> *Joule:* "The first pre-order bonus of 1% applies to dealers placing their first-ever pre-order with BestRun EV. If this is your first pre-order, you can combine this with your base discount and any applicable early bird bonus."

---

## Pre-Order Guided Experience: UI Card Design

The Guided Experience is a 4-step pre-order wizard built from pre-built UI cards. The cards are authored in advance and already available in the WZ Card Catalog — participants do not build them, they assemble the guided experience from them.

| Step | Card Name | What the dealer does |
|---|---|---|
| **Step 1** | Apex Model Selection | Choose which model(s) to pre-order (Apex City / Trail / Pro) with product images and key specs |
| **Step 2** | Configuration & Quantity | Select quantity, color variant, and preferred delivery window |
| **Step 3** | Pricing & Discount Review | View dealer base pricing, see the discount calculated from the entered quantity and selected payment terms, choose payment terms — a **"Ask Joule"** prompt is surfaced here ("Not sure about your discount? Ask Joule →") |
| **Step 4** | Pre-Order Confirmation | Review full order summary including final discounted price and submit — generates a reference number |

> **The Joule integration moment:** Step 3 is where the discount complexity surfaces. The dealer sees the discount matrix is multi-dimensional and opens Joule alongside the wizard to ask their specific question. This demonstrates Document Grounding as an **inline task assistant**, not a separate feature — Joule helps the dealer complete the wizard, not distract from it.

---

## AI Feature Coverage Map

| AI Feature | Exercise | How it's used |
|---|---|---|
| **Joule — create workspace** | ex1 | Admin creates the BestRun EV Dealer Portal workspace via Joule |
| **Joule — add members** | ex1 | Admin adds regional sales managers as workspace members |
| **AI text generation** | ex2 | Admin drafts the Apex Series launch announcement and model overview pages |
| **Document Grounding** | ex3 | Admin uploads Apex docs and enables grounding for the workspace |
| **Joule Q&A (grounded)** | ex5 | Dealer asks: "What is the range of the Apex Pro in eco mode?" — sourced answer |
| **AI summary** | ex5 | Dealer summarizes the Battery Technology Guide before a customer demo |
| **Joule as inline task assistant** | ex5 | Dealer asks about pre-order discount *mid-wizard* during the Guided Experience — Joule answers from the Discount Policy document without the dealer leaving the wizard |
| **Joule — find workspace** | ex5 + ex6 | Dealer locates the portal via Joule (desktop and mobile) |

---

## Proposed Workshop Flow

**Total session time: ~2 hours**

```
ex0  Getting Started (15 min — optional pre-reading)
      ├─ What is SAP Build Work Zone, advanced edition?
      ├─ What is an external workspace / dealer portal?
      └─ Meet BestRun EV and the Apex Series (scenario briefing)

ex1  Set up the Dealer Portal with Joule (25 min)          [Admin persona]
      ├─ 1.1  Open Joule and navigate to SAP Build Work Zone
      ├─ 1.2  Use Joule to create the "BestRun EV Dealer Portal" workspace
      │        (natural language: "Create a workspace for my dealer network")
      ├─ 1.3  Use Joule to add regional sales managers as members
      └─ 1.4  Configure the workspace as external-facing (portal settings)

ex2  Build the Apex Launch Content with AI (20 min)        [Admin persona]
      ├─ 2.1  Create the Apex Series landing page in the workspace
      ├─ 2.2  Use AI text generation to draft the launch announcement
      │        (prompt: "Write a professional dealer announcement for our new Apex Series launch")
      ├─ 2.3  Create model overview sections (Apex City / Trail / Pro)
      └─ 2.4  Use AI text generation for model overview copy
               (external-facing, commercial tone, consistent across models)

ex3  Enable Document Grounding (20 min)                    [Admin persona]
      ├─ 3.1  Upload the Apex Series source documents to the workspace
      ├─ 3.2  Enable and configure Document Grounding
      ├─ 3.3  Test grounding as admin — ask Joule a technical question
      └─ 3.4  Verify answers are sourced from the uploaded documents

ex4  Add the Pre-Order Guided Experience (20 min)          [Admin persona]
      ├─ 4.1  Open the WZ Card Catalog and locate the pre-built Apex Pre-Order cards
      ├─ 4.2  Create a new "Order Now" page in the workspace
      ├─ 4.3  Add the 4 pre-order cards to the page:
      │        Step 1 — Model Selection
      │        Step 2 — Configuration & Quantity
      │        Step 3 — Pricing & Terms Review
      │        Step 4 — Pre-Order Confirmation
      └─ 4.4  Configure the Guided Experience flow and publish the page

ex5  Experience the Portal as a Dealer (25 min)            [Dealer persona]
      ├─ 5.1  [Persona switch] Accept portal invitation as Amsterdam dealer
      ├─ 5.2  Explore the Apex Series launch pages
      ├─ 5.3  Ask Joule: "What is the maximum range of the Apex Pro in eco mode?"
      │        → grounded answer with source reference from Technical Spec Sheet
      ├─ 5.4  Use AI summary on the Battery & Drive Technology Guide
      │        → 5-bullet summary before a customer demo
      ├─ 5.5  Open the "Order Now" page and start the pre-order Guided Experience
      ├─ 5.6  Complete Step 1 (model: Apex Pro) and Step 2 (quantity: 12 units)
      ├─ 5.7  On Step 3 (Pricing & Discount Review), open Joule alongside the wizard:
      │        Ask: "What discount do I get for 12 Apex Pro units with upfront payment?"
      │        → Joule answers from Pre-Order Discount Policy (10% cap for Apex Pro,
      │           plus early bird bonus if applicable)
      │        → Dealer adjusts payment terms based on the answer, sees discount update
      └─ 5.8  Complete Step 4 and submit pre-order — note the reference number

ex6  Access from Joule Work Mobile (15 min)                [Dealer persona, optional]
      ├─ 6.1  Download / open Joule Work Mobile on your smartphone
      │        (formerly SAP Mobile Start — new app name for SAP TechEd 2026)
      ├─ 6.2  Sign in and locate the BestRun EV Dealer Portal workspace
      ├─ 6.3  Browse the Apex Series pages on mobile
      └─ 6.4  Ask Joule a product question from the mobile interface
```

---

## Timing Summary

| Exercise | Persona | Duration |
|---|---|---|
| ex0 Getting Started | — | 15 min (optional) |
| ex1 Set up portal with Joule | Admin | 25 min |
| ex2 Build Apex content with AI | Admin | 20 min |
| ex3 Enable Document Grounding | Admin | 20 min |
| ex4 Add Pre-Order Guided Experience | Admin | 20 min |
| ex5 Experience portal as dealer | Dealer | 25 min |
| ex6 Joule Work Mobile | Dealer | 15 min (optional) |
| **Total (ex1–ex5)** | | **~110 min** |
| **Total (ex1–ex6)** | | **~125 min** |

> Both ex6 and ex0 are optional — the core session (ex1–ex5) fits comfortably within 2 hours.

---

## Visual Design Direction

The workspace should look like a premium product portal — not a generic demo:

- **Workspace header:** Full-width hero image of the Apex Pro against an outdoor/urban backdrop
- **Model pages:** Product photography per model (Apex City = city street, Apex Trail = forest path, Apex Pro = mountain terrain)
- **Color palette:** BestRun EV brand colors — electric blue accent (#0066FF or similar), dark backgrounds for premium feel
- **Widget layout:** Large image tiles for each model, not text-heavy lists
- **Guided Experience page:** Clean step-indicator UI, product images prominent in each card

Image sources: Royalty-free electric bike/scooter images from Unsplash or Pexels, or AI-generated product images that match a consistent brand look. Sample images should be stored in the repo under `/exercises/images/bestrun-ev/`.

---

## Sample Content to Prepare

Before writing detailed exercise steps, these artifacts need to be created:

- [ ] BestRun EV brand assets: logo concept, brand colors, hero images per Apex model
- [ ] 5 source documents for Document Grounding (see table above, ~1–2 pages each, realistic but fictional data)
- [ ] 4 pre-built UI cards for the Apex Pre-Order Guided Experience (to be loaded into WZ Card Catalog)
- [ ] Sample Joule prompts and expected grounded outputs for ex5
- [ ] Screenshot sequence: static portal "before" state (for ex0 context-setting)
- [ ] Workspace screenshots for each exercise step (taken from the live landscape after setup)

---

## Next Steps

1. **Confirm scenario** — BestRun EV / Apex Series / 5+1 exercise structure
2. **Author the 5 source documents** — realistic Apex Series specs, pricing, FAQ
3. **Design and build the 4 pre-order UI cards** — to be pre-loaded in the WZ Card Catalog
4. **Set up the landscape** — SAP Build Work Zone tenant with Joule, Document Grounding, and Joule Work Mobile enabled
5. **Prepare visual assets** — hero images, product images, workspace styling
6. **Write detailed exercise steps** starting with ex1, capture screenshots per sub-step
7. **Write the main README.md** for the repo
