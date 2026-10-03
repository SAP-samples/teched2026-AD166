# Exercise 5 - Experience the Portal as a Dealer

**You are now an authorized BestRun EV dealer based in Amsterdam.**

You have just received an invitation to the new BestRun EV Dealer Portal. You want to learn about the Apex Series before a customer visit tomorrow, understand the pre-order discount available to you, and place an early order to secure stock of the Apex Pro.

In this exercise you experience the portal from the dealer's perspective — using Joule to get answers, AI to summarize documents, and the Guided Experience to place a pre-order. Crucially, during the pre-order flow you will use Joule to ask about your discount directly from within the wizard, without leaving the page.

## Exercise 5.1 Accept the Dealer Portal Invitation

1. Log out of your current admin session and log in with your dealer participant credentials.

    > [!IMPORTANT]
    > **TODO:** Confirm how the dealer persona is set up in the landscape — is it a separate user account per participant, or is there a role-switch mechanism? Add the exact login steps and dealer credentials format. Replace placeholder text with the actual login URL.

    ![Login screen showing the dealer participant login](images/05_01_0010.png)
    > *📸 Capture: The SAP Build Work Zone login screen, with the dealer user email/identifier entered. The "participant number" placeholder should be visible if applicable.*

2. After login, locate the portal invitation notification for **BestRun EV Dealer Portal - ###**.

    > [!IMPORTANT]
    > **TODO:** Confirm how workspace invitations are surfaced to external users in SAP Build Work Zone — via a notification bell, a dedicated invitations page, or an email link. Update this step with the actual invitation path.

    ![Dealer home screen showing a pending workspace invitation for BestRun EV Dealer Portal](images/05_01_0020.png)
    > *📸 Capture: The dealer's home screen or notification center showing the pending invitation to the BestRun EV Dealer Portal workspace.*

3. Accept the invitation to join the workspace.

    ![Invitation acceptance confirmation — workspace now appears in the dealer's workspace list](images/05_01_0030.png)
    > *📸 Capture: The acceptance confirmation screen or the dealer's workspace list now showing the BestRun EV Dealer Portal as an accessible workspace.*

### Summary

You have accepted the invitation and the workspace is accessible. Open the portal to explore it.

---

## Exercise 5.2 Explore the Apex Series Launch Content

1. Open the **BestRun EV Dealer Portal - ###** workspace.

    ![BestRun EV Dealer Portal home page as seen by the dealer — Apex Series hero image visible](images/05_02_0010.png)
    > *📸 Capture: The dealer's view of the BestRun EV portal — the Apex Series hero image at the top, the launch announcement text below, and the three model cards (City / Trail / Pro) in the lower section. This is the "reveal" moment of the session.*

2. Scroll through the **Apex Series** page to read the launch content and model overviews.

    ![Apex Series page scrolled to show the three model cards](images/05_02_0020.png)
    > *📸 Capture: The model cards section showing all three Apex models with their product images and AI-generated overview text. The dealer perspective should feel polished and premium.*

3. Note the **Order Now** page in the workspace navigation — you will use it later in this exercise.

### Summary

The portal content is compelling and professional. Next you will use Joule to go deeper on the Apex Pro before your customer meeting.

---

## Exercise 5.3 Ask Joule a Product Question

As a dealer, you have a customer interested in the Apex Pro coming in tomorrow. You need to know the exact range figures before the meeting — without downloading a PDF.

1. Open the **Joule** panel from within the workspace.

    ![Joule panel open within the dealer portal workspace](images/05_03_0010.png)
    > *📸 Capture: The Joule panel open within the BestRun EV Dealer Portal context, showing the workspace name as context in the Joule header or system message.*

2. Ask the following question:

    ```
    What is the maximum range of the Apex Pro in eco mode?
    ```

    ![Joule answer for the Apex Pro range question with source citation from the Technical Spec Sheet](images/05_03_0020.png)
    > *📸 Capture: Joule's grounded answer — including the specific range figure and a source citation referencing the Apex Series Technical Spec Sheet. The citation should be clearly visible (link, footnote, or document badge).*

3. Ask a follow-up question:

    ```
    How long does it take to charge the Apex Pro from 0 to 80%?
    ```

    ![Joule answer for the charging time question with source citation](images/05_03_0030.png)
    > *📸 Capture: Joule's follow-up answer giving the specific charging time, sourced from the Apex Pro Battery & Drive Technology Guide.*

### Summary

Joule answered both questions instantly from the grounded documents — no PDF required. Next you will use AI to summarize the battery guide before your customer visit.

---

## Exercise 5.4 Use AI to Summarize the Battery Technology Guide

The Apex Pro Battery & Drive Technology Guide is 12 pages. You need a quick briefing before your customer visit.

1. In the workspace, navigate to the **Documents** section and locate the **Apex Pro Battery & Drive Technology Guide**.

    > [!IMPORTANT]
    > **TODO:** Confirm whether documents are accessible to external dealer users in the workspace and how the AI summary feature is invoked — via a document action menu, a dedicated summary button, or through Joule. Update this step with the exact path.

    ![Documents section of the dealer portal showing the Apex Pro Battery & Drive Technology Guide](images/05_04_0010.png)
    > *📸 Capture: The documents section listing the available files. The Apex Pro Battery & Drive Technology Guide should be visible in the list.*

2. Select the document and click **Summarize** or use the **AI summary** option.

    ![AI summary option available on the Battery & Drive Technology Guide document](images/05_04_0020.png)
    > *📸 Capture: The document detail view or action menu showing the AI summary/summarize option for the Battery & Drive Technology Guide.*

3. Review the AI-generated summary.

    ```
    Expected output (approximate):
    - The Apex Pro uses a next-generation LFP (Lithium Iron Phosphate) battery,
      offering improved thermal stability and a longer cycle life than previous models.
    - Maximum range is 200 km in eco mode, 140 km in standard mode.
    - Charging from 0–80% takes approximately 2.5 hours with the fast charger.
    - The integrated BMS (Battery Management System) automatically optimizes
      charge cycles for long-term battery health.
    - Service interval for the drive system is 5,000 km or annually, whichever comes first.
    ```

    > [!IMPORTANT]
    > **TODO:** The expected output above is illustrative. Replace with the actual AI summary output once the document is authored and the landscape is tested. Verify that the summary aligns with the data in the final version of the Battery Guide document.

    ![AI-generated 5-point summary of the Battery & Drive Technology Guide](images/05_04_0030.png)
    > *📸 Capture: The AI-generated summary displayed — showing 4–6 bullet points covering the main technical highlights of the Apex Pro battery system.*

### Summary

In under 30 seconds you have a clear, structured summary of a 12-page technical document. You are ready for tomorrow's customer demo. Now it is time to place a pre-order.

---

## Exercise 5.5 Open the Pre-Order Guided Experience

1. In the workspace navigation, click **Order Now**.

    ![Order Now page opening in the dealer portal](images/05_05_0010.png)
    > *📸 Capture: The Order Now page opening — showing the Guided Experience widget at the top with the first step (Model Selection) displayed and a step indicator showing "Step 1 of 4".*

2. The Guided Experience opens at **Step 1 — Model Selection**. Review the three model options.

    ![Guided Experience Step 1 — Model Selection showing Apex City, Apex Trail, and Apex Pro cards](images/05_05_0020.png)
    > *📸 Capture: Step 1 of the wizard — three model selection cards side by side (Apex City, Apex Trail, Apex Pro), each with a product image, model name, and a brief key spec line. A "Select" button on each card.*

3. Click **Select** on the **Apex Pro** card.

    ![Apex Pro selected in Step 1, Next button becomes active](images/05_05_0030.png)
    > *📸 Capture: Step 1 with Apex Pro selected — the Apex Pro card highlighted or checked, and the "Next" button becoming active/clickable.*

4. Click **Next** to proceed to Step 2.

---

## Exercise 5.6 Ask Joule About Your Pre-Order Discount

You are now on **Step 2 — Configuration & Quantity**. You are planning to order 12 Apex Pro units with upfront payment, but you want to understand your discount before committing.

1. In Step 2, enter **12** as the quantity and select **Upfront Payment** as the payment terms.

    ![Guided Experience Step 2 — Configuration & Quantity with 12 units and Upfront Payment selected](images/05_06_0010.png)
    > *📸 Capture: Step 2 of the wizard — quantity field filled with "12", color variant selected, and "Upfront Payment" chosen in the payment terms dropdown.*

2. Click **Next** to move to **Step 3 — Pricing & Discount Review**.

    ![Guided Experience Step 3 — Pricing & Discount Review showing the calculated discount](images/05_06_0020.png)
    > *📸 Capture: Step 3 of the wizard — showing the dealer's base price for 12 Apex Pro units, with a discount percentage calculated and displayed. The total discounted price should be visible.*

3. You notice the discount shown and want to understand how it was calculated — and whether ordering more units or changing payment terms would give you a better rate. **Open the Joule panel** without leaving the wizard.

    ![Joule panel open alongside the Guided Experience wizard — Step 3 visible on the left, Joule panel on the right](images/05_06_0030.png)
    > *📸 Capture: The key screenshot of the session — the Guided Experience wizard showing Step 3 on the main content area, with the Joule side panel open simultaneously. Both should be clearly visible in the same view.*

4. Ask Joule the following question:

    ```
    What is my pre-order discount for 12 Apex Pro units with upfront payment?
    ```

    ![Joule answering the discount question with the specific discount percentage, citing the Pre-Order Discount Policy](images/05_06_0040.png)
    > *📸 Capture: Joule's response explaining the discount — the base discount percentage for 12 units × upfront payment, the Apex Pro cap rule (10% maximum), and any applicable early bird bonus. Source citation to the Pre-Order Discount Policy document should be visible.*

5. Ask a follow-up to see if the early bird bonus applies:

    ```
    Does the early bird bonus apply to my order?
    ```

    ![Joule answering the early bird bonus eligibility question](images/05_06_0050.png)
    > *📸 Capture: Joule's response confirming whether the early bird bonus (+2%) applies, based on whether the pre-order is being placed at least 60 days before the Apex Series launch date.*

6. Close the Joule panel and confirm the discount shown in Step 3 matches Joule's explanation.

    > [!NOTE]
    > The discount shown in the Pricing & Discount Review card is calculated dynamically from the quantity and payment terms entered in Step 2. Joule's answer confirms the logic — you did not need to find or read the discount policy document yourself.

### Summary

You used Joule as an inline assistant while filling in the pre-order wizard — without leaving the page, without opening a document. This is Document Grounding working at its most useful: answering a specific, contextual business question at the exact moment it is needed.

---

## Exercise 5.7 Submit Your Pre-Order

1. Click **Next** on Step 3 to proceed to **Step 4 — Pre-Order Confirmation**.

    ![Guided Experience Step 4 — Pre-Order Confirmation showing the complete order summary](images/05_07_0010.png)
    > *📸 Capture: Step 4 of the wizard — the complete order summary showing: Model (Apex Pro), Quantity (12), Color variant, Payment terms (Upfront), Unit price, Discount applied, Total discounted price. A "Submit Pre-Order" button visible at the bottom.*

2. Review the order summary and click **Submit Pre-Order**.

    ![Pre-order submitted successfully — confirmation screen with reference number](images/05_07_0020.png)
    > *📸 Capture: The order submission success screen — showing a confirmation message, the pre-order reference number, and an estimated processing timeline. This is the final "done" moment of the main exercise flow.*

3. Note the pre-order reference number displayed on screen.

    > [!IMPORTANT]
    > **TODO:** Confirm whether the pre-order confirmation card generates a real reference number via a connected backend service, or whether it displays a simulated/static reference number for demo purposes. Update the step text and screenshot description accordingly.

### Summary

Your pre-order is submitted. You have completed the full dealer journey — from exploring product information with Joule, to summarizing a technical document with AI, to using Joule mid-wizard to understand your commercial terms, to placing a pre-order.

If you have a smartphone available, continue to Exercise 6 to access the portal from Joule Work Mobile.

Continue to — [Exercise 6 - Access the Dealer Portal from Joule Work Mobile (Optional)](../ex6/README.md)
