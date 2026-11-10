# Botpress Cloud Integration & Documentation Suite

## Overview

**CampusConnect AI** leverages **Botpress Cloud** as its conversational Generative AI engine. Botpress handles Natural Language Understanding (NLU), Large Language Model (LLM) orchestration, and Knowledge Base vector retrieval (RAG).

The frontend portal embeds the official **Botpress Webchat** library to provide an accessible, real-time chat interface.

---

## Suite of Botpress Configuration Documents

This directory contains the complete specification and configuration materials needed to set up and deploy the Botpress AI assistant:

1. **[`setup-guide.md`](setup-guide.md):** Complete step-by-step instructions for creating the bot in Botpress Cloud, configuring the Autonomous Node, uploading the knowledge base, testing in the emulator, publishing, and retrieving Webchat credentials.
2. **[`agent-instructions.md`](agent-instructions.md):** Complete system instructions and personality prompt for the Autonomous Node, including anti-hallucination rules, clarification protocols, and verified resource references.
3. **[`conversation-design.md`](conversation-design.md):** Architectural flows for greeting, academic assistance, examination preparation, timetable planning, resource recommendations, unknown-question fallback, and closing.
4. **[`test-cases.md`](test-cases.md):** 28 comprehensive test cases covering normal questions, differently phrased/typo queries, ambiguous inquiries, institution-specific questions, and boundary-testing questions.
5. **[`botpress-config-template.json`](botpress-config-template.json):** Configuration parameters template ready for your live `botId` and `clientId`.

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
|  - Autonomous Node (System Instructions)               |
|  - Generative AI LLM Orchestrator                      |
|  - Knowledge Base (Vector Ingestion from /knowledge-base)
+--------------------------------------------------------+
```

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
