# Exercise 3 - Enable Document Grounding

In this exercise you upload the BestRun EV product documents to the workspace and enable Document Grounding for it. Document Grounding is already provisioned and connected to SAP Build Work Zone in this landscape — you do not need to set it up from scratch. Your task is to upload the source documents and activate grounding specifically for the **BestRun EV Dealer Portal XXX** workspace.

Once enabled, Joule will answer dealer questions directly from the content of those documents — without requiring dealers to open or search through any file.

## Exercise 3.1 Download the Source Documents

Six documents have been prepared for this session. Download them to your laptop before uploading them to the workspace.

1. Click the link below. It opens the GitHub file page for the zip archive.

    ### [⬇ Download BestRun_EV_Apex_Series_Documents.zip](BestRun_EV_Apex_Series_Documents.zip)

2. On the GitHub file page, click the **download** icon (↓) in the top-right corner of the file view to save the zip to your local machine.

    ![GitHub file page for BestRun_EV_Apex_Series_Documents.zip with the download icon highlighted](images/03_01_0010.png)

3. Locate the downloaded zip file (typically in your **Downloads** folder) and extract it to a folder of your choice on your local drive.

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

1. In the workspace, click the **Content** tab in the navigation bar.

    ![Workspace navigation bar with the Content tab highlighted](images/03_02_0010.png)

2. Click the **Upload File** button in the top-right of the Content section. This opens your operating system's file selection dialog.

    ![Content section showing the Upload File button highlighted](images/03_02_0020.png)

3. In the file picker, navigate to the folder where you extracted the zip archive. Select all six PDF files at once, then click **Open**.

    > [!TIP]
    > On most operating systems you can select all files at once by pressing **Ctrl+A** (Windows/Linux) or **Cmd+A** (macOS) after opening the folder, or by clicking the first file and then **Shift-clicking** the last one.

    ![File picker showing all six Apex Series PDF files selected](images/03_02_0030.png)

4. An **Upload Files** dialog appears, listing the selected files under **Upload To: Content**. Click **Upload** to start the transfer. The upload may take a minute — wait for it to complete before continuing.

    ![Upload Files dialog with the files queued and the Upload button highlighted](images/03_02_0040.png)

5. Once complete, all six PDF files appear in the Content list alongside the existing Overview page.

    ![Content section listing all six uploaded Apex Series PDF files](images/03_02_0050.png)

### Summary

All source documents are uploaded. Notify your instructor that your uploads are complete, then continue to Exercise 3.3.

---

## Exercise 3.3 Enable Document Grounding for the Workspace (Instructor-Led)

> [!NOTE]
> **TechEd session participants:** You do not have workspace admin access and **cannot perform this step yourself**. Your instructor will enable Document Grounding for all participant workspaces during the session. The admin configuration will be shown on the projector so you can follow along. **Once the instructor confirms grounding is active, move on to Exercise 3.4.**

Document Grounding in SAP Build Work Zone advanced edition is activated per workspace by designating it as an **AI Source**. This tells the BTP Document Grounding Service (DGS) to index the content of that workspace and make it available for Joule to draw from.

<details>
<summary>&#9654;&nbsp; Admin configuration walkthrough (shown on projector)</summary>

<br>

1. Click the **user profile avatar** (initials circle) in the top-right corner of SAP Build Work Zone **(1)**, then click **Administration Console (2)**.

    ![User profile menu open showing the Administration Console option highlighted](images/03_03_0010.png)

2. In the Administration Console, expand **Area & Workspace Configuration (1)** in the left navigation and click **Workspaces (2)**. On the right panel, switch to the **All Workspaces (3)** tab. Use the search box to filter by workspace name and locate the **BestRun EV Dealer Portal XXX** row — the **Document Grounding** column shows **-** (not yet enabled). Click **Actions (5)** for that row and select **Enable as AI source (6)**.

    ![Administration Console — Workspaces Management with the Actions menu open and Enable as AI source highlighted](images/03_03_0020.png)

3. Once enabled, the **Document Grounding** column for the workspace shows the **AI Source** badge, confirming that DGS will index the uploaded content on its next sync cycle.

    ![Workspaces Management list showing the AI Source badge in the Document Grounding column for BestRun EV Dealer Portal](images/03_03_0030.png)

</details>


### About the Sync Timing

> [!IMPORTANT]
> The BTP Document Grounding Service syncs workspace content into its vector store on a scheduled cron interval. The minimum configurable interval is **1 hour** — meaning after AI Source is enabled, it can take up to an hour before Joule can answer questions from the uploaded documents.
>
> **For this TechEd session:** The instructor will manually trigger the DGS ingestion pipeline every **5–10 minutes** using the DGS pipeline APIs, so documents you uploaded in Exercise 3.2 will be indexed quickly. You do not need to wait. The instructor will confirm on the projector when ingestion is complete and grounding is ready.

### Summary

Document Grounding is being activated by the instructor. Wait for the go-ahead before continuing. Once confirmed, Joule will be able to draw answers from the six uploaded documents.

---

> [!NOTE]
> **Working in your own environment?** If you have workspace admin access and are running this exercise outside the TechEd session, expand the **Admin configuration walkthrough** above and follow those steps to enable AI Source for your workspace. After saving, allow up to **1 hour** for the first sync cycle to complete before proceeding to Exercise 3.4. You can also trigger an on-demand ingestion run via the [DGS pipeline API](https://help.sap.com/docs/document-grounding) if you need faster results.

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
