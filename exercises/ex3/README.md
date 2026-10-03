# Exercise 3 - Enable Document Grounding

In this exercise you upload the BestRun EV product documents to the workspace and enable Document Grounding for it. Document Grounding is already provisioned and connected to SAP Build Work Zone in this landscape — you do not need to set it up from scratch. Your task is to upload the source documents and activate grounding specifically for the **BestRun EV Dealer Portal XXX** workspace.

Once enabled, Joule will answer dealer questions directly from the content of those documents — without requiring dealers to open or search through any file.

## Exercise 3.1 Upload Product Documents to the Workspace

The following documents have been prepared for this session and are available in the provided materials folder. You will upload all of them to the workspace.

| # | Document | Purpose |
|---|---|---|
| 1 | Apex Series Technical Spec Sheet | Range, motor, weight, colors, charging times per model |
| 2 | Apex Pro Battery & Drive Technology Guide | LFP battery system details, charging curve, range calculations |
| 3 | Dealer Commercial Handbook | Pricing tiers, dealer margins, ordering process |
| 4 | Apex Pre-Order Discount Policy | Discount matrix by quantity and payment terms, bonus conditions |
| 5 | After-Sales & Warranty Guide | Warranty terms, service intervals, spare parts |

> [!IMPORTANT]
> **TODO:** Confirm the file format for the source documents (PDF is most likely). Confirm where participants find the documents — shared folder on the desktop, downloadable from the repo, or pre-loaded somewhere in the landscape.

1. In the workspace, navigate to the **Documents** section or the content area where files can be uploaded.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact navigation path to the document upload area in SAP Build Work Zone advanced edition for use with Document Grounding. This may be a dedicated Knowledge Base section or a Documents folder within the workspace.

    ![Workspace documents or knowledge base section, ready for file upload](images/03_01_0010.png)
    > *📸 Capture: The documents section or knowledge base area of the workspace. An upload button or drag-and-drop zone should be visible.*

2. Upload the first document: **Apex Series Technical Spec Sheet**.

    ![File upload dialog or drag-and-drop area with the spec sheet file selected](images/03_01_0020.png)
    > *📸 Capture: The upload dialog or area showing the Apex Series Technical Spec Sheet file selected or in progress.*

3. Repeat for all remaining documents. When complete, verify that all five documents appear in the list.

    ![Documents section showing all five Apex Series documents uploaded successfully](images/03_01_0030.png)
    > *📸 Capture: The documents list showing all five uploaded files — spec sheet, battery guide, commercial handbook, discount policy, warranty guide — with upload status confirmed (e.g., green checkmarks or status indicators).*

### Summary

All source documents are uploaded. You are ready to enable Document Grounding.

---

## Exercise 3.2 Configure Document Grounding

Document Grounding is already available in the landscape. In this step you enable it for your workspace and confirm that the uploaded documents are included in the grounding scope.

1. Open the workspace **Settings** and navigate to the **AI** or **Document Grounding** section.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact location of the Document Grounding settings within a workspace in this version of SAP Build Work Zone advanced edition (e.g., workspace settings → AI, or a dedicated Knowledge Base / Grounding panel).

    ![Workspace settings open at the Document Grounding section](images/03_02_0010.png)
    > *📸 Capture: The workspace settings panel showing the Document Grounding configuration section. The section should indicate Document Grounding is available (the service is pre-configured) but not yet enabled for this workspace.*

2. Enable **Document Grounding** for the workspace.

    ![Document Grounding toggle switched to enabled](images/03_02_0020.png)
    > *📸 Capture: The Document Grounding toggle or setting in its enabled state, with a confirmation message visible.*

3. Confirm that all five uploaded documents are included in the grounding scope.

    > [!IMPORTANT]
    > **TODO:** Confirm whether grounding scope is configured per document, per folder, or applied automatically to all workspace documents. Update this step accordingly.

    ![Grounding scope showing all five documents included](images/03_02_0030.png)
    > *📸 Capture: The grounding scope configuration showing all five BestRun EV documents selected or confirmed as included.*

4. Save the settings.

    ![Document Grounding enabled and saved — workspace is now grounded](images/03_02_0040.png)
    > *📸 Capture: Confirmation that settings were saved — Document Grounding shown as active for the workspace.*

### Summary

Document Grounding is active for the workspace. Joule can now draw from the uploaded documents when answering questions in this workspace.

---

## Exercise 3.3 Test Grounding with a Product Question

Before handing off to Exercise 4, you will verify that Document Grounding is working by asking Joule a question that can only be answered from one of the uploaded documents.

1. Open the Joule panel from within the workspace.

    ![Joule panel opening within the BestRun EV Dealer Portal workspace](images/03_03_0010.png)
    > *📸 Capture: The Joule panel open within the workspace context — showing the workspace name is visible in the Joule header or context indicator, confirming Joule is operating in the grounded workspace scope.*

2. Ask the following question:

    ```
    What is the maximum range of the Apex Pro in eco mode?
    ```

    ![Joule returning an answer about the Apex Pro range sourced from the Technical Spec Sheet](images/03_03_0020.png)
    > *📸 Capture: Joule's response to the range question — the answer should include the specific range figure (from the spec sheet) and a source citation or reference indicator showing it came from the uploaded document.*

3. Verify that Joule's answer includes a **source reference** pointing to the uploaded document.

    > [!NOTE]
    > A correctly grounded answer will show a citation, a document reference link, or a footnote indicating which uploaded document the answer was drawn from. If Joule answers without a source reference, grounding may not be correctly configured — revisit Exercise 3.2.

    ![Joule answer with source citation highlighted — reference to "Apex Series Technical Spec Sheet" visible](images/03_03_0030.png)
    > *📸 Capture: A close-up of the source citation in Joule's answer, showing the document name and optionally a page or section reference.*

4. Ask a second test question to verify another document is grounded:

    ```
    What is the dealer margin for the Apex Trail?
    ```

    ![Joule returning the dealer margin from the Dealer Commercial Handbook with a source citation](images/03_03_0040.png)
    > *📸 Capture: Joule's response to the margin question, citing the Dealer Commercial Handbook as the source. The specific margin percentage should be included in the answer.*

### Summary

Document Grounding is working correctly. Joule returns precise, sourced answers from the uploaded documents. Dealers will be able to use this capability in Exercise 5 — without needing to open any document directly.

Continue to — [Exercise 4 - Add the Pre-Order Guided Experience](../ex4/README.md)
