# Project Development Roadmap

This document outlines the phased engineering milestones for **CampusConnect AI**. The roadmap is organized into five structured phases to ensure systematic delivery and academic rigor.

---

## Roadmap Overview

```
+--------------------------------------------------------------------------+
|  Phase 1: Project Foundation & Architecture (Current Phase)              |
|  - Repository architecture, Git hygiene, foundational docs & design system|
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 2: Modern Web Portal Implementation                               |
|  - Semantic HTML5, CSS3 Navy/Electric design, responsive interactions   |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 3: Knowledge Base & Botpress Cloud Configuration                  |
|  - Institutional RAG document authoring, bot persona & workflow rules    |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 4: Botpress Webchat Integration & Event Binding                   |
|  - Script embed injection, custom styling alignment & launch triggers    |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|  Phase 5: Quality Assurance, Verification & Deployment                   |
|  - WCAG audit, performance benchmarks, GitHub Pages deployment           |
+--------------------------------------------------------------------------+
```

---

## Phase Details

### Phase 1: Project Foundation & Architecture (CURRENT)
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

### Phase 2: Modern Web Portal Implementation
- [x] Implement the Navy Blue, Electric Blue, and Crisp White aesthetic.
- [x] Build semantic components:
  - Global Navigation with responsive mobile menu.
  - Hero banner with UN SDG 4 recognition badge.
  - Interactive Guidance Categories (Academics, Resources, Campus Life, Admissions, Exams, Career).
  - Quick Search & Filter mechanism in Vanilla JS.
  - Botpress Architecture & Integration Preview section.
- [x] Apply accessible typography, modern CSS grid/flexbox layouts, and smooth transition states.

### Phase 3: Knowledge Base & Botpress Cloud Setup
- [ ] Author standardized knowledge templates inside `knowledge-base/`:
  - `academic-policies.md`
  - `library-and-learning-resources.md`
  - `student-support-services.md`
  - `examination-and-grading-rules.md`
  - `faq-repository.md`
- [ ] Set up the Botpress Cloud workspace and create the student assistant bot.
- [ ] Ingest the curated knowledge base into Botpress Cloud vector storage.
- [ ] Configure generative AI prompt instructions (advising persona, boundaries, citation policies).

### Phase 4: Botpress Webchat Integration
- [ ] Extract Botpress Webchat v2 embed credentials (Bot ID, Client ID, Host URL).
- [ ] Securely link the Webchat script into `index.html` and `assets/js/script.js`.
- [ ] Align Webchat colors with the university Navy and Electric Blue theme palette.
- [ ] Test real-time message exchange and knowledge base retrieval via Botpress.

### Phase 5: QA, Verification & Final Deployment
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge).
- [ ] Mobile and tablet viewport validation.
- [ ] Accessibility review against WCAG 2.1 AA standards.
- [ ] Deploy live site via GitHub Pages or chosen static web host.
- [ ] Populate `screenshots/` directory with interface walkthrough visuals.

