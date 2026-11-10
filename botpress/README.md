# Botpress Cloud Integration Guide

## Overview

**CampusConnect AI** leverages **Botpress Cloud** as its conversational Generative AI engine. Botpress handles the Natural Language Understanding (NLU), Large Language Model (LLM) orchestration, and Knowledge Base vector retrieval (RAG).

The frontend portal embeds the official **Botpress Webchat** library to provide a real-time chat interface.

---

## Integration Architecture

```
+--------------------------------------------------------+
|          CampusConnect AI Webpage (index.html)         |
|  - Injects Botpress Webchat v2 bundle                  |
|  - Injects assets/js/script.js initialization script   |
+---------------------------+----------------------------+
                            |
                     (HTTPS / WSS)
                            |
                            v
+--------------------------------------------------------+
|                 Botpress Cloud Engine                  |
|  - Bot ID / Client ID Authentication                   |
|  - Generative AI Orchestrator                          |
|  - Knowledge Base (Vector Ingestion from /knowledge-base)
+--------------------------------------------------------+
```

---

## Setup Steps (For Integration Stage)

1. **Create a Botpress Cloud Account:**  
   Sign in to [Botpress Cloud](https://cloud.botpress.com/) and create a new bot workspace named `CampusConnect-AI`.

2. **Upload Knowledge Base Assets:**  
   Upload the documents in `knowledge-base/` to the Botpress Knowledge Base panel.

3. **Configure Bot Persona & Prompt:**  
   Set the bot instructions to act as a courteous, accurate, and supportive university advisor.

4. **Retrieve Integration Credentials:**  
   From the Botpress Admin panel under **Integrations > Webchat**, note:
   - `botId`: Unique identifier for your bot.
   - `clientId`: Webchat client key.
   - `hostUrl`: Typically `https://cdn.botpress.cloud/webchat/v2`.

5. **Link into Frontend Portal:**  
   In `index.html` and `assets/js/script.js`, provide the config variables to the initialization hook `initBotpressWebchat()`.

---

## Webchat Configuration Sample

```json
{
  "botId": "YOUR_BOTPRESS_BOT_ID",
  "configuration": {
    "botName": "CampusConnect Assistant",
    "botAvatar": "assets/images/logo.svg",
    "botDescription": "Generative AI Student Assistance Hub",
    "themeColor": "#0066FF"
  }
}
```

> **Security Reminder:** Never commit administrative API keys or personal access tokens to this repository. The Webchat integration only requires public client identifiers.

