# CampusConnect AI – Generative AI Powered Student Assistance Chatbot

[![UN SDG 4: Quality Education](https://img.shields.io/badge/UN%20SDG-4%20Quality%20Education-C5192D.svg)](https://sdgs.un.org/goals/goal4)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Stack: HTML5 / CSS3 / Vanilla JS](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-0066FF.svg)](assets/)
[![AI Engine: Botpress Cloud](https://img.shields.io/badge/AI%20Engine-Botpress%20Cloud-38BDF8.svg)](https://botpress.com/)

> **CampusConnect AI** is a lightweight, responsive student assistance platform engineered to provide 24/7 academic guidance, learning resources, and campus support. Built strictly with standard web technologies and integrated with Botpress Cloud, it empowers college learners while directly advancing **United Nations Sustainable Development Goal 4 (Quality Education)**.

---

## Table of Contents
- [Project Overview](#project-overview)
- [UN SDG 4 Alignment](#un-sdg-4-alignment)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Design Direction](#design-direction)
- [Getting Started](#getting-started)
- [Knowledge Base & Botpress Cloud Integration](#knowledge-base--botpress-cloud-integration)
- [Development Roadmap](#development-roadmap)
- [Engineering Guidelines](#engineering-guidelines)
- [License](#license)

---

## Project Overview

Higher education administrative systems are frequently fragmented across disparate websites, unindexed PDFs, and backlogged email queues. During peak periods such as enrollment weeks and examinations, students face multi-day delays for basic advising questions.

**CampusConnect AI** solves this challenge through:
1. **A Centralized Web Portal:** A fast, accessible, dependency-free frontend organized around six student guidance categories.
2. **Generative AI Chatbot (Botpress Cloud):** An authentic conversational agent backed by Retrieval-Augmented Generation (RAG) that answers questions grounded strictly in official university guidelines.
3. **Structured Knowledge Base Repository:** Standardized markdown templates designed for seamless vector ingestion into Botpress Cloud.

---

## UN SDG 4 Alignment

This project is built under the framework of **United Nations Sustainable Development Goal 4: Quality Education**:
- **Target 4.3 (Equal Access to Higher Education):** Provides continuous, 24/7 guidance to non-traditional, commuter, and working students who cannot attend standard on-campus advising hours.
- **Target 4.4 (Digital Inclusivity & Skills):** Delivers a responsive, lightweight web application requiring zero high-end hardware, native app downloads, or heavy runtimes.
- **Target 4.a (Inclusive Learning Environments):** Connects learners immediately with mental wellness counseling, academic accommodations, peer tutoring, and emergency relief grants.

---

## Technology Stack

To ensure maximum performance, zero build complexity, and long-term maintainability, the project strictly adheres to native web standards:

- **Markup:** HTML5 (Semantic, accessible landmarks)
- **Styling:** CSS3 (CSS Variables, Flexbox, CSS Grid, Responsive Breakpoints, Custom Animations)
- **Scripting:** Vanilla JavaScript (ES6+, zero frameworks, zero external dependencies)
- **AI Chatbot Engine:** Botpress Cloud (NLU, LLM orchestration, RAG vector database)
- **Frontend Integration:** Botpress Webchat v2
- **Version Control:** Git & GitHub

> **Architecture Principle:** No React, Next.js, Node.js, Python/Flask/Django backends, or SQL databases are introduced into the frontend client repository. The application runs natively in any standard web browser.

---

## Project Structure

```
CampusConnect-AI/
├── index.html                           # Main student portal landing page
├── assets/
│   ├── css/
│   │   └── style.css                    # Master stylesheet (Navy/White/Electric Blue aesthetic)
│   ├── js/
│   │   └── script.js                    # Client logic & Botpress Webchat integration hook
│   └── images/
│       └── logo.svg                     # Vector brand identity & favicon
├── knowledge-base/
│   ├── README.md                        # Knowledge base structuring & ingestion guide
│   ├── academic-guidelines-template.md  # Degree requirements, add/drop, prerequisites
│   └── student-services-faq-template.md # Health, housing, counseling, financial aid
├── botpress/
│   ├── README.md                        # Botpress Cloud configuration walkthrough
│   └── botpress-config-template.json    # Botpress Webchat parameters template
├── docs/
│   ├── project-overview.md              # Detailed academic project overview
│   ├── requirements-specification.md    # Functional & non-functional requirements
│   └── development-roadmap.md           # 5-Phase milestone & delivery plan
├── screenshots/
│   └── README.md                        # Submission captures guide
├── .gitignore                           # Git ignore rules (OS, IDE, secrets, logs)
├── LICENSE                              # MIT License
└── README.md                            # Primary project documentation
```

---

## Design Direction

CampusConnect AI incorporates a **modern university technology aesthetic**:
- **Palette:** Deep Academic Navy (`#0A192F`), Slate Navy (`#0F172A`), Electric Blue (`#0066FF`), Electric Cyan (`#38BDF8`), and Crisp Cloud White (`#F8FAFC`).
- **Typography:** Modern, clean sans-serif stack (`Inter`, system-ui, -apple-system, sans-serif) with high-contrast legibility.
- **Components:** Polished cards with subtle gradients, accent border glows, hover lift micro-interactions, and status indicators.
- **Responsiveness:** Full layout adaptation across mobile (320px+), tablet, and desktop screens.

---

## Getting Started

### Local Execution (No build tools or installation needed)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/CampusConnect-AI.git
   cd CampusConnect-AI
   ```

2. **Open in your browser:**
   - Double-click `index.html`, OR
   - Open it in VS Code and use the "Live Server" extension, OR
   - Use Python's built-in static server:
     ```bash
     python -m http.server 8000
     ```
     Navigate to `http://localhost:8000` in any web browser.

---

## Knowledge Base & Botpress Cloud Integration

The platform is engineered to separate presentation from conversational intelligence:

1. **Curate Documents:** Place your university handbooks and FAQs into `knowledge-base/`.
2. **Setup Botpress Cloud:** Create a bot in [Botpress Cloud](https://cloud.botpress.com/).
3. **Vectorize:** Upload the markdown files from `knowledge-base/` to the Botpress Knowledge Base section.
4. **Deploy Webchat:** Copy your `botId` into `botpress/botpress-config-template.json` and invoke `window.initBotpressWebchat()` from `assets/js/script.js`.

*Note: In the foundational stage, no fake or mock bot responses are hardcoded. Genuine AI responses are activated when Botpress Cloud is wired in the integration phase.*

---

## Development Roadmap

- [x] **Phase 1: Project Foundation & Architecture** *(Current Phase Completed)*
  - Full directory structure created.
  - Production `.gitignore` and open-source MIT License added.
  - Core specifications authored (`docs/project-overview.md`, `docs/requirements-specification.md`, `docs/development-roadmap.md`).
  - Knowledge base templates staged in `knowledge-base/`.
  - Botpress Cloud integration templates staged in `botpress/`.
  - Responsive HTML5/CSS3 landing page and Vanilla JS engine implemented.
- [ ] **Phase 2: College Portal Refinement & Domain Customization**
- [ ] **Phase 3: Botpress Cloud Setup, Persona Engineering & Knowledge Ingestion**
- [ ] **Phase 4: Botpress Webchat Injection & Live Chat Event Binding**
- [ ] **Phase 5: Quality Assurance, Accessibility Audit & Deployment (GitHub Pages)**

See [`docs/development-roadmap.md`](docs/development-roadmap.md) for detailed deliverables.

---

## Engineering Guidelines

- **Zero Fake Responses:** The assistant interface strictly defers conversation to the authenticated Botpress Cloud agent.
- **Security & Privacy:** Never commit `.env` files, API keys, or private bot tokens.
- **Maintainability:** Pure standard web technologies; zero node modules or compile steps.

---

## License

This project is licensed under the [MIT License](LICENSE).

