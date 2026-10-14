# Exercise 4 - Create the Apex Pre-Order Page

The Apex Series launch announcement is live on the Overview page. Now it's time to give dealers a place to act on it. In this exercise you will create a dedicated **Apex Pre-Order** page and build it out with three sections:

1. **An intro text widget** — a call-to-action banner that sets the context before the wizard
2. **A Guided Experience section** — a 5-step pre-order wizard that walks the dealer through model selection, quantities, payment terms, order review, and confirmation
3. **An order status card** — a live status card on the same page that reflects what the dealer has configured in the wizard

> [!NOTE]
> This exercise is performed as the **portal admin** (your primary **AD166-XXX** account). If you are still on your dealer alias from a previous exercise, switch back via the **Alias Account Switcher** in your profile menu first.

---

## Exercise 4.1 Create the Apex Pre-Order Page

First, create a new page in your Dealer Portal that will host the pre-order wizard.

1. Navigate to your **BestRun EV Dealer Portal AD166-XXX** workspace.

2. In the workspace navigation bar (where the **Overview**, **Content**, **Forums**, and **Events** tabs are), click the **+** icon at the right end of the tab row. The **Add Tab to Navigation Bar** dialog opens.

    In the dialog, under the **Overview** section, select **Workpage** — described as *"Create a freestyle page with layouts"*.

    ![Add Tab to Navigation Bar dialog with Workpage highlighted in the Overview section](images/04_01_0010.png)

3. The **Add Workpage** dialog opens. Leave **New Workpage** selected. In the **Tab Name** field, enter:

    ```
    Apex Pre-Order
    ```

    Leave the **Save in Folder** set to **Content** (the default) and the **Contributor** as your user. Click **Add**.

    ![Add Workpage dialog with Tab Name set to Apex Pre-Order and Add button highlighted](images/04_01_0020.png)

    The new **Apex Pre-Order** workpage opens in edit mode, showing the **Title** field pre-filled with `Apex Pre-Order` and an empty canvas with an **Add** button in the centre.

    ![Empty Apex Pre-Order workpage open in edit mode with the Add button in the centre](images/04_01_0030.png)

> [!NOTE]
> A yellow banner warns that *"This workpage is visible to external users"* — this is expected, since the workspace is configured as an external dealer portal. You will build out this page in the exercises below.

---

## Exercise 4.2 Add the Intro Text Widget

Before the wizard, add a short call-to-action banner so dealers understand what the page is for as soon as they land on it.

1. The **Apex Pre-Order** page is already open in edit mode from Exercise 4.1. Click the **Add** button (with the dropdown arrow) in the centre of the empty canvas. A new empty section appears on the page.

2. Inside the new section, click the **Add Content** button (the **+** icon inside the section). The **Add Content** dialog opens. Select **Text** — described as *"Create and format text with a rich text editor."*

    ![Add Content dialog with the Text widget highlighted](images/04_02_0010.png)

3. The rich text editor opens inside the section. In the editor toolbar, click the **Source code** button (the `<>` icon — hovering over it shows the tooltip *"Source code"*) to open the source code dialog.

    ![Text widget editor toolbar with the Source code button highlighted](images/04_02_0020.png)

    In the source code dialog that opens, paste the following HTML and click **Save**:

    ```html
    <div style="font-family: Arial,Helvetica,sans-serif; text-align: center; padding: 28px 20px; background: linear-gradient(135deg, #e8f0fe 0%, #f0f4ff 100%); border-radius: 8px; border: 1px solid #c8d8f5;">
      <div style="display: inline-block; background: #0066FF; color: #fff; font-size: 11px; font-weight: bold; letter-spacing: 1.5px; padding: 4px 12px; border-radius: 3px; margin-bottom: 12px;">PRE-ORDER OPEN NOW</div>
      <h3 style="font-size: 22px; color: #0b1a2b; margin: 0 0 10px;">Ready to secure your Apex Series allocation?</h3>
      <p style="color: #5a6b7b; font-size: 14px; margin: 0 0 6px;">Use the 5-step guided wizard below to configure your order, choose your payment terms, and lock in your pre-order discount — all in under 5 minutes.</p>
      <p style="color: #5a6b7b; font-size: 13px; margin: 0;"><strong>Have questions along the way?</strong> Keep Joule open in the panel — it can answer any question about the Apex Series, pricing, or pre-order terms instantly.</p>
    </div>
    ```

4. Verify that the banner renders correctly inside the editor — you should see the blue **PRE-ORDER OPEN NOW** badge, the heading *"Ready to secure your Apex Series allocation?"*, and the two lines of supporting text below it.

    ![Text widget rendered in the editor showing the PRE-ORDER OPEN NOW banner](images/04_02_0030.png)

---

## Exercise 4.3 Add the Guided Experience Section

Now add the 5-step pre-order wizard below the intro banner.

### 4.3.1 Add the Guided Experience section

1. Hover below the intro banner section until the **Add section** bar appears. Click it. A small popup shows two section types — **Freestyle** and **Wizard**. Select **Wizard**.

    ![Add Section popup showing Freestyle and Wizard options, with Wizard highlighted](images/04_03_0010.png)

2. The **Add Wizard** dialog opens. Fill in the **Title** and **Description** fields:

    | Field | Value |
    |-------|-------|
    | Title | `Apex Series Pre-Order` |
    | Description | `Secure your Apex Series allocation before the public launch. Complete the 5-step wizard to configure your order, lock in your pre-order discount, and receive your confirmation.` |

3. Under **Display Options**, select **Opens as a dialog**. This opens the wizard in a full-screen dialog when dealers launch it, giving the cards more space to render comfortably.

    ![Add Wizard dialog with Title and Description filled in and Opens as a dialog selected](images/04_03_0020.png)

### 4.3.2 Add the five wizard steps

5. Click **Add step**. Set the step **Title** and **Description** exactly as shown:

    | Field | Value |
    |-------|-------|
    | Title | `Choose Your Models` |
    | Description | `Select the Apex Series models you want to pre-order. You can choose one or more models.` |

6. Click **Add step** again. Fill in:

    | Field | Value |
    |-------|-------|
    | Title | `Quantities & Variants` |
    | Description | `Set the quantity and color variant for each selected model. Your total units determine your base discount tier.` |

7. Click **Add step** again. Fill in:

    | Field | Value |
    |-------|-------|
    | Title | `Payment Terms` |
    | Description | `Choose how you'd like to pay. Payment terms affect your final pre-order discount — use Joule to clarify any questions.` |

8. Click **Add step** again. Fill in:

    | Field | Value |
    |-------|-------|
    | Title | `Order Summary` |
    | Description | `Review your complete pre-order: models, quantities, discounted prices, delivery windows, and terms.` |

9. Click **Add step** again. Fill in:

    | Field | Value |
    |-------|-------|
    | Title | `Confirm Pre-Order` |
    | Description | `Your pre-order is submitted. Note your reference number and explore what happens next.` |

The wizard now shows a 5-step indicator. Each step is empty until you assign a card in the next section.

10. **(Optional)** The dialog also shows a final **Done** step (auto-added by WZ to mark completion). Rename it to `Pre-Order Successful` to make the end state clearer for dealers.

    Once all steps are filled in you will see the **Wizard Cover Preview** at the bottom of the dialog — showing the wizard title and description as dealers will see it on the launch card.

    ![Add Wizard dialog with all 5 steps filled in and the final step renamed to Pre-Order Successful, showing the Wizard Cover Preview](images/04_03_0030.png)

11. Click **Save** to create the wizard section.

The five pre-order cards have been pre-loaded into the **Card Catalog** of this tenant by the workshop team. You will assign one card to each step.

10. After saving, the wizard section appears on the page showing the 6-step indicator. Step 1 **Choose Your Models** is active. Click the **Add Content** button inside the step area.

    ![Wizard section on the page showing the 6-step indicator, with Add Content button visible in Step 1](images/04_03_0040.png)

    In the **Add Content** dialog that opens, select **Cards** — described as *"Show content from various sources to enable user interaction."*

    ![Add Content dialog with Cards highlighted](images/04_03_0050.png)

    In the card picker that follows, type `Guided` in the search box to filter the list. Select **Guided1 Card | Model Selection**.

    ![Add Cards picker showing all 5 Guided cards after searching for "Guided", with Guided1 Card | Model Selection highlighted](images/04_03_0060.png)

    The **Guided1 Card | Model Selection** card renders inside Step 1 of the wizard, showing the three Apex models.

    ![Step 1 of the wizard showing the Guided1 card rendered with the three Apex models](images/04_03_0070.png)

11. In the step indicator bar, click **2 — Quantities & Variants** to navigate to Step 2. The step area switches to an empty **Add Content** state. Repeat the same process — click **Add Content** → **Cards** → search `Guided` → select **Guided2 Card | Quantities & Variants**.

11. In the step indicator bar, click **2 — Quantities & Variants** to navigate to Step 2. The step area switches to an empty **Add Content** state, just like Step 1 looked before you added its card.

    ![Step 2 Quantities & Variants active in the wizard, showing the empty Add Content state](images/04_03_0080.png)

    Repeat the same process for each remaining step — click the step number in the indicator bar, then **Add Content** → **Cards** → search `Guided` → select the matching card:

    **Step 2 — Quantities & Variants** → select `Guided2 Card | Quantities & Variants`

    ![Step 2 with Guided2 card rendered showing quantity and color variant configurator](images/04_03_0090.png)

    **Step 3 — Payment Terms** → select `Guided3 Card | Payment Terms`

    ![Step 3 with Guided3 card rendered showing payment term options and discount breakdown](images/04_03_0100.png)

    **Step 4 — Order Summary** → select `Guided4 Card | Order Summary`

    ![Step 4 with Guided4 card rendered showing the full order summary with discounted line totals](images/04_03_0110.png)

    **Step 5 — Confirm Pre-Order** → select `Guided5 Card | Pre-Order Confirmation`

    ![Step 5 with Guided5 card rendered showing the pre-order reference number and order recap](images/04_03_0120.png)

> [!NOTE]
> Each card passes context to the next step automatically via the browser's session storage. No additional card configuration is required — the cards read and write a shared `apexPreOrder` key that keeps the wizard state as the dealer progresses through the steps.

---

## Exercise 4.4 Add the Order Status Card

Below the wizard, add the **Pre-Order Status** card in a new Freestyle section. This card listens to the wizard's progress and shows the dealer a live summary of their pre-order on the same page — updating in real time as they move through the steps.

1. Hover below the Guided Experience (Wizard) section. An **Add section** bar appears. Click it.

    ![Add section popup below the wizard section showing Freestyle and Wizard options](images/04_04_0010.png)

2. In the popup, select **Freestyle**.

    A new empty Freestyle section is added below the wizard.

3. In the new section, click **Add Content**.

4. In the Add Content dialog, select **Cards**.

5. In the Add Cards picker, search for:

    ```
    Pre-Order Status
    ```

    Select **BestRun EV | Pre-Order Status** and click **Add**.

    ![Add Cards dialog with "Pre-Order Status" searched, showing the BestRun EV | Pre-Order Status card](images/04_04_0020.png)

> [!IMPORTANT]
> Make sure you select **BestRun EV | Pre-Order Status**, *not* the Guided5 confirmation card. The status card is the one purpose-built for this page — it starts empty and fills in as the dealer works through the wizard. (If it doesn't appear in the picker, upload `preorder-status-card.card.zip` to the Card Catalog first.)

6. The card is added below the wizard. Because no pre-order has been started yet, it shows its empty state — a **"No pre-order started yet"** illustration. This is exactly what you want: the card stays empty until a dealer runs the wizard.

    ![Pre-Order Status card on the page showing the "No pre-order started yet" empty state](images/04_04_0030.png)

7. Click **Publish** in the top-right toolbar to publish the **Apex Pre-Order** page.

8. With the published **Apex Pre-Order** page open, **copy the full page URL** from your browser's address bar and keep it somewhere handy (a note or scratch file). You will paste it into the Button card's navigation target in Exercise 4.5.

    ![Published Apex Pre-Order page with the browser address bar showing the page URL to copy](images/04_04_0040.png)

> [!TIP]
> The URL looks like `https://<host>.workzone.cfapps.eu10.hana.ondemand.com/site#workzone-home&/groups/<groupId>/workpage_tab/...`. Copy the whole thing — it points directly to this Apex Pre-Order workpage.

> [!NOTE]
> When no wizard data exists yet, the status card shows an empty-state illustration ("No pre-order started yet"). As soon as the dealer progresses through the wizard, the card updates automatically — first showing an "in progress" checklist, then switching to the confirmed order summary once Step 5 is completed.

---

## Exercise 4.5 Add a Button Card on the Overview Page

Now that the Apex Pre-Order page exists, give dealers a clear path to it straight from the **Overview** page. You will add a **Button card** below the Apex Series launch announcement that links directly to the pre-order wizard.

1. Open the **Overview** page (the one you built in Exercise 3) and enter **edit mode**. Scroll down to the **Apex Series launch announcement** section, hover just below it until the **Add section** bar appears, and click it. In the popup, select **Freestyle**.

    ![Overview page in edit mode with the Add Section popup open below the Apex launch announcement, showing Freestyle and Wizard options](images/04_05_0010.png)

2. In the new Freestyle section, click **Add Content**, select **Cards**, and in the Add Cards picker search for:

    ```
    Button Card
    ```

    Select **Button Card** — "A component card that renders a fully configurable button with title, subtitle, icon, colors, borders and a navigation target" — and click **Add**.

    ![Add Cards dialog with "Button Card" searched, showing the Button Card result](images/04_05_0020.png)

3. The Button Card configuration dialog opens. In the **General** section, set the following values — the live preview on the right updates as you type:

    | Field | Value |
    | --- | --- |
    | Fill Card Background | **Yes** |
    | Title | `Start Your Apex Series Pre-Order` |
    | Subtitle | `Reserve your units before public launch — secure special dealer pricing` |
    | Icon | Navigation Right Arrow |
    | Icon Size (rem) | `3` |
    | Title Font Size (rem) | `2` |
    | Subtitle Font Size (rem) | `1.5` |
    | Target URL | *paste the Apex Pre-Order page URL you copied in Exercise 4.4* |
    | Open in new tab | **No** |

    ![Button Card configuration dialog with the title, subtitle and sizing values set, showing the blue filled preview](images/04_05_0030.png)

4. Click **Save** to close the Button card dialog, then click **Publish** in the top-right toolbar to publish the updated **Overview** page.

    The Overview page now shows a full-width **"Start Your Apex Series Pre-Order"** button beneath the Apex Series announcement. Click it to confirm it opens the **Apex Pre-Order** page (in a new tab).

    ![Published Overview page showing the full-width Start Your Apex Series Pre-Order button below the announcement](images/04_05_0040.png)

### Summary

Dealers now have a clear call-to-action on the Overview page that takes them straight into the Apex Pre-Order wizard.

---

## Exercise 4.6 Experience the Full Flow as Dealer-XXX

Everything is now in place. Time to put yourself back in the dealer's shoes and run the complete pre-order journey end to end — from spotting the call-to-action on the Overview page to receiving a confirmed pre-order.

1. Switch to your dealer alias: open the **profile menu** (your avatar / initials in the top-right corner) and select **Switch to Alias Account**, just as you did in Exercises 2.6 and 3.4. Choose your **Dealer-XXX** alias to switch into the dealer view, then navigate to your **BestRun EV Dealer Portal AD166-XXX** and open the **Overview** page.

    Below the Apex Series announcement you will spot the new, full-width **Start Your Apex Series Pre-Order** button you added in Exercise 4.5. This is the dealer's clear path from "I heard about the launch" to "let me reserve my units." Click the big blue button to begin.

    ![Dealer view of the Overview page with the full-width "Start Your Apex Series Pre-Order" button below the Apex Series announcement](images/04_06_0010.png)

2. The button takes you straight to the new **Apex Pre-Order** page. Take a moment to review it — the intro banner (*"Ready to secure your Apex Series allocation?"*), the **Apex Series Pre-Order** guided experience with its **Start** button, and, further down, the **Pre-Order Status** card showing its empty **"No pre-order started yet"** state (it will fill in as you progress).

    When you are ready, click **Start** on the guided experience to begin the pre-order wizard.

    ![Apex Pre-Order page showing the intro banner, the guided experience with the Start button, and the empty Pre-Order Status card](images/04_06_0020.png)

3. The wizard opens on **Step 1 — Choose Your Models**, showing all three Apex models with their key specs and dealer net pricing. Select **all three** — **Apex City**, **Apex Trail**, and **Apex Pro** — by ticking each card's checkbox. The counter updates to **"3 models selected"** and **Save & Continue** becomes available.

    ![Step 1 of the wizard with Apex models shown; Apex Pro carries a "Limited Allocation" badge](images/04_06_0030.png)

    Before moving on, notice the orange **Limited Allocation** badge on the **Apex Pro** — a detail a premium-focused dealer will immediately want to understand. Rather than guess, open **Joule** from the top navigation bar and ask (the step card even suggests this question):

    ```
    Why is the Apex Pro marked as limited allocation?
    ```

    Joule answers from the Apex Launch Material documents, so you get the official reason without leaving the pre-order flow.

4. Open **Joule** from the top navigation bar — the panel opens **alongside the wizard**, so the guided experience stays exactly where it is. Ask:

    ```
    Why is Apex Pro marked as limited allocation?
    ```

    Joule explains the allocation policy in full — production allocation is managed by priority, so **Platinum and Gold dealers who pre-order more than 60 days before launch are guaranteed their full order**, **Silver dealers (or any tier ordering 30+ days ahead) are guaranteed up to 5 units**, later orders draw on remaining allocation, and dealers are notified at least 30 days ahead if an order cannot be fully filled (with the option to cancel unfulfillable units without penalty). The answer carries an inline **[1]** citation and a **Sources (1)** control — click the citation to open the underlying document in a new tab and read the full policy.

    ![Joule answering "Why is Apex Pro marked as limited allocation?" in the side panel while the pre-order wizard stays open underneath](images/04_06_0040.png)

    Once you have the answer, **close the Joule panel**, click **Save & Continue** on the step card, then **Next** at the bottom of the wizard to advance to **Step 2 — Quantities & Variants**.

5. **Step 2 — Quantities & Variants.** For each model, pick a colour variant and set the order quantity. The **subtotal**, the running **units total**, and the **Discount Tier Progress** bar all update live. Try, for example:

    - **Apex City** — Midnight Black, **5** units
    - **Apex Trail** — Forest Green, **10** units
    - **Apex Pro** stays at its minimum of **2** units (recall the MOQ for the Apex Pro)

    That makes **17 units total**, which puts you in the **10–19 units → 10% base discount** tier — and the bar even nudges you that just 3 more units would reach the **20–49 (14%)** tier. Adjust the quantities up and down to watch the discount tier change in real time.

    ![Step 2 of the wizard with quantities and colours set, the 17-unit total, and the Discount Tier Progress bar showing the 10% tier](images/04_06_0050.png)

    The step card suggests more Joule questions. Open **Joule** and ask one, for example:

    ```
    Do I need to order all models at once to qualify for the higher discount tier?
    ```

    Then click **Save & Continue** and **Next** to move on to **Step 3 — Payment Terms**.

6. **Step 3 — Payment Terms.** Choose how you want to pay — the choice directly affects your discount:

    - **Upfront** (100% at checkout, no invoice) → **10% base discount**
    - **Net 30** (invoice on launch date, due 30 days later) → **8% base discount**
    - **Net 60** → Gold / Platinum tier only (greyed out as *Not available* for a Silver dealer)

    Pick **Upfront** to maximise the discount. The **Discount Breakdown** then shows exactly how your effective discount is built up: **10% base + 2% early-bird** (ordering ≥60 days before launch) **+ 1% first-ever pre-order = 13% effective** for City & Trail — while the **Apex Pro is capped at 10%**.

    ![Step 3 of the wizard showing the Upfront/Net 30/Net 60 options and the Discount Breakdown with the 13% effective discount and Apex Pro capped at 10%](images/04_06_0060.png)

    This is the most intricate moment in the flow — exactly where grounded answers help. The step card lists several Joule questions; open **Joule** and let it do the math for your exact order:

    ```
    How much more do I save with upfront payment vs Net 30 if I order 5 Apex City, 10 Apex Trail and 2 Apex Pro units?
    ```

    Joule works through it step by step — totalling your 17 units, reading the base-discount matrix (10% upfront vs 8% Net 30 for the 10–19 tier), and concluding that upfront payment gives a **2% higher discount** — with every figure cited back to the source policy. This is the comparative analysis that helps the dealer understand the concrete difference between the plans while deciding how to pre-order.

    ![Joule's side-by-side comparison of upfront vs Net 30 savings for the dealer's exact 5 / 10 / 2-unit order](images/04_06_0070.png)

    When you are satisfied with the terms, click **Save & Continue** and **Next** to advance to **Step 4 — Order Summary**.

7. **Step 4 — Order Summary.** This is the complete review before you commit. The table lists every model with its colour, quantity, **net (list)** price, the **discount** applied, the **net (final)** price, and the **line total**:

    | Model | Colour | Qty | Net (list) | Disc. | Net (final) | Line total |
    | --- | --- | --- | --- | --- | --- | --- |
    | Apex City | Midnight Black | 5 | EUR 1,471 | −13% | EUR 1,280 | EUR 6,399 |
    | Apex Trail | Forest Green | 10 | EUR 2,581 | −13% | EUR 2,245 | EUR 22,455 |
    | Apex Pro | Matte Black | 2 | EUR 4,430 | −10% | EUR 3,987 | EUR 7,974 |

    The totals confirm **17 units**, a pre-discount value of **EUR 42,025**, **savings of EUR 5,197**, and a **total dealer net payable of EUR 36,828**. A **Discount Summary** restates the tier and terms (10–19 units → 10% base + 2% early bird + 1% first-order; Apex Pro capped at 10%), and a **Delivery** panel shows the per-model windows (Apex City & Trail 5–10 business days, Apex Pro 7–14 business days — from the official launch date, priority batch allocation confirmed).

    ![Step 4 Order Summary with per-model discounted pricing, the 17-unit totals, discount summary, delivery windows, and the Terms & Conditions acceptance checkbox](images/04_06_0080.png)

    Before you can continue, tick the box to **accept the Apex Series Pre-Order Terms & Conditions** — acknowledging that the pre-order is binding on submission and subject to the cancellation and delivery terms in the document.

> [!TIP]
> Unsure what you are agreeing to? The step card suggests Joule questions for exactly this moment, such as *"What are my cancellation rights after submitting a pre-order?"* and *"What happens if BestRun EV cannot deliver within the stated window?"* — ask Joule before you accept.

With the terms accepted, click **Save & Continue** and **Next** to move on to **Step 5 — Confirm Pre-Order**.

8. **Step 5 — Confirm Pre-Order.** The wizard confirms **"Pre-Order Submitted Successfully"** — you have secured your Apex Series allocation, and BestRun EV will confirm within 2 business days. The screen gives you everything to keep on file:

    - A unique **Pre-Order Reference** (for example `APEX-PRE-2026-37350`) with the submission date — quote it in any communication with BestRun EV.
    - An **Order Recap** — Apex City ×5 (Midnight Black), Apex Trail ×10 (Forest Green), Apex Pro ×2 (Matte Black); **17 units**, **Upfront** payment, **EUR 5,197** total savings, **EUR 36,828** payable.
    - A **What Happens Next** panel — confirmation email, processing within 2 business days, batch-allocation confirmation by your regional account manager, and invoicing on the official launch date per your terms.
    - A **Keep Joule open for what comes next** panel suggesting post-order questions such as *"What are the warranty terms for the Apex Trail?"*, *"How do I report damage on delivery of a pre-ordered unit?"*, and *"Can I change the quantities in my pre-order after submission?"*

    ![Step 5 confirmation showing the success banner, pre-order reference, order recap, what-happens-next panel, and the Pre-Order Status card now Confirmed behind the dialog](images/04_06_0090.png)

    Look at the page **behind** the wizard: the **Pre-Order Status card** you added in Exercise 4.4 has already flipped from its empty state to **CONFIRMED**, mirroring this exact order — the live cross-card update you built now paying off end to end.

9. **Step 6 — Pre-Order Successful.** A final **"Congrats! You're all done"** screen confirms the guided experience is complete. Click **Finish**, then **Close** to exit the wizard and return to the Apex Pre-Order page.

    ![Final wizard step showing the "Congrats! You're all done" confirmation with the Finish button](images/04_06_0100.png)

10. **Review your order status.** Back on the Apex Pre-Order page, the guided experience now shows a completed progress bar, and the **Pre-Order Status card** below it displays your **CONFIRMED** pre-order in full — reference **APEX-PRE-2026-37350**, the three models with their quantities and colours, the pre-discount total, your **EUR 5,197** saving, the **EUR 36,828** total payable, and the estimated delivery window. This card is the dealer's home for the pre-order: they can return here any time to check the **latest status** and follow up once BestRun EV has processed the order.

    ![Apex Pre-Order page after completing the wizard, showing the Pre-Order Status card with the CONFIRMED order details](images/04_06_0110.png)

### What the Dealer Just Experienced

In one guided flow, the dealer went from the launch announcement to a **confirmed, discounted pre-order** — choosing models, setting quantities and variants, comparing payment terms, accepting the terms, and receiving a reference number — without ever leaving the portal. The **Pre-Order Status card** now gives them a lasting, at-a-glance view to return to for the latest status and follow-up.

The real lesson is how two capabilities combine. The **Guided Experience** breaks a genuinely complex process — tiered pricing, stacked discounts, allocation rules, payment terms, binding T&Cs — into clear, confident steps, while **Joule** stands beside every decision with instant, cited answers grounded in BestRun EV's own documents. Together they let a dealer make smooth, well-informed decisions and complete an intricate execution flow quickly, with AI assistance at exactly the moments it matters.

That is the promise of an **AI-enabled business site** on SAP Build Work Zone: unstructured content, a live business process, and grounded AI — brought together on a single page.

---

Continue to — [Exercise 5 - Access the Dealer Portal from Joule Work Mobile (Optional)](../ex5/README.md)
