# Exercise 3 - Enable Document Grounding

In this exercise you upload the BestRun EV product documents to the workspace and enable Document Grounding for it. Document Grounding is already provisioned and connected to SAP Build Work Zone in this landscape — you do not need to set it up from scratch. Your task is to upload the source documents and activate grounding specifically for the **BestRun EV Dealer Portal XXX** workspace.

Once enabled, Joule will answer dealer questions directly from the content of those documents — without requiring dealers to open or search through any file.

## Exercise 3.1 Download the Source Documents

Six documents have been prepared for this session. Download them to your laptop before uploading them to the workspace.

1. Click the link below to download the document package:

    ### [⬇ Download BestRun_EV_Apex_Series_Documents.zip](BestRun_EV_Apex_Series_Documents.zip)

    ![Browser download bar or save dialog showing BestRun_EV_Apex_Series_Documents.zip being saved](images/03_01_0010.png)
    > *📸 Capture: The browser download prompt or the downloaded zip file visible in the browser's download bar or the system Downloads folder.*

2. Locate the downloaded zip file (typically in your **Downloads** folder) and extract it to a folder of your choice on your local drive.

    > [!TIP]
    > Most operating systems let you right-click the zip file and choose an **Extract** or **Unarchive** option. You can also double-click the zip to open it and drag the files to a folder. Choose a location you can easily navigate back to — you will need to select these files one by one in the next step.

    Once extracted, you should have the following six PDF files:

    | # | File | Contents |
    |---|---|---|
    | 1 | `01_Apex_Series_Technical_Spec_Sheet.pdf` | Range, motor, weight, colors, charging times per model |
    | 2 | `02_Apex_Pro_Battery_Drive_Technology_Guide.pdf` | LFP battery system details, charging curve, range calculations |
    | 3 | `03_Dealer_Commercial_Handbook.pdf` | Pricing tiers, dealer margins, ordering process |
    | 4 | `04_Apex_Pre-Order_Discount_Policy.pdf` | Discount matrix by quantity and payment terms, bonus conditions |
    | 5 | `05_After-Sales_Warranty_Guide.pdf` | Warranty terms, service intervals, spare parts |
    | 6 | `06_Apex_Pre-Order_Terms_and_Conditions.pdf` | Pre-order eligibility, cancellation rights, delivery commitments |

### Summary

The documents are on your local drive and ready to upload. Continue to the next step.

---

## Exercise 3.2 Upload Product Documents to the Workspace

You will upload all six documents to the workspace so that Document Grounding can index them.

1. In the workspace, navigate to the **Documents** section or the content area where files can be uploaded.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact navigation path to the document upload area in SAP Build Work Zone advanced edition for use with Document Grounding. This may be a dedicated Knowledge Base section or a Documents folder within the workspace.

    ![Workspace documents or knowledge base section, ready for file upload](images/03_02_0010.png)
    > *📸 Capture: The documents section or knowledge base area of the workspace. An upload button or drag-and-drop zone should be visible.*

2. Upload the first document: **01_Apex_Series_Technical_Spec_Sheet.pdf**.

    ![File upload dialog or drag-and-drop area with the spec sheet file selected](images/03_02_0020.png)
    > *📸 Capture: The upload dialog or area showing the Apex Series Technical Spec Sheet file selected or in progress.*

3. Repeat for all remaining five documents. When complete, verify that all six documents appear in the list.

    ![Documents section showing all six Apex Series documents uploaded successfully](images/03_02_0030.png)
    > *📸 Capture: The documents list showing all six uploaded files with upload status confirmed (e.g., green checkmarks or status indicators).*

### Summary

All source documents are uploaded. You are ready to enable Document Grounding.

---

## Exercise 3.3 Configure Document Grounding

Document Grounding is already available in the landscape. In this step you enable it for your workspace and confirm that the uploaded documents are included in the grounding scope.

1. Open the workspace **Settings** and navigate to the **AI** or **Document Grounding** section.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact location of the Document Grounding settings within a workspace in this version of SAP Build Work Zone advanced edition (e.g., workspace settings → AI, or a dedicated Knowledge Base / Grounding panel).

    ![Workspace settings open at the Document Grounding section](images/03_03_0010.png)
    > *📸 Capture: The workspace settings panel showing the Document Grounding configuration section. The section should indicate Document Grounding is available (the service is pre-configured) but not yet enabled for this workspace.*

2. Enable **Document Grounding** for the workspace.

    ![Document Grounding toggle switched to enabled](images/03_03_0020.png)
    > *📸 Capture: The Document Grounding toggle or setting in its enabled state, with a confirmation message visible.*

3. Confirm that all six uploaded documents are included in the grounding scope.

    > [!IMPORTANT]
    > **TODO:** Confirm whether grounding scope is configured per document, per folder, or applied automatically to all workspace documents. Update this step accordingly.

    ![Grounding scope showing all six documents included](images/03_03_0030.png)
    > *📸 Capture: The grounding scope configuration showing all six BestRun EV documents selected or confirmed as included.*

4. Save the settings.

    ![Document Grounding enabled and saved — workspace is now grounded](images/03_03_0040.png)
    > *📸 Capture: Confirmation that settings were saved — Document Grounding shown as active for the workspace.*

### Summary

Document Grounding is active for the workspace. Joule can now draw from the uploaded documents when answering questions in this workspace.

---

## Exercise 3.4 Test Grounding with a Product Question

Before handing off to Exercise 4, you will verify that Document Grounding is working by asking Joule a question that can only be answered from one of the uploaded documents.

1. Open the Joule panel from within the workspace.

    ![Joule panel opening within the BestRun EV Dealer Portal workspace](images/03_04_0010.png)
    > *📸 Capture: The Joule panel open within the workspace context — showing the workspace name is visible in the Joule header or context indicator, confirming Joule is operating in the grounded workspace scope.*

2. Ask the following question:

    ```
    What is the maximum range of the Apex Pro in eco mode?
    ```

    ![Joule returning an answer about the Apex Pro range sourced from the Technical Spec Sheet](images/03_04_0020.png)
    > *📸 Capture: Joule's response to the range question — the answer should include the specific range figure (200 km) and a source citation or reference indicator showing it came from the uploaded document.*

3. Verify that Joule's answer includes a **source reference** pointing to the uploaded document.

    > [!NOTE]
    > A correctly grounded answer will show a citation, a document reference link, or a footnote indicating which uploaded document the answer was drawn from. If Joule answers without a source reference, grounding may not be correctly configured — revisit Exercise 3.3.

    ![Joule answer with source citation highlighted — reference to the spec sheet document visible](images/03_04_0030.png)
    > *📸 Capture: A close-up of the source citation in Joule's answer, showing the document name and optionally a page or section reference.*

4. Ask a second test question to verify another document is grounded:

    ```
    What is the maximum pre-order discount I can get on the Apex Pro?
    ```

    ![Joule returning the Apex Pro discount cap from the Pre-Order Discount Policy with a source citation](images/03_04_0040.png)
    > *📸 Capture: Joule's response citing the Pre-Order Discount Policy as the source. The answer should mention the 10% cap for Apex Pro units.*

### Summary

Document Grounding is working correctly. Joule returns precise, sourced answers from the uploaded documents. Dealers will be able to use this capability in Exercise 5 — without needing to open any document directly.

Continue to — [Exercise 4 - Add the Pre-Order Guided Experience](../ex4/README.md)
