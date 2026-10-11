# Exercise 1 - Create the External Dealer Workspace

In this exercise, you take on the role of the **Digital Experience Manager at BestRun EV**. You will use Joule to create the dealer portal workspace from a template, configure it as a private, external-facing portal, and add your dealer alias user so you can experience it later as a dealer.

By the end of this exercise, you will have a live workspace ready to receive content.

## Exercise 1.1 Access Work Zone and Launch Joule

Joule is available directly within SAP Build Work Zone — no BTP cockpit access is needed. You will log in, open Joule, and ask it to show the workspaces you manage to orient yourself.

1. Open the following URL in your browser and log in with your participant credentials:

    **[https://jw164-djmbomr8.workzone.cfapps.eu10.hana.ondemand.com/](https://jw164-djmbomr8.workzone.cfapps.eu10.hana.ondemand.com/)**

    ![SAP Build Work Zone site home screen after login](images/01_01_0010.png)

2. In the top menu bar, click the **<img src="images/JouleIcon.png" width="16" height="16"> Joule icon** to open the Joule panel.

    ![Joule icon in the SAP Build Work Zone top menu bar](images/01_01_0020.png)

3. With the Joule panel open, ask Joule to list the workspaces you manage:

    ```
    Show me my managed workspaces
    ```

    Joule returns the list of workspaces you currently manage. This is a quick way to see what you already have before you create a new one.

    > [!NOTE]
    > **TODO:** Capture a screenshot of Joule responding to the "my managed workspaces" prompt.

### Summary

You are logged in to SAP Build Work Zone, the Joule panel is open, and you have seen your managed workspaces. Continue to the next step to create the dealer portal workspace.

---

## Exercise 1.2 Create the Dealer Portal Workspace from a Template

There are two ways to create a workspace in SAP Build Work Zone — using Joule with a natural language prompt, or through the classical workspace creation UI. Both lead to the same result.

> [!NOTE]
> Replace `XXX` in the workspace name with your assigned participant number (e.g. **005** for participant AD166-005).

---

<details open>
<summary><strong>Option A — Create with Joule (recommended)</strong></summary>

1. With the Joule panel open, type the following prompt:

    ```
    Create a new workspace called "BestRun EV Dealer Portal XXX"
    ```

    ![Joule responding to the create workspace prompt](images/01_02_0010.png)

2. Joule may ask you to select a workspace template. If prompted, select **Partner Portal Template** from the list (click **View More** to locate the correct template).

    > [!NOTE]
    > Joule may skip this step if it selects the template automatically based on your prompt. If no template selection appears, continue to the next step.

    ![Joule template selection showing Partner Portal Template highlighted](images/01_02_0020.png)

3. Joule creates the workspace. Once complete, a **notification appears on the Work Zone home page** with a link to the new workspace. Click the notification link to open **BestRun EV Dealer Portal XXX** in the same tab — this keeps Joule accessible on the right side.

    > [!TIP]
    > Prefer the **notification link** over the link inside the Joule chat panel. The notification opens the workspace in the same tab, keeping the Joule panel visible. The Joule chat link opens a new tab, which closes the panel.

    ![Work Zone home page showing the workspace creation notification with a link](images/01_02_0030.png)

    > [!NOTE]
    > If no notification appears on the home page, open the **Workspaces** menu in the top navigation and browse to **BestRun EV Dealer Portal XXX** from the list of your workspaces.

</details>

---

<details>
<summary><strong>Option B — Create via the Workspaces menu (standard UI)</strong></summary>

1. In the SAP Build Work Zone left navigation menu, expand the **Workspaces** item and click **New Workspace**.

    ![Workspaces menu with New Workspace option highlighted](images/01_02_B_0010.png)

2. In the workspace type dialog, select **Private Workspace**.

    ![Workspace type dialog options](images/01_02_B_0020.png)

3. In the workspace creation dialog, enter the name **BestRun EV Dealer Portal XXX**, select **Partner Portal Template** from the template list, and click **Finish**.

    ![Workspace creation dialog with name and settings filled in](images/01_02_B_0030.png)

4. After a few seconds, the new workspace opens.

    ![Newly created workspace open in the classical UI flow](images/01_02_B_0040.png)

    > [!NOTE]
    > You might need to refresh the workspace to get the cover image from the template.

</details>

---

> [!IMPORTANT]
> As soon as your workspace is created, **notify your instructor**. The instructor needs your workspace name to enable **Document Grounding** for it (used in Exercise 3). Enabling grounding takes time to sync, so flagging it early means it is ready when you reach Exercise 3.

### Summary

Your workspace **BestRun EV Dealer Portal XXX** is created from the Partner Portal Template. Next, you will configure its visibility and external access.

---

## Exercise 1.3 Make the Workspace Private and External

By default a workspace is internal. To make the BestRun EV Dealer Portal a private portal that your external dealer network can be invited into, you configure both the visibility and external access settings in **Edit Workspace**.

1. Inside the workspace, open **Edit Workspace** (More workspace options **'...'** > **Workspace Admin Settings** > **Edit Workspace**).

    ![Edit Workspace open at the General tab](images/01_02_0040.png)

2. Set the **Visibility** to **Private**, then save.

    ![Workspace settings showing the Private visibility option](images/01_02_0041.png)

3. Keep the **Email Notifications** option set to **None** and click **Accept**.

    ![Workspace settings showing the email notification option](images/01_02_0042.png)

4. Still in **Edit Workspace**, locate the **External Users** field and check **"Allow external users to access this workspace and be invited as members"**. This enables external dealer access to your portal.

    ![External Users checkbox enabled in Edit Workspace General tab](images/01_04_0020.png)

5. Click **Save** to apply the settings.

    ![Save button highlighted in Edit Workspace](images/01_04_0030.png)

### Summary

The workspace is now a private, external-facing dealer portal. Next, you will add your dealer alias user as a member.

---

## Exercise 1.4 Add Your Dealer Alias User to the Workspace

Each participant has a dedicated **dealer alias user** — **Dealer-XXX**, matching your participant number (e.g. participant **AD166-005** uses **Dealer-005**). You add this user as a member now so that later, when an exercise asks you to experience the portal as a dealer, you can switch to this alias and already have access.

> [!NOTE]
> Replace `XXX` with your participant number — e.g. if you are **AD166-005**, add **Dealer-005**.

1. With the Joule panel open, type the following prompt:

    ```
    Add user Dealer-XXX as a member of BestRun EV Dealer Portal XXX
    ```

    ![Joule responding to the add member prompt](images/01_03_0010.png)

    > [!NOTE]
    > **TODO:** Recapture this screenshot — it currently shows the previous moderator account instead of the **Dealer-XXX** alias.

2. Confirm the member addition in the Joule panel.

    ![Member successfully added confirmation in Joule](images/01_03_0020.png)

3. Open the workspace **Members** settings and verify that **Dealer-XXX** appears in the members list.

    ![Workspace members panel showing the added Dealer-XXX user](images/01_03_0030.png)

    > [!NOTE]
    > **TODO:** Recapture this screenshot to show **Dealer-XXX** in the members list.

### Summary

Your workspace is created, configured as a private external portal, and your **Dealer-XXX** alias is a member. The foundation is in place — move on to Exercise 2 to start building the portal content.

Continue to — [Exercise 2 - Update the Dealer Workspace Content](../ex2/README.md)
