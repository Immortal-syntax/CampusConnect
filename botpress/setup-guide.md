# Botpress Cloud Setup Guide – CampusConnect AI

> **Scope:** Manual Step-by-Step Guide for Creating, Configuring, and Publishing the CampusConnect AI Botpress Agent  
> **Status:** Configuration Blueprint (To be performed manually in your Botpress Cloud dashboard)  
> **Notice:** These configuration steps must be executed by you inside [Botpress Cloud](https://cloud.botpress.com/). They have **not** been performed automatically.

---

## Prerequisites
1. A web browser with access to [https://cloud.botpress.com/](https://cloud.botpress.com/).
2. A free Botpress Cloud account.
3. The local files created in this repository:
   - `knowledge-base/campusconnect-student-guide.md`
   - `botpress/agent-instructions.md`
   - `botpress/test-cases.md`

---

## Step 1: Create a New Bot in Botpress Cloud

1. Log in to your [Botpress Cloud Dashboard](https://cloud.botpress.com/).
2. Click the **"Create Bot"** button in your workspace.
3. When prompted for a template, select **"Start from Scratch"** (or **"Blank Bot"**).
4. In the bot settings panel:
   - **Bot Name:** `CampusConnect AI`
   - **Bot Description:** `Generative AI Student Assistance Chatbot advancing UN SDG`
5. Click **"Open in Studio"** to launch the visual workflow canvas.

---

## Step 2: Configure the Autonomous Node

1. In the central canvas of Botpress Studio, open the **Main** workflow (`main.flow.json`).
2. If your template starts with a standard conversational card, right-click on the canvas and add an **Autonomous Node** (or AI Agent / LLM Node).
3. Connect the **Start** trigger to the entry point of your Autonomous Node.
4. Click on the Autonomous Node to open the **Inspector Panel** on the right side of the screen.

---

## Step 3: Paste Agent Instructions

1. Open [`botpress/agent-instructions.md`](file:///D:/Projects/CampusConnect/botpress/agent-instructions.md) on your computer.
2. Copy the text inside Section 3 (**Ready-to-Paste Botpress Autonomous Node Prompt**):
   ```text
   You are CampusConnect AI Assistant, an empathetic, knowledgeable, and reliable university academic mentor advancing UN SDG: Quality Education.
   ...
   ```
3. In Botpress Studio, locate the **"Instructions"** (or **"Personality Prompt"**) field in the Autonomous Node's Inspector panel.
4. Paste the instructions directly into this field.
5. Set the model to the default recommended LLM (e.g., **GPT-4o mini** or Botpress default AI engine).

---

## Step 4: Create a Knowledge Base

1. In the far-left vertical navigation bar of Botpress Studio, click the **Knowledge Base** icon (represented by an open book or stacked layers).
2. Click the **"+ New Knowledge Base"** button.
3. Set the knowledge base title to:
   - **Name:** `CampusConnect Student Guide`
   - **Description:** `Curated university study techniques, exam preparation, time management, and learning resources.`

---

## Step 5: Upload the Student Guide

1. Inside your new Knowledge Base, click **"Add Source"** and choose **"Documents / File Upload"**.
2. Select and upload the file from your local workspace:
   `D:\Projects\CampusConnect\knowledge-base\campusconnect-student-guide.md`
   *(You may also optionally upload `academic-policies.md` and `library-and-learning-resources.md`).*
3. Wait 15–30 seconds while Botpress vectorizes and chunks the document.
4. Verify that the file status indicator turns **Green** (indicating `"Indexed"` / `"Ready"`).

---

## Step 6: Connect the Knowledge Base to the Autonomous Node

1. Return to the **Main Workflow** canvas.
2. Click on the **Autonomous Node** to reopen its right-hand Inspector panel.
3. Under the **"Knowledge Base"** or **"Sources"** section:
   - Ensure the toggle switch for **"Enable Knowledge Bases"** is turned **ON**.
   - Select `CampusConnect Student Guide` as an active knowledge source.
4. In the **"Search Mode"** setting, select **Hybrid** or **Vector Search** (default).

---

## Step 7: Test the Agent in the Studio Emulator

Before publishing, validate the assistant using the interactive **Emulator** on the right side of Botpress Studio:

1. **Test Normal Study Query:**
   - Type: *"What is active recall and how do I use it?"*
   - Verify: The bot explains retrieval practice and closed-book methods from the student guide.
2. **Test Open Learning Platform Query:**
   - Type: *"Where can I find free engineering courses on SWAYAM or NPTEL?"*
   - Verify: The bot references SWAYAM and NPTEL with context on government accreditation.
3. **Test Boundary / Unknown Administrative Query:**
   - Type: *"When is the final exam date for CS101 in our college?"*
   - Verify: The bot **refuses to invent dates**, clearly states that exam timetables vary by college, and directs you to your college student portal or registrar.
4. Consult [`botpress/test-cases.md`](file:///D:/Projects/CampusConnect/botpress/test-cases.md) to execute additional test prompts.

---

## Step 8: Publish the Agent

1. Once the emulator tests succeed, click the blue **"Publish"** button in the top right corner of Botpress Studio.
2. Wait for the notification banner confirming: **"Your bot has been published successfully."**

---

## Step 9: Obtain Webchat Embed Credentials

1. Exit the Studio and navigate back to your **Botpress Cloud Admin Dashboard**.
2. From the left sidebar, navigate to **Integrations** > **Webchat** (or **Channels** > **Webchat**).
3. In the Webchat configuration view, locate your unique credentials:
   - **Bot ID:** (e.g., `a1b2c3d4-e5f6-7890-abcd-1234567890ab`)
   - **Client ID:** (e.g., `a1b2c3d4-e5f6-7890-abcd-1234567890ab`)
   - **Webchat Script URL:** `https://cdn.botpress.cloud/webchat/v2/inject.js`
4. Copy these credentials and keep them handy.
5. In the upcoming website integration phase, you will paste these keys into `botpress/botpress-config-template.json` to activate the live chatbot in your web portal.

> **Security Note:** Do NOT commit administrative API keys or personal access tokens to GitHub. The Webchat Bot ID and Client ID are public client identifiers intended for browser embedding.

