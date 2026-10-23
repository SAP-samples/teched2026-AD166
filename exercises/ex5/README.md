# Exercise 5 - Access the Dealer Portal from Joule Work (Optional)

> [!NOTE]
> This exercise is optional. You will need a smartphone (iOS or Android) to complete it.

SAP Build Work Zone content can be accessed not only from a desktop browser, but also from the native mobile app **Joule Work**, available on iOS and Android. In this exercise you access the BestRun EV Dealer Portal from the app and ask Joule a grounded product question, just as a dealer in the field would.

## Exercise 5.1 Set Up Joule Work

### Install the app

The download may take a moment depending on network conditions — start it now and continue with the next steps on the desktop while the app installs.

1. On your smartphone, go to the app store for your platform and install **Joule Work**. Scan the QR code for your device:

    <img src="images/05_01_download.png" alt="App Store and Google Play badges with QR codes for downloading Joule Work" width="600">

> [!NOTE]
> If you already have Joule Work installed and connected to another environment, you can still use it here. You can switch the connected environment from your user profile screen inside the app (+ Add New Environment)

### Generate the registration QR code (on the desktop)

2. In SAP Build Work Zone, click your **user avatar** in the top right of the shell bar, then click **Settings**.

    <img src="images/05_01_0010.png" alt="User avatar menu open with Settings option highlighted" width="800" height="435">

3. In the Settings panel, select **Joule Work Mobile App**.

    <img src="images/05_01_0020.png" alt="Settings panel with Joule Work Mobile App selected, showing the Install and Register tabs" width="800" height="438">

4. Click the **Register** tab. The QR code to register the app changes - this is the one you will scan from the phone in the next step.

    <img src="images/05_01_0030.png" alt="Joule Work Mobile App settings with the Register tab active and the registration QR code visible" width="800" height="438">

### Connect the app to the landscape (on your phone)

5. Open **Joule Work** on your smartphone.

    - **Fresh install:** tap **Scan QR Code**. Follow any on-screen permission prompts — allow **camera access** when asked (required to scan the QR code), and allow **push notifications** if you wish. You can change these permissions later in your device's settings.

    - **Already connected to another environment:** sign out and tap **Switch Environment** at the bottom of the screen, then scan the QR code from the next step.

    <img src="images/05_01_0040.png" alt="Joule Work splash screen on a fresh install, showing the Scan QR Code button" width="500" height="1045">

6. Scan the QR code displayed on the desktop screen. The app shows a **Confirmation** screen — *"Scan succeeded. You will be connected to: jw164-djmbomr8..."*. Tap **Continue**.

    <img src="images/05_01_0050.png" alt="Confirmation screen after scanning — Scan succeeded, Continue button" width="500" height="1053">

7. Sign in with your participant credentials (**AD166-XXX**).

    <img src="images/05_01_0060.png" alt="SAP Build Work Zone login screen on the phone with Email or User Name and Password fields" width="500" height="1053">

8. After signing in, Joule Work opens the **Start** tab. This is your home screen in the app. Notice the **bottom tab bar** with four tabs: **Start**, **Joule**, **Workspaces**, and **Apps** — you will use these to navigate the app in the next exercises.

    <img src="images/05_01_0070.png" alt="Joule Work Start tab after sign-in, showing the bottom tab bar with Start, Joule, Workspaces, and Apps" width="500" height="1046">

### Summary

Joule Work is installed and connected to the session landscape. You are ready to access the BestRun EV Dealer Portal from your phone.

---

## Exercise 5.2 Access the BestRun EV Dealer Portal

1. Tap the **Workspaces** tab in the bottom bar. Your **BestRun EV Dealer Portal XXX** workspace appears in the **Recently Visited** list.

    <img src="images/05_02_0010.png" alt="Joule Work Workspaces tab showing BestRun EV Dealer Portal in the Recently Visited list" width="500" height="1053">

2. Tap **BestRun EV Dealer Portal XXX** to open it. The portal loads in a web view showing the Overview page — the hero banner, workspace header (Private, Members, External), and the Apex Series announcement below.

    <img src="images/05_02_0020.png" alt="BestRun EV Dealer Portal Overview page open in Joule Work" width="500" height="1053">

3. Scroll through the **Overview page** to see the launch content — the product descriptions for Apex City, Apex Trail, and Apex Pro, and the brochure carousel below.

    <img src="images/05_02_0030.png" alt="Apex Series page in mobile layout showing product descriptions and brochure carousel" width="500" height="1053">

4. If you completed the optional **Guided Experience** (Exercise 4), navigate to the **Apex Pre-Order** page and confirm the wizard is accessible on mobile — the step-by-step cards render correctly on a phone screen.

> [!NOTE]
> This step only applies if you built the Guided Experience in Exercise 4.

<img src="images/05_02_0040.png" alt="Apex Series Pre-Order Guided Experience wizard open on mobile, showing Step 1 — Choose Your Models" width="500" height="1053">

### Summary

The dealer portal is fully accessible on mobile. The content and navigation all work in Joule Work. In the final step, you will use Joule from the mobile app.

---

## Exercise 5.3 Ask Joule a Question from Your Phone

1. Tap the **Joule** tab in the bottom bar (the second tab, between Start and Workspaces). Joule opens with a **"What's up?"** prompt and a **Message Joule** input bar at the bottom.

    <img src="images/05_03_0010.png" alt="Joule tab open in Joule Work, showing the What's up? prompt and Message Joule input bar" width="500" height="1053">

2. Tap **Message Joule** and type the following question, then send it:

    ```
    What color options are available for the Apex Trail?
    ```

    Joule answers directly from the portal's product documents: *"The Apex Trail model is available in Forest Green, Slate Grey, and Burnt Orange."* Notice the **Sources 1** badge — the answer is grounded in the content you published in Exercise 3, not generated from general knowledge.

    <img src="images/05_03_0020.png" alt="Joule's grounded answer on mobile: Apex Trail colors with Sources 1 badge" width="500" height="1053">

3. Tap **Sources 1** to verify the citation links back to the Apex Series page in your dealer portal.

### Summary

You have completed all exercises. You have experienced the BestRun EV Dealer Portal across both desktop and mobile — as the admin who built it, and as the dealer who uses it.

---

## Session Complete

> **Congratulations!** :clap: :clap: - 
> you have completed **AD166: Experience AI-enabled business sites with SAP Build Work Zone**.

Here is what you built and explored in this session:

| Exercise | What you did |
|---|---|
| **0** | Learned the scenario and explored a sample workspace |
| **1** | Used Joule to create the dealer portal workspace, made it private & external, and added your dealer alias |
| **2** | Built the generic portal content — hero, Key Highlights, and self-service cards — then experienced it as a dealer |
| **3** | Created the Apex Series product launch page and asked Joule a grounded product question as a dealer |
| **4** | *(Optional)* Assembled a Guided Experience wizard |
| **5** | *(Optional)* Accessed the portal from Joule Work |

## Further Resources

- [SAP Build Work Zone on SAP Community](https://pages.community.sap.com/topics/work-zone)
- [Documentation for SAP Build Work Zone, advanced edition](https://help.sap.com/docs/WZ)
- [Joule documentation](https://help.sap.com/docs/joule)
- [SAP Build Work Zone, advanced edition on Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-build-work-zone-advanced-edition?service_plan=advanced&region=all&commercialModel=btpea)
