# Botpress Cloud Integration & Documentation Suite

## Overview

**CampusConnect AI** leverages **Botpress Cloud** as its conversational Generative AI engine. Botpress handles Natural Language Understanding (NLU), Large Language Model (LLM) orchestration, and Knowledge Base vector retrieval (RAG).

The frontend portal embeds the official **Botpress Webchat v3.7** library connected to the live published agent.

---

## Active Webchat Embed Configuration

The live bot is integrated directly into `index.html` using the official Botpress embed snippet:

```html
<script src="https://cdn.botpress.cloud/webchat/v3.7/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/11/10/16/bot-config.js" defer></script>
```

- **Bot ID:** `YOUR_BOTPRESS_BOT_ID`
- **Client ID:** `YOUR_BOTPRESS_CLIENT_ID`
- **Active Config File:** [`botpress-config.json`](botpress-config.json)

---

## Suite of Botpress Configuration Documents

This directory contains the complete specification and configuration materials needed to set up and deploy the Botpress AI assistant:

1. **[`setup-guide.md`](setup-guide.md):** Complete step-by-step instructions for creating the bot in Botpress Cloud, configuring the Autonomous Node, uploading the knowledge base, testing in the emulator, publishing, and retrieving Webchat credentials.
2. **[`agent-instructions.md`](agent-instructions.md):** Complete system instructions and personality prompt for the Autonomous Node, including anti-hallucination rules, clarification protocols, and verified resource references.
3. **[`conversation-design.md`](conversation-design.md):** Architectural flows for greeting, academic assistance, examination preparation, timetable planning, resource recommendations, unknown-question fallback, and closing.
4. **[`test-cases.md`](test-cases.md):** 28 comprehensive test cases covering normal questions, differently phrased/typo queries, ambiguous inquiries, institution-specific questions, and boundary-testing questions.
5. **[`botpress-config.json`](botpress-config.json):** Active configuration parameters matching the published live bot.
6. **[`botpress-config-template.json`](botpress-config-template.json):** Reusable template for secondary environments.

---

## Webchat JavaScript API Integration

CampusConnect AI's frontend interacts with the live Botpress Webchat via documented methods in `assets/js/script.js`:

- **Open Webchat:** `window.botpress.open()`
- **Send Message:** `window.botpress.sendMessage(message)`
- **Readiness Listener:** `window.botpress.on('webchat:ready', () => { ... })`
- **Open/Close Listeners:** `window.botpress.on('webchat:opened', ...)` and `window.botpress.on('webchat:closed', ...)`
