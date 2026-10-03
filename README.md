# AD166 - AI at Work: Build a Smart B2B Dealer Portal with SAP Build Work Zone
[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/teched2026-AD166)](https://api.reuse.software/info/github.com/SAP-samples/teched2026-AD166)

> [!IMPORTANT]
> **TODO:** Replace session title above with the official SAP TechEd 2026 session title once confirmed.

<p align="center"><img src="./exercises/images/ad166-banner.png" width="80%" /></p>

> [!IMPORTANT]
> **TODO:** Add the session banner image to `exercises/images/ad166-banner.png`.

## Description

This repository contains the material for the SAP TechEd 2026 session **AD166 - AI at Work: Build a Smart B2B Dealer Portal with SAP Build Work Zone**.

## Overview

In this hands-on session, you take on the role of a Digital Experience Manager at **BestRun EV** — a premium electric mobility company launching a new product line, the **Apex Series**, through its 200+ strong authorized dealer network. Their existing dealer portal is a static website with PDF downloads and a contact form. With the Apex Series launching in 90 days, the team decides to migrate to an AI-powered external portal on **SAP Build Work Zone, advanced edition** — and use it as the launchpad for the new products.

You will build the dealer portal from scratch using Joule, populate it with AI-generated content, ground it with product documents so dealers can get instant answers, and assemble a pre-order guided experience. Midway through the session you switch personas — you become an authorized dealer in Amsterdam experiencing the portal for the first time.

### What you will learn

- How to use **Joule** to create and manage workspaces in SAP Build Work Zone
- How to generate dealer-facing content with **AI-assisted text generation**
- How to configure **Document Grounding** so Joule can answer questions from your own documents
- How to assemble a structured ordering workflow using a **Guided Experience** with pre-built UI cards
- How to use Joule as an **inline assistant** while filling in a form — without leaving the page
- How to access an external workspace from **Joule Work Mobile**

## Requirements

There are no specific technical requirements to follow exercises 1–5. For Exercise 6 (optional), you will need:

- A smartphone (iOS or Android) with **Joule Work Mobile** installed

> [!NOTE]
> For the SAP TechEd 2026 session we have already prepared the landscape with **SAP Build Work Zone, advanced edition**, Joule, and Document Grounding enabled. If following these exercises outside of SAP TechEd 2026, you will need to set up the environment first.

## Exercises

- [Getting Started (Optional)](exercises/ex0/) — Meet BestRun EV, the Apex Series, and the tools you will use today
- [Exercise 1 - Set Up the Dealer Portal with Joule](exercises/ex1/)
    - [Exercise 1.1 - Open Joule and access SAP Build Work Zone](exercises/ex1/README.md#exercise-11-open-joule-and-access-sap-build-work-zone)
    - [Exercise 1.2 - Create the BestRun EV Dealer Portal workspace](exercises/ex1/README.md#exercise-12-create-the-bestrun-ev-dealer-portal-workspace)
    - [Exercise 1.3 - Add team members using Joule](exercises/ex1/README.md#exercise-13-add-team-members-using-joule)
    - [Exercise 1.4 - Configure the workspace as an external-facing portal](exercises/ex1/README.md#exercise-14-configure-the-workspace-as-an-external-facing-portal)
- [Exercise 2 - Build the Apex Series Launch Content with AI](exercises/ex2/)
    - [Exercise 2.1 - Create the Apex Series landing page](exercises/ex2/README.md#exercise-21-create-the-apex-series-landing-page)
    - [Exercise 2.2 - Use AI to draft the launch announcement](exercises/ex2/README.md#exercise-22-use-ai-to-draft-the-launch-announcement)
    - [Exercise 2.3 - Add model overview sections](exercises/ex2/README.md#exercise-23-add-model-overview-sections)
    - [Exercise 2.4 - Generate model copy with AI](exercises/ex2/README.md#exercise-24-generate-model-copy-with-ai)
- [Exercise 3 - Enable Document Grounding](exercises/ex3/)
    - [Exercise 3.1 - Upload product documents to the workspace](exercises/ex3/README.md#exercise-31-upload-product-documents-to-the-workspace)
    - [Exercise 3.2 - Configure Document Grounding](exercises/ex3/README.md#exercise-32-configure-document-grounding)
    - [Exercise 3.3 - Test grounding with a product question](exercises/ex3/README.md#exercise-33-test-grounding-with-a-product-question)
- [Exercise 4 - Add the Pre-Order Guided Experience](exercises/ex4/)
    - [Exercise 4.1 - Find the pre-built Apex pre-order cards](exercises/ex4/README.md#exercise-41-find-the-pre-built-apex-pre-order-cards)
    - [Exercise 4.2 - Create the Order Now page](exercises/ex4/README.md#exercise-42-create-the-order-now-page)
    - [Exercise 4.3 - Assemble the pre-order Guided Experience](exercises/ex4/README.md#exercise-43-assemble-the-pre-order-guided-experience)
    - [Exercise 4.4 - Publish the Order Now page](exercises/ex4/README.md#exercise-44-publish-the-order-now-page)
- [Exercise 5 - Experience the Portal as a Dealer](exercises/ex5/)
    - [Exercise 5.1 - Accept the dealer portal invitation](exercises/ex5/README.md#exercise-51-accept-the-dealer-portal-invitation)
    - [Exercise 5.2 - Explore the Apex Series launch content](exercises/ex5/README.md#exercise-52-explore-the-apex-series-launch-content)
    - [Exercise 5.3 - Ask Joule a product question](exercises/ex5/README.md#exercise-53-ask-joule-a-product-question)
    - [Exercise 5.4 - Use AI to summarize the Battery Technology Guide](exercises/ex5/README.md#exercise-54-use-ai-to-summarize-the-battery-technology-guide)
    - [Exercise 5.5 - Open the pre-order Guided Experience](exercises/ex5/README.md#exercise-55-open-the-pre-order-guided-experience)
    - [Exercise 5.6 - Ask Joule about your pre-order discount](exercises/ex5/README.md#exercise-56-ask-joule-about-your-pre-order-discount)
    - [Exercise 5.7 - Submit your pre-order](exercises/ex5/README.md#exercise-57-submit-your-pre-order)
- [Exercise 6 - Access the Dealer Portal from Joule Work Mobile (Optional)](exercises/ex6/)
    - [Exercise 6.1 - Set up Joule Work Mobile](exercises/ex6/README.md#exercise-61-set-up-joule-work-mobile)
    - [Exercise 6.2 - Access the BestRun EV Dealer Portal](exercises/ex6/README.md#exercise-62-access-the-bestrun-ev-dealer-portal)
    - [Exercise 6.3 - Ask Joule a question from your phone](exercises/ex6/README.md#exercise-63-ask-joule-a-question-from-your-phone)

## System Access

The following systems are used for this hands-on session. Please find your participant number on your desk. Login credentials will be provided by the instructor.

> [!IMPORTANT]
> Make sure to replace `###` throughout the exercises with your participant number.

> [!IMPORTANT]
> **TODO:** Add the SAP Build Work Zone tenant URL once the landscape is provisioned.

| System | URL |
|---|---|
| SAP Build Work Zone | `TODO: https://ad166-XXXXXXXX.workzone.cfapps.eu10.hana.ondemand.com/site` |

> [!NOTE]
> Outside of the hands-on session of SAP TechEd 2026, your own systems will be required to execute the exercises.

## Further Resources

- [SAP Build Work Zone on SAP Community](https://pages.community.sap.com/topics/work-zone)
- [Documentation for SAP Build Work Zone, advanced edition](https://help.sap.com/docs/WZ)
- [SAP Build Work Zone, advanced edition on Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/sap-build-work-zone-advanced-edition?service_plan=advanced&region=all&commercialModel=btpea)
- [Joule documentation](https://help.sap.com/docs/joule)
- [SAP Builders on SAP Community](https://pages.community.sap.com/topics/low-code-no-code)

> [!IMPORTANT]
> **TODO:** Add link to Joule Work Mobile app store pages (iOS / Android) once confirmed for TechEd 2026.

## Code of Conduct

Please read the [SAP Open Source Code of Conduct](https://github.com/SAP-samples/.github/blob/main/CODE_OF_CONDUCT.md).

## How to Obtain Support

Support for the content in this repository is available during the actual time of the online session for which this content has been designed. Otherwise, you may request support via the [Issues](../../issues) tab.

## License

Copyright (c) 2026 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
