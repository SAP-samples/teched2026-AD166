# Exercise 1 - Set Up the Dealer Portal with Joule

In this exercise, you take on the role of the **Digital Experience Manager at BestRun EV**. You will use Joule to create the dealer portal workspace, add the first team members, and configure it as an external-facing portal accessible to the dealer network.

By the end of this exercise, you will have a live workspace ready to receive content.

## Exercise 1.1 Open Joule and Access SAP Build Work Zone

Joule is available directly within SAP Build Work Zone — no BTP cockpit access is needed. You will log in to the Work Zone site, open Joule, and navigate to the workspace administration console.

1. Open the SAP Build Work Zone URL provided on your desk card and log in with your participant credentials.

    > [!IMPORTANT]
    > **TODO:** Add the SAP Build Work Zone site URL once the landscape is provisioned.

    ![SAP Build Work Zone site home screen after login](images/01_01_0010.png)
    > *📸 Capture: The SAP Build Work Zone home screen as it appears immediately after participant login — showing the site launchpad or home page.*

2. Click the **Joule** icon in the Work Zone interface to open the Joule panel.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact location of the Joule entry point within SAP Build Work Zone (e.g., top navigation bar icon, floating button, or menu item).

    ![Joule panel open within SAP Build Work Zone](images/01_01_0020.png)
    > *📸 Capture: The Joule side panel open within SAP Build Work Zone — showing the chat interface and a welcome/greeting prompt. The Work Zone page should be visible behind the panel.*

3. Navigate to the **Administration Console** of SAP Build Work Zone.

    > [!IMPORTANT]
    > **TODO:** Confirm the navigation path to the Administration Console from the Work Zone home screen (e.g., user menu → Administration Console, or a direct tile/link on the home page).

    ![SAP Build Work Zone Administration Console home screen](images/01_01_0030.png)
    > *📸 Capture: The SAP Build Work Zone Administration Console — showing the main admin dashboard. This is the starting point for workspace creation in the next step.*

### Summary

You are logged in to SAP Build Work Zone and the Joule panel is open. Continue to the next step to create your workspace.

---

## Exercise 1.2 Create the BestRun EV Dealer Portal Workspace

You will now use Joule to create a new workspace for the BestRun EV dealer network. Using a natural language prompt, Joule will guide you through the workspace creation process.

1. With the Joule panel open, type the following prompt:

    ```
    Create a new workspace called BestRun EV Dealer Portal
    ```

    ![Joule responding with workspace creation options or a confirmation card](images/01_02_0010.png)
    > *📸 Capture: Joule's response after the create workspace prompt — showing a confirmation card, workspace template selection, or creation form pre-filled with the name.*

2. Joule presents workspace template options. Select the **External Portal** template (or the template most suited to a B2B dealer portal).

    > [!IMPORTANT]
    > **TODO:** Confirm the exact template name available for external-facing workspaces in the landscape. Update the template name above and the screenshot description accordingly.

    ![Template selection screen showing available workspace templates](images/01_02_0020.png)
    > *📸 Capture: The workspace template selection screen or Joule's prompt for template choice, with the external/portal template option highlighted.*

3. Confirm the workspace name **BestRun EV Dealer Portal XXX** (replace `XXX` with your participant number) and click **Create** or confirm via Joule.

    ![Workspace creation confirmation screen showing the workspace name and settings](images/01_02_0030.png)
    > *📸 Capture: The final creation confirmation step — workspace name field pre-filled, template confirmed, ready to create.*

4. After a few seconds, the new workspace opens. Verify the workspace name appears correctly in the header.

    ![Newly created BestRun EV Dealer Portal workspace, empty, ready to be configured](images/01_02_0040.png)
    > *📸 Capture: The newly created workspace in its initial state — empty pages, no content yet. The workspace name "BestRun EV Dealer Portal XXX" should be visible in the header.*

### Summary

Your workspace is created. Next, you will add your team members.

---

## Exercise 1.3 Add Team Members Using Joule

The BestRun EV regional sales managers need access to the workspace so they can review and contribute content. You will use Joule to add them as workspace members.

1. With the Joule panel open, type the following prompt:

    ```
    Add user AD166-XXX as a member of BestRun EV Dealer Portal XXX
    ```

    > [!IMPORTANT]
    > **TODO:** Confirm the exact Joule prompt format for adding members — specify whether the user identifier is an email address, display name, or user ID, and update the prompt above accordingly.

    ![Joule responding to add member prompt with a confirmation or user search result](images/01_03_0010.png)
    > *📸 Capture: Joule's response to the add member prompt — showing a confirmation card with the user's name and the workspace they are being added to.*

2. Confirm the member addition in the Joule panel.

    ![Member successfully added confirmation in Joule](images/01_03_0020.png)
    > *📸 Capture: Joule's success message confirming the user has been added to the workspace.*

3. Open the workspace **Members** settings to verify the new member appears in the list.

    > [!IMPORTANT]
    > **TODO:** Add navigation path to the workspace members panel (e.g., workspace settings → members, or the admin console path).

    ![Workspace members panel showing the added user](images/01_03_0030.png)
    > *📸 Capture: The workspace Members panel listing the newly added user alongside the workspace owner.*

### Summary

Team members have been added to the workspace using Joule. You are now ready to configure the portal settings.

---

## Exercise 1.4 Configure the Workspace as an External-Facing Portal

By default, a workspace is accessible only to internal users. To make the BestRun EV Dealer Portal accessible to the external dealer network, you need to configure it as an external-facing portal.

1. In the workspace administration view, navigate to **Settings**.

    > [!IMPORTANT]
    > **TODO:** Confirm the exact navigation path to external workspace settings in this version of SAP Build Work Zone advanced edition.

    ![Workspace settings navigation, with the Settings option highlighted](images/01_04_0010.png)
    > *📸 Capture: The workspace overview or admin panel with the Settings menu item clearly visible and selected.*

2. Locate the **Visibility** or **Access** section and enable **External Access**.

    ![Workspace settings screen showing the External Access or Visibility toggle](images/01_04_0020.png)
    > *📸 Capture: The settings panel showing the external access configuration option. The toggle or dropdown should be visible in its default (internal) state.*

3. Enable external access and configure the required settings.

    > [!IMPORTANT]
    > **TODO:** Document the specific fields that need to be configured for external access — e.g., domain allowlist, identity provider settings, invitation mode. Add sub-steps per field.

    ![External access settings configured and enabled](images/01_04_0030.png)
    > *📸 Capture: The settings panel after enabling external access — showing the confirmed configuration with a green indicator or enabled toggle.*

4. Click **Save** to apply the settings.

    ![Settings saved confirmation message or updated workspace state](images/01_04_0040.png)
    > *📸 Capture: The success message or updated settings panel confirming changes were saved.*

### Summary

The workspace is now configured as an external-facing dealer portal. The foundation is in place — move on to Exercise 2 to start building the Apex Series launch content.

Continue to — [Exercise 2 - Build the Apex Series Launch Content with AI](../ex2/README.md)
