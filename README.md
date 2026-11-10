# CampusConnect AI – Generative AI Powered Student Assistance Chatbot

[![UN SDG: Quality Education](https://img.shields.io/badge/UN%20SDG-Quality%20Education-C5192D.svg)](https://sdgs.un.org/goals/goal4)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Stack: HTML5 / CSS3 / Vanilla JS](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-0066FF.svg)](assets/)
[![AI Engine: Botpress Cloud](https://img.shields.io/badge/AI%20Engine-Botpress%20Cloud-38BDF8.svg)](https://botpress.com/)
[![Webchat: Connected](https://img.shields.io/badge/Webchat-Live%20Agent%20Connected-10B981.svg)](botpress/)

> **CampusConnect AI** is a modern student assistance platform engineered to provide 24/7 academic guidance, learning resource recommendations, and student support. Built strictly with standard web technologies and integrated with an authentic **Botpress Cloud** Generative AI agent, it empowers collegiate learners while directly advancing **United Nations Sustainable Development Goal 4 (Quality Education)**.

---

## Table of Contents
- [Project Overview](#project-overview)
- [UN SDG Alignment](#un-sdg-alignment)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Design Direction](#design-direction)
- [Botpress Cloud Integration & Live Agent](#botpress-cloud-integration--live-agent)
- [Getting Started & Local Execution](#getting-started--local-execution)
- [GitHub Pages Deployment Guide](#github-pages-deployment-guide)
- [Development Roadmap Status](#development-roadmap-status)
- [Engineering & Security Principles](#engineering--security-principles)
- [License](#license)

---

## Project Overview

Higher education administrative systems are frequently fragmented across disparate websites, unindexed PDFs, and backlogged email queues. During peak periods such as enrollment weeks and examinations, students face multi-day delays for basic advising questions.

**CampusConnect AI** solves this challenge through:
1. **A Centralized Web Portal:** A fast, responsive, dependency-free frontend organized around 6 core student guidance pillars, an accessible search filter, and interactive prompt cards.
2. **Generative AI Chatbot (Botpress Cloud):** An authentic conversational agent backed by Retrieval-Augmented Generation (RAG) that answers questions grounded strictly in official university guidelines and learning science.
3. **Structured Knowledge Base Repository:** Standardized markdown documents designed for seamless vector ingestion into Botpress Cloud.

---

## UN SDG Alignment

This project is built under the framework of **United Nations Sustainable Development Goal 4: Quality Education**:
- **Target 4.3 (Equal Access to Higher Education):** Provides continuous, 24/7 guidance to non-traditional, commuter, and working students who cannot attend standard on-campus advising hours.
- **Target 4.4 (Digital Inclusivity & Skills):** Delivers a responsive, lightweight web application requiring zero high-end hardware, native app downloads, or heavy runtimes.
- **Target 4.a (Inclusive Learning Environments):** Connects learners immediately with mental wellness counseling, academic accommodations, peer tutoring, and emergency relief grants.

---

## Technology Stack

To ensure maximum performance, zero build complexity, and long-term maintainability, the project strictly adheres to native web standards:

- **Markup:** HTML5 (Semantic, accessible landmarks, WCAG 2.1 AA compliant)
- **Styling:** CSS3 (CSS Variables, Flexbox, CSS Grid, Responsive Breakpoints, Custom Animations)
- **Scripting:** Vanilla JavaScript (ES6+, zero frameworks, zero external libraries)
- **AI Chatbot Engine:** Botpress Cloud (NLU, Autonomous Node, RAG vector database)
- **Frontend Integration:** Botpress Webchat v3.7 official embed bundle
- **Version Control:** Git & GitHub

> **Architecture Principle:** No React, Next.js, Node.js, Python/Flask/Django backends, or SQL databases are introduced into the frontend client repository. The application runs natively in any standard web browser.

---

## Project Structure

```
CampusConnect-AI/
├── index.html                                 # Main student portal landing page
├── assets/
│   ├── css/
│   │   └── style.css                          # Master stylesheet (Navy/White/Electric Blue aesthetic)
│   ├── js/
│   │   └── script.js                          # Client logic, live search & Botpress Webchat API binding
│   └── images/
│       └── logo.svg                           # Vector brand identity & favicon
├── knowledge-base/
│   ├── README.md                              # Knowledge base structuring & ingestion guide
│   ├── campusconnect-student-guide.md         # Primary 10-category student guide for Botpress RAG
│   ├── academic-policies.md                   # Credit limits, add/drop, prerequisites, GPA scale
│   ├── library-and-learning-resources.md      # Library hours, digital databases, study rooms
│   ├── student-services-and-campus-life.md    # Health, CAPS, residential life, transit, and clubs
│   ├── examination-and-grading-rules.md       # Exam conflicts, 4.00 GPA calculation, and honor code
│   ├── academic-guidelines-template.md        # Modular template for degree requirements
│   └── student-services-faq-template.md       # Modular template for campus FAQs
├── botpress/
│   ├── README.md                              # Botpress Cloud configuration & integration guide
│   ├── agent-instructions.md                  # Autonomous Node system prompt & behavioral guardrails
│   ├── conversation-design.md                 # 8 Conversational flows, dialog trees & fallbacks
│   ├── test-cases.md                          # 28 Structured evaluation test cases
│   ├── setup-guide.md                         # Step-by-step setup walkthrough for Botpress Cloud
│   ├── botpress-config.json                   # Active Botpress configuration matching live bot
│   └── botpress-config-template.json          # Reusable template for secondary bot environments
├── docs/
│   ├── project-overview.md                    # Detailed academic project overview & SDG 4 analysis
│   ├── requirements-specification.md          # Functional (FR) & Non-Functional (NFR) specifications
│   └── development-roadmap.md                 # 5-Phase milestone & delivery tracking
├── screenshots/
│   └── README.md                              # Visual documentation & screenshot capture guide
├── .gitignore                                 # Git ignore rules (OS, IDE, secrets, logs)
├── LICENSE                                    # MIT Open Source License
└── README.md                                  # Primary project documentation
```

---

## Design Direction

CampusConnect AI incorporates a **modern university technology aesthetic**:
- **Palette:** Deep Academic Navy (`#0A192F`), Slate Navy (`#0F172A`), Surface Navy (`#132238`), Electric Blue (`#0066FF`), Electric Cyan (`#38BDF8`), and Crisp Cloud White (`#F8FAFC`).
- **Typography:** Modern, clean sans-serif stack (`Inter`, system-ui, -apple-system, sans-serif) with high-contrast legibility.
- **Components:** Polished cards with subtle gradients, accent border glows, hover lift micro-interactions, live search filtering, and status indicators.
- **Responsiveness:** Full layout adaptation across mobile (320px+), tablet, and desktop screens.

---

## Botpress Cloud Integration & Live Agent

The platform is integrated with an authentic **Botpress Cloud** AI agent:

### Active Embed Code (`index.html`)
```html
<script src="https://cdn.botpress.cloud/webchat/v3.7/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/11/10/16/20261110165048-XOMTS7I8.js" defer></script>
```
- **Bot ID:** `2133e1fa-1a4d-404a-9f96-6a988597b04f`
- **Client ID:** `eacbce57-d261-419a-8f54-f8c85d2402a5`
- **Active Configuration File:** [`botpress/botpress-config.json`](botpress/botpress-config.json)

### JavaScript Interaction Model
- **Opening the Assistant:** All "Ask CampusConnect" and "Ask AI" buttons invoke `window.botpress.open()`.
- **Suggested Questions:** Clicking any suggested prompt opens the Webchat and delivers the message via `window.botpress.sendMessage(question)` after the `webchat:ready` event.
- **Anti-Hallucination Guardrail:** The bot strictly refuses to guess official college exam dates, tuition fees, or admission deadlines, directing students to their official registrar or portal.

---

## Getting Started & Local Execution

### Option 1: Direct File Open
Double-click `index.html` to open it in any standard web browser (Chrome, Edge, Firefox, Safari).

### Option 2: Python Static Web Server (Recommended)
```bash
# Clone the repository
git clone https://github.com/your-username/CampusConnect-AI.git
cd CampusConnect-AI

# Start static HTTP server on port 8080
python -m http.server 8080
```
Navigate to `http://localhost:8080` in your browser.

---

## GitHub Pages Deployment Guide

Because CampusConnect AI is built strictly with HTML5, CSS3, and Vanilla JavaScript, it can be deployed to **GitHub Pages** with zero build steps:

1. Push the repository to GitHub:
   ```bash
   git remote add origin https://github.com/your-username/CampusConnect-AI.git
   git branch -M main
   git push -u origin main
   ```
2. On GitHub, navigate to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4. Set branch to `main` and folder to `/ (root)`.
5. Click **Save**. Within 1–2 minutes, your website is live at:  
   `https://<your-username>.github.io/CampusConnect-AI/`

---

## Development Roadmap Status

- [x] **Phase 1: Project Foundation & Architecture** (Completed)
- [x] **Phase 2: Modern Web Portal Implementation** (Completed)
- [x] **Phase 3: Knowledge Base & Botpress Cloud Setup** (Completed)
- [x] **Phase 4: Botpress Webchat Integration & Event Binding** (Completed)
- [x] **Phase 5: Quality Assurance, Verification & Deployment** (Completed)

See [`docs/development-roadmap.md`](docs/development-roadmap.md) for detailed deliverables.

---

## Engineering & Security Principles

- **Zero Fake Responses:** The assistant interface strictly defers conversation to the authenticated Botpress Cloud agent.
- **Security & Privacy:** No administrative API keys, secrets, or personal access tokens are committed. All external links use `rel="noopener noreferrer"`.
- **Maintainability:** Pure standard web technologies; zero node modules, compile steps, or runtime overhead.

---

## License

This project is licensed under the [MIT License](LICENSE).
