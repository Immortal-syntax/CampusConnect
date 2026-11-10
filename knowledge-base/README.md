# CampusConnect AI – Knowledge Base Repository

## Purpose
This directory stores structured institutional documents and study guides designed for ingestion into **Botpress Cloud** to power the generative AI student assistant.

Using Retrieval-Augmented Generation (RAG), Botpress indexes these markdown documents into high-dimensional vector embeddings, enabling the conversational assistant to provide verified, factual responses with zero fictitious information.

---

## Directory Inventory

```
knowledge-base/
  README.md                                    # This directory index & ingestion guide
  campusconnect-student-guide.md               # Primary 10-category student guide for Botpress RAG
  academic-policies.md                         # Credit limits, add/drop, prerequisites, GPA scale
  library-and-learning-resources.md            # Library hours, digital databases, study rooms
  student-services-and-campus-life.md          # Health & CAPS, housing, dining, transit, clubs
  examination-and-grading-rules.md             # Exam conflicts, grade appeals, honor code
  academic-guidelines-template.md              # Customizable template for degree requirements
  student-services-faq-template.md             # Customizable template for campus FAQs
```

---

## Primary Knowledge Base Document: `campusconnect-student-guide.md`

The file [`campusconnect-student-guide.md`](campusconnect-student-guide.md) is the primary document to upload directly into your Botpress Cloud Knowledge Base. It contains verified educational guidance across 10 essential categories:

1. **Study Techniques:** Active recall, spaced repetition, Feynman technique, interleaving, and dual coding.
2. **Examination Preparation:** Backward study planning, timed past papers, error logging, and anxiety reduction.
3. **Time Management:** The Eisenhower Matrix, time blocking, Pomodoro variations, and overcoming procrastination.
4. **Creating Study Timetables:** The credit-hour study ratio formula and sample balanced weekly schedules.
5. **Note-Taking Methods:** Cornell note-taking, concept/mind mapping, outline method, digital vs. handwritten notes.
6. **Learning Resources:** Accredited platforms including SWAYAM, NPTEL, DIKSHA, UNESCO OER, NDLI, and MIT OCW.
7. **Online Education:** Asynchronous pacing, digital etiquette, and low-bandwidth optimizations.
8. **Academic Productivity:** Managing phone distractions, workspace ergonomics, hydration, and avoiding burnout.
9. **Student Support:** Faculty office hours, academic advising, peer tutoring, and mental health awareness.
10. **Frequently Asked Student Questions:** Realistic student queries and high-retention answers.

---

## Guidelines for Authoring & Customizing Knowledge Base Documents

1. **Clear Markdown Hierarchy:** Use `#`, `##`, and `###` headers to delineate topics. Botpress chunking algorithms split documents on header boundaries.
2. **Atomic Information Units:** Keep sections self-contained with clear definitions and actionable steps.
3. **Institutional Verification Disclaimers:** Mark institution-specific information (fees, dates, specific course codes) with verification notices so the AI accurately advises students to verify with their college registrar.
4. **Accredited Resources:** Anchor all learning recommendations in verified educational platforms (e.g., SWAYAM, NPTEL, DIKSHA, UNESCO, MIT OCW).
