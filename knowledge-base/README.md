# CampusConnect AI - Knowledge Base Repository

## Purpose
This directory holds the structured, institutional documents that will be ingested into **Botpress Cloud** to power the generative AI student assistant.

Using Retrieval-Augmented Generation (RAG), Botpress indexes these markdown and text files, enabling the AI chatbot to provide accurate, factual responses with zero fictitious information.

---

## Directory Organization

```
knowledge-base/
  README.md                              # Ingestion guidelines & best practices
  academic-guidelines-template.md        # Course selection, prerequisites, credits
  student-services-faq-template.md       # Counseling, housing, health, student affairs
  library-resources-template.md          # Research databases, borrowing policies
  examination-rules-template.md          # Exam guidelines, grading schemes, reassessments
```

---

## Guidelines for Authoring Knowledge Base Documents

To ensure optimal vectorization and retrieval accuracy in Botpress Cloud:
1. **Use Clear Headings:** Use hierarchical markdown `#`, `##`, `###` headings to delineate topics.
2. **Atomic Information Units:** Keep related information grouped in concise sections.
3. **Question-and-Answer Pairs:** For FAQs, formulate questions matching how students typically inquire (e.g., *"How do I register for elective courses?"*).
4. **Avoid Speculative or Outdated Dates:** Use relative guidance or explicit academic year flags (e.g., `Academic Year 2026-2027`).
5. **No Invented Data:** Fill templates with generalized institutional guidelines or your specific university handbook data.

