# AD166 - Hands-On Planning: SAP Build Work Zone Advanced + AI
## SAP TechEd 2026

> **Canonical flow:** `planning/overall-hands-on-flow.png`. Structure: Main README → ex0 → ex1 → ex2 → ex3 → ex4 (optional, Guided Experience) → ex5 (optional, Mobile). **Note:** the diagram labels Guided Experience as "Exercise 5" and Mobile as "Exercise 6"; per the latest decision these are renumbered to **ex4** and **ex5** respectively (no gap).

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

The hands-on has two persona moments — participants briefly switch into dealer mode at the end of ex2, ex3, and ex4 (and fully in ex5):

**Persona 1 — Portal Admin at BestRun EV (exercises 0–3, ex4 setup steps)**
You are a Digital Experience Manager at BestRun EV. You set up the dealer portal on SAP Build Work Zone, build the generic portal content, add the Apex Series product launch page, and assemble the Guided Experience wizard.

**Persona 2 — Authorized Dealer (embedded in ex2 step 4, ex3 step 4, ex4 step 4, and all of ex5)**
You are the owner of an authorized BestRun EV dealership. At the end of each exercise, you switch to your `Dealer-XXX` alias user to experience the feature you just built — the portal overview, the product launch page with a Joule query, the Guided Experience wizard, and mobile access.

---

## Source Documents (sample content)

> **Where these are used in the current flow:**
> - **ex3** is where the Apex-specific documents land in the dealer portal — **copied** from the "Dealer Management" workspace's **Apex Launch Material** folder (not downloaded/uploaded), then indexed by Document Grounding for the ex3.4 Joule query.
> - The source set lives in `exercises/ex3/content/` (6 PDFs + 3 bike images + `Apex-Series-Launch-Brochure.pptx`). These are pre-loaded into the Dealer Management workspace's Apex Launch Material folder for participants to copy.
> - **ex2.4** no longer includes a document summary (per the latest decision — the dealer just accepts the invite and views the Overview page).

| Document | Content | Where used |
|---|---|---|
| **Apex Series Technical Spec Sheet** | Dimensions, weight, motor specs, range figures, charging times, color options per model | ex3 (copied content, grounding) |
| **Apex Pro Battery & Drive Technology Guide** | LFP battery chemistry, range calculations, charging curve, battery management system, service intervals | ex3 (copied content, grounding) |
| **Dealer Commercial Handbook** | Pricing tiers, dealer margins, ordering process, minimum stock requirements, co-marketing budget | ex3 (copied content, grounding) |
| **Apex Pre-Order Discount Policy** | Discount matrix by quantity tier × payment terms, early bird bonus, first-order bonus, model-specific conditions, stacking rules | ex4 (optional guided experience) — if a mid-wizard Joule query is included |
| **After-Sales & Warranty Guide** | Warranty terms by model, common issues, service intervals, spare parts ordering | ex3 (copied content, grounding) |
| **Apex Pre-Order Terms & Conditions** | Pre-order eligibility, cancellation rights, delivery commitments | ex4 (optional) |

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

## Guided Experience: UI Card Design (optional ex4)

> **Flow note:** The Guided Experience is **optional ex4** (`Guided Exp Creation`), built on the product launch page from ex3. The admin edits the page, adds a wizard section, adds steps, and assigns a pre-built card to each step (ex4.1–4.3), then experiences it as a dealer (ex4.4). **The cards are not built yet** — ex4 is currently a placeholder. The earlier "mid-wizard Ask Joule about discount" interaction is not confirmed in scope; revisit when the cards are designed.

The wizard is assembled from pre-built UI cards already available in the WZ Card Catalog — participants do not build the cards, they assemble the wizard from them.

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
| **Joule — list managed workspaces** | ex1 | Admin asks Joule "show my managed workspaces" to orient themselves |
| **Joule — create workspace** | ex1 | Admin creates the BestRun EV Dealer Portal workspace via Joule |
| **Embedded widget AI — Generate Text** | ex2 | Admin generates the hero tagline and Key Highlights copy using the widget's built-in ✨ AI button (not the Joule panel) |
| **Embedded widget AI — Change Tone / Adjust Length** | ex2 | Admin refines existing widget text in place |
| **Document Grounding** | ex3 | Launch documents are copied into the workspace; Joule queries them |
| **Joule Q&A (grounded)** | ex3 | Dealer asks Joule about the new product in the context of the workspace |
| **Joule as inline task assistant** | ex4 | Dealer asks about order details mid-wizard using Joule (if included) |
| **Joule — find workspace on mobile** | ex5 | Dealer locates the portal via Joule Work Mobile |

---

## Proposed Workshop Flow

> **Updated flow — see `planning/overall-hands-on-flow.png` for the visual diagram.**
> Key changes from the previous plan: ex2 is now generic dealer portal content (not Apex-specific); ex3 adds the product launch content to the **Overview page** (no new page) by **copying** a ready-made content set from the shared "Dealer Management" workspace (no download/upload); the standalone pre-order exercise is dropped; Guided Experience becomes optional **ex4** (placeholder for now, added to the Overview page); Mobile becomes optional **ex5**; the dealer experience moments are embedded as the final step within ex2, ex3, and ex4.

**Total session time: ~2 hours**

```
README  Introduction (pre-reading)
         ├─ Introduction to SAP Build Work Zone & AI Capabilities
         ├─ High-level overview of the hands-on with exercise links
         ├─ Visual flow of what the user will achieve in each exercise
         └─ Summary & Learning objectives

ex0  Detailed Overview of Scenario (~15 min)
      ├─ 0.1  Learn about the company, business scenario, and persona
      ├─ 0.2  Launch Work Zone and see what's where
      ├─ 0.3  Access the existing "Dealer Management" workspace
      └─ 0.4  Explore the workspace and view tasks

ex1  External Dealer Workspace Creation (~20 min)           [Admin persona]
      ├─ 1.1  Access Work Zone and launch Joule — ask for "My managed workspaces"
      ├─ 1.2  Create Dealer Portal workspace from template using a Joule prompt
      ├─ 1.3  Make the workspace private & external
      └─ 1.4  Add the dealer user to the workspace

ex2  External Dealer Workspace Content Update (~20 min)     [Admin then Dealer]
      ├─ 2.1  Update the hero section with a generic dealer portal tagline
      ├─ 2.2  Update the Key Highlights section with generic dealer portal content
      ├─ 2.3  Add a cards section with 3 cards side by side: My Orders, My Invoices, My Tickets
      └─ 2.4  Experience the workspace: document summary & comment

ex3  New Apex Launch Material Creation (~20 min)          [Admin then Dealer]
      ├─ 3.1  Copy launch content from the "Dealer Management" workspace
      │        (Apex Launch Material folder → your workspace; multi-select copy)
      ├─ 3.2  Add a section with a Text block (announcement HTML) & the PPT (multimedia card)
      ├─ 3.3  Add 3 product images to the hero carousel — each with a title and subtitle
      └─ 3.4  Experience the workspace as Dealer — Joule query about the new product

ex4  Guided Experience Creation (Optional, ~20 min)         [Admin then Dealer]
      ├─ 4.1  Edit the Overview page and add a wizard section
      ├─ 4.2  Add steps to the wizard
      ├─ 4.3  Add the cards for each step
      └─ 4.4  Experience the Guided Experience as a dealer
      (Cards not built yet — exercise kept as a placeholder for now)

ex5  Mobile Experience (Optional, ~15 min)                  [Dealer persona]
      ├─ 5.1  Set up Joule Work Mobile on your smartphone
      ├─ 5.2  Access the BestRun EV Dealer Portal workspace on mobile
      ├─ 5.3  Browse the product launch page on mobile
      └─ 5.4  Ask Joule a product question from the mobile interface
```

> **Note on numbering:** The original standalone "pre-order Guided Experience" exercise has been folded into the optional **ex4**. The flow diagram's "Exercise 5 / Exercise 6" labels map to repo folders **ex4 / ex5**.

---

## Timing Summary

| Exercise | Persona | Duration | Notes |
|---|---|---|---|
| ex0 Scenario Overview | — | ~15 min | |
| ex1 Create Dealer Workspace | Admin | ~20 min | |
| ex2 Workspace Content Update | Admin + Dealer | ~20 min | |
| ex3 New Product Launch Page | Admin + Dealer | ~20 min | |
| ex4 Guided Experience Creation | Admin + Dealer | ~20 min | Optional (placeholder) |
| ex5 Joule Work Mobile | Dealer | ~15 min | Optional |
| **Total (ex0–ex3)** | | **~75 min** | |
| **Total (ex0–ex4)** | | **~95 min** | |
| **Total (all)** | | **~110 min** | |

> The core session (ex0–ex3) fits well within 90 minutes. ex4 and ex5 are both optional add-ons.

---

## Visual Design Direction

The portal should look like a premium product portal — not a generic demo. Note the split introduced by the new flow:

- **Overview page (ex2) — generic dealer portal:** Hero with a generic dealer-portal tagline (not product-specific), generic Key Highlights, and the My Orders / My Invoices / My Tickets self-service cards
- **Product launch page (ex3) — Apex Series:** This is where the product branding lives — carousel of Apex product imagery, product data sheet card, and a presentation/content widget
- **Color palette:** BestRun EV brand colors — electric blue accent (#0066FF or similar), dark backgrounds for a premium feel
- **Guided Experience page (ex4, optional):** Clean step-indicator wizard UI, product images prominent in each card

Image sources: royalty-free electric bike/scooter images, or AI-generated product images with a consistent brand look. Store sample images in the repo alongside the relevant exercise.

---

## Sample Content to Prepare

Artifacts still needed to finalize the exercises:

- [x] **ex0:** The **"Dealer Management"** sample workspace exists (Overview, Tasks, and Apex Launch Material content captured); ex0.3–0.4 elaborated. More WZ-explanation content to be added later by the user
- [ ] **ex1:** `Dealer-001`…`Dealer-040` alias users provisioned in the landscape
- [ ] **ex2:** Confirm the pre-built **My Orders / My Invoices / My Tickets** cards appear in the card picker; recapture all ex2 screenshots for the generic content
- [ ] **ex2:** Confirm the dealer-alias user-profile switch path (for ex2.4)
- [x] **ex3:** Launch content set in `exercises/ex3/content/` — 6 PDFs, 3 bike images, `Apex-Series-Launch-Brochure.pptx`
- [x] **ex3:** The **Apex Launch Material** folder in the **Dealer Management** workspace is pre-loaded with the launch set (6 PDFs, 3 bike images, PPT brochure) for participants to copy
- [ ] **ex3:** Instructor enables Document Grounding per workspace (participant notifies instructor at ex1.2)
- [ ] **ex4 (optional):** Design and build the Guided Experience wizard cards (exercise is a placeholder until then)
- [ ] **ex5 (optional):** Capture Joule Work Mobile screenshots
- [ ] **All:** Workspace screenshots per sub-step from the live landscape

---

## Next Steps

**Done in this pass:**
- Planning doc re-aligned to the diagram (AD166-only, AD165 reference removed)
- ex0 expanded to the 4-step scenario overview (0.3/0.4 are placeholders pending the sample workspace)
- ex1 updated — "my managed workspaces" prompt, private+external merged, Dealer-XXX alias replaces the moderator
- ex2 fully rewritten — generic portal content + My Orders/Invoices/Tickets cards + dealer accepts invite & views overview
- ex3 rewritten — product launch content on the Overview page: copy from Dealer Management workspace, Text+PPT section, hero carousel slides, dealer Joule query
- ex4 reset to a Guided Experience placeholder (added to the Overview page); old pre-order content removed
- Old dealer-experience ex5 removed; mobile moved ex6 → ex5; main README links updated
- `ApexLine-Brochure-content.md` authored and `Apex-Series-Launch-Brochure.pptx` generated for ex3
- `TextWidgetHTMLContent.html` authored for the ex3.2 announcement widget

**Remaining:**
1. Build the ex4 Guided Experience cards, then author the exercise
2. Recapture ex2 and ex3 step screenshots (ex0 is done; current ex2/ex3 step images still show old content)
3. Add more WZ-explanation content/screenshots to ex0.4 as the sample workspace is expanded
4. Confirm landscape specifics flagged as **TODO** in each README (dealer-alias switch path, invitation surfacing, cross-workspace copy UI, widget names, mobile sign-in)
