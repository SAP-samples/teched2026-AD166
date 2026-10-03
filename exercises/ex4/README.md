# Exercise 4 - Add the Pre-Order Guided Experience

In this exercise you assemble the pre-order workflow that dealers will use to place orders for Apex Series units. The four UI cards that make up the wizard have been pre-built and are already available in the workspace card catalog — your task is to create a new page, add the cards, configure the Guided Experience flow, and publish it.

By the end of this exercise, the dealer portal has a fully functional **Order Now** page with a four-step pre-order wizard.

## Exercise 4.1 Find the Pre-Built Apex Pre-Order Cards

The four pre-order UI cards are already loaded in the card catalog for this landscape. You will locate them before assembling the Guided Experience.

1. In the workspace administration console, navigate to the **Card Catalog** (or **UI Card Repository**).

    > [!IMPORTANT]
    > **TODO:** Confirm the exact navigation path to the UI Card Catalog in this version of SAP Build Work Zone advanced edition (e.g., via the admin console, a dedicated card management section, or content manager).

    ![Card Catalog or UI card repository overview showing the list of available cards](images/04_01_0010.png)
    > *📸 Capture: The Card Catalog overview — a list or grid view of available UI cards. The search or filter functionality should be visible.*

2. Search for **Apex** or **BestRun** to filter the pre-built cards.

    ![Card Catalog filtered to show the four Apex pre-order cards](images/04_01_0020.png)
    > *📸 Capture: The Card Catalog filtered view showing the four pre-built cards: "Apex - Model Selection", "Apex - Configuration & Quantity", "Apex - Pricing & Discount Review", and "Apex - Pre-Order Confirmation".*

3. Verify all four cards are present and note their names:

    | Card | Purpose |
    |---|---|
    | **Apex - Model Selection** | Dealer selects which Apex model(s) to pre-order |
    | **Apex - Configuration & Quantity** | Dealer selects quantity, color variant, and delivery window |
    | **Apex - Pricing & Discount Review** | Shows dealer pricing and discount calculated from quantity and payment terms |
    | **Apex - Pre-Order Confirmation** | Order summary and submit action, generates a reference number |

    > [!IMPORTANT]
    > **TODO:** Confirm the exact names of the four pre-built cards as they appear in the card catalog. Update the table above with the exact names.

### Summary

The four pre-order cards are confirmed in the catalog. You are ready to assemble the Guided Experience.

---

## Exercise 4.2 Create the Order Now Page

You will add a new page to the workspace to host the pre-order Guided Experience.

1. From the workspace, open the page management view and click **Add Page**.

    ![Page management view with the Add Page option](images/04_02_0010.png)
    > *📸 Capture: The workspace page navigation or admin view showing the existing pages (e.g., Apex Series) and a visible option to add a new page.*

2. Name the page **Order Now** and select a **single-column** or **wizard** layout.

    > [!IMPORTANT]
    > **TODO:** Confirm whether a dedicated "Guided Experience" page type or layout exists in this version of SAP Build Work Zone. If so, update the step to use that page type instead of a generic layout.

    ![New page creation dialog with "Order Now" as the page name](images/04_02_0020.png)
    > *📸 Capture: The new page dialog with the name "Order Now" entered and the layout selection visible.*

3. Save the page. The **Order Now** page now appears in the workspace navigation.

    ![Workspace navigation showing both "Apex Series" and "Order Now" pages](images/04_02_0030.png)
    > *📸 Capture: The workspace navigation or page list showing the new "Order Now" page alongside the existing "Apex Series" page.*

### Summary

The Order Now page is created. Next you will add the pre-order cards and wire them into a Guided Experience flow.

---

## Exercise 4.3 Assemble the Pre-Order Guided Experience

You will add the four Apex pre-order cards to the Order Now page and configure them as a sequential Guided Experience — a wizard that guides the dealer step-by-step through the pre-order process.

1. On the **Order Now** page, click **Add Widget** or **Add Card** to open the card picker.

    ![Order Now page in edit mode with the Add Widget or Add Card option visible](images/04_03_0010.png)
    > *📸 Capture: The Order Now page in edit mode — empty, with a clear call to action to add a widget or card.*

2. From the card picker, select the **Guided Experience** widget type.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact name of the Guided Experience widget in the page editor and the steps to configure it (e.g., does it function as a container for cards, or are individual cards sequenced separately?). Update steps 2–6 accordingly based on the actual product behavior.

    ![Card or widget picker with the Guided Experience option selected](images/04_03_0020.png)
    > *📸 Capture: The widget/card picker showing the Guided Experience widget option highlighted or selected.*

3. In the Guided Experience configuration, add **Step 1** and assign the **Apex - Model Selection** card.

    ![Guided Experience configuration showing Step 1 with the Apex - Model Selection card assigned](images/04_03_0030.png)
    > *📸 Capture: The Guided Experience step configuration panel showing Step 1 labeled and the Model Selection card assigned to it.*

4. Add **Step 2** and assign the **Apex - Configuration & Quantity** card.

    ![Guided Experience configuration showing Step 2 with the Apex - Configuration & Quantity card assigned](images/04_03_0040.png)
    > *📸 Capture: The step configuration panel showing Step 2 with the Configuration & Quantity card assigned.*

5. Add **Step 3** and assign the **Apex - Pricing & Discount Review** card.

    > [!NOTE]
    > Step 3 is the key moment for Document Grounding. The Pricing & Discount Review card shows the dealer their calculated discount. Dealers who want to understand how the discount was calculated can open Joule alongside the wizard and ask a question — Joule will answer from the Pre-Order Discount Policy document without the dealer leaving this page.

    ![Guided Experience configuration showing Step 3 with the Apex - Pricing & Discount Review card assigned](images/04_03_0050.png)
    > *📸 Capture: The step configuration panel showing Step 3 with the Pricing & Discount Review card assigned. A note or tooltip referencing the Joule assistant capability on this step would be ideal to capture if visible in the UI.*

6. Add **Step 4** and assign the **Apex - Pre-Order Confirmation** card.

    ![Guided Experience configuration showing all four steps configured](images/04_03_0060.png)
    > *📸 Capture: The full Guided Experience configuration showing all four steps in sequence: Model Selection → Configuration & Quantity → Pricing & Discount Review → Pre-Order Confirmation.*

7. Preview the assembled Guided Experience to verify the four-step flow is correct.

    ![Preview of the Guided Experience wizard showing Step 1 - Model Selection](images/04_03_0070.png)
    > *📸 Capture: The Guided Experience preview — Step 1 (Model Selection) with the three Apex model cards (City / Trail / Pro) visible, each with a product image. A step indicator at the top should show "Step 1 of 4".*

### Summary

The four-step pre-order wizard is assembled. You are ready to publish the Order Now page.

---

## Exercise 4.4 Publish the Order Now Page

With the Guided Experience configured, you will publish the Order Now page to make it available to dealers.

1. Click **Save** to save the current page configuration.

2. Click **Publish** to make the **Order Now** page live in the dealer portal.

    > [!IMPORTANT]
    > **TODO:** Confirm the publish/save workflow for pages in this version of SAP Build Work Zone — is there a draft/publish distinction, or does saving automatically publish? Update steps accordingly.

    ![Order Now page published confirmation](images/04_04_0010.png)
    > *📸 Capture: The confirmation message or updated page state showing the Order Now page is published and accessible.*

3. Navigate to the workspace as a member (not as admin) to verify the **Order Now** page appears in the workspace navigation alongside **Apex Series**.

    ![Dealer-facing view of the workspace showing both "Apex Series" and "Order Now" in the navigation](images/04_04_0020.png)
    > *📸 Capture: The workspace as seen by a member — showing the workspace navigation with "Apex Series" and "Order Now" tabs or menu items. This is the final admin view before the persona switch in Exercise 5.*

### Summary

The **Order Now** page is published and the dealer portal is complete. You have built everything the BestRun EV dealer portal needs:

- A branded Apex Series product page with AI-generated content
- Document Grounding with five product documents
- A four-step pre-order Guided Experience

It is time to switch personas — in Exercise 5, you become the dealer.

Continue to — [Exercise 5 - Experience the Portal as a Dealer](../ex5/README.md)
