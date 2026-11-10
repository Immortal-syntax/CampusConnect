# Screenshots & Project Visual Presentation

## Overview
This directory serves as the repository for visual captures of **CampusConnect AI** for project reports, viva presentations, and submission evaluations.

---

## Suggested Visual Submissions for Academic Evaluation

| Visual Asset | Target Viewport | Key Features to Highlight |
| :--- | :---: | :--- |
| `01-desktop-hero-overview.png` | Desktop (1920x1080) | - Header navigation & "Ask AI" button<br>- UN SDG Announcement Banner<br>- Navy & Electric Blue SaaS aesthetic<br>- Value proposition & stat pills<br>- Interactive UI card preview |
| `02-features-grid.png` | Desktop (1440x900) | - 6 Modern feature cards with hover states<br>- Topic tags (Generative AI, Curriculum Support, etc.) |
| `03-chatbot-intro-and-status.png` | Desktop (1440x900) | - Assistant overview & capabilities checklist<br>- "Open AI Chatbot" CTA<br>- Live status badge: `Botpress Webchat Connected & Live`<br>- Integration architecture spec card |
| `04-student-support-categories.png` | Desktop (1440x900) | - 6 Collegiate advisory categories with topic tags<br>- Direct question trigger buttons |
| `05-interactive-suggested-questions.png`| Desktop / Tablet | - 5 Suggested prompt cards<br>- Micro-interaction hover states |
| `06-botpress-webchat-live-chat.png` | Desktop (1440x900) | - Botpress Webchat dialog open on the right<br>- Multi-turn conversation demonstrating active recall advice<br>- Verified resource recommendation (SWAYAM / NPTEL) |
| `07-mobile-responsive-navigation.png` | Mobile (375x812) | - Mobile hamburger menu expanded<br>- Touch-friendly navigation links and layout reflow |

---

## How to Capture Live Screenshots

1. Start your local server:
   ```bash
   python -m http.server 8080
   ```
2. Open `http://localhost:8080` in your browser.
3. Use your browser's Developer Tools (`Ctrl+Shift+I` or `Cmd+Option+I`):
   - Toggle Device Toolbar (`Ctrl+Shift+M`).
   - Select **Responsive**, set dimensions (e.g., `1920x1080` or `375x812`).
   - Click the three dots in DevTools -> **"Capture full size screenshot"** or **"Capture screenshot"**.
4. Save the generated image files into this `screenshots/` directory with the filenames listed above.
