# Project Development Roadmap

This document outlines the phased engineering milestones for **CampusConnect AI**. The roadmap is organized into five structured phases to ensure systematic delivery and academic rigor.

---

## Roadmap Overview

```
+--------------------------------------------------------------------------+
|  Phase 1: Project Foundation & Architecture (COMPLETED)                  |
|  - Repository architecture, Git hygiene, foundational docs & design system|
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 2: Modern Web Portal Implementation (COMPLETED)                   |
|  - Semantic HTML5, CSS3 Navy/Electric design, responsive interactions   |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 3: Knowledge Base & Botpress Cloud Configuration (COMPLETED)      |
|  - Institutional RAG document authoring, bot persona & workflow rules    |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 4: Botpress Webchat Integration & Event Binding (COMPLETED)       |
|  - Script embed injection, custom styling alignment & launch triggers    |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 5: Quality Assurance, Verification & Deployment (COMPLETED)       |
|  - WCAG audit, performance benchmarks, GitHub Pages deployment           |
+--------------------------------------------------------------------------+
```

---

## Phase Details

### Phase 1: Project Foundation & Architecture (COMPLETED)
- [x] Establish the clean repository directory tree:
  - `assets/` (`css/`, `js/`, `images/`)
  - `docs/`
  - `knowledge-base/`
  - `botpress/`
  - `screenshots/`
- [x] Configure production `.gitignore` ensuring zero leakage of secrets or OS artifacts.
- [x] Define open-source MIT License.
- [x] Author core documentation suite:
  - `docs/project-overview.md`
  - `docs/requirements-specification.md`
  - `docs/development-roadmap.md`
- [x] Prepare foundational markup, stylesheet, and client script with Botpress integration hooks.
- [x] Create comprehensive `README.md` baseline.

### Phase 2: Modern Web Portal Implementation (COMPLETED)
- [x] Implement the Navy Blue, Electric Blue, and Crisp White aesthetic.
- [x] Build semantic components:
  - Global Navigation with responsive mobile menu.
  - Hero banner with UN SDG recognition badge.
  - Interactive Guidance Categories (Academics, Resources, Campus Life, Admissions, Exams, Career).
  - Quick Search & Filter mechanism in Vanilla JS.
  - Botpress Architecture & Integration Preview section.
- [x] Apply accessible typography, modern CSS grid/flexbox layouts, and smooth transition states.

### Phase 3: Knowledge Base & Botpress Cloud Setup (COMPLETED)
- [x] Author comprehensive knowledge base guides inside `knowledge-base/`:
  - `campusconnect-student-guide.md` (10 core study and learning categories)
  - `academic-policies.md`
  - `library-and-learning-resources.md`
  - `student-services-and-campus-life.md`
  - `examination-and-grading-rules.md`
- [x] Author Botpress Cloud configuration suite:
  - `botpress/agent-instructions.md` (Autonomous Node prompt, anti-hallucination guardrails)
  - `botpress/conversation-design.md` (8 conversational flow specifications)
  - `botpress/test-cases.md` (28 structured evaluation test cases)
  - `botpress/setup-guide.md` (Manual step-by-step Botpress setup guide)

### Phase 4: Botpress Webchat Integration (COMPLETED)
- [x] Injected official Botpress Webchat v3.7 embed bundle:
  - `https://cdn.botpress.cloud/webchat/v3.7/inject.js`
  - `https://files.bpcontent.cloud/2026/11/10/16/bot-config.js`
- [x] Wired CTA buttons ("Ask CampusConnect", "Ask AI") to `window.botpress.open()`.
- [x] Connected interactive suggested question cards to `window.botpress.sendMessage(question)`.
- [x] Enforced Webchat readiness event (`webchat:ready`) and queued messages.
- [x] Prevented duplicate floating widgets by hiding custom button upon Botpress mount.
- [x] Executed live API test sessions against hosted agent (`clientId: YOUR_BOTPRESS_CLIENT_ID`).

### Phase 5: QA, Verification & Final Deployment (COMPLETED)
- [x] Verify HTTP 200 responses on all static assets without 404s.
- [x] JavaScript syntax validation (`node -c assets/js/script.js` passing with 0 errors).
- [x] Accessibility audit against WCAG 2.1 AA standards (contrast, focus outlines, ARIA attributes).
- [x] Multi-viewport layout testing (Desktop 1920px/1280px, Tablet 768px, Mobile 360px–480px).
- [x] Create GitHub Pages deployment instructions in documentation (`README.md`).
- [x] Final project summary and viva voce presentation guide (`docs/viva-presentation-guide.md`).
