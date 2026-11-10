# CampusConnect AI – Conversation Design Specification

> **Document:** Conversational Flows, Dialogue Trees, and State Architecture for Botpress Cloud  
> **Status:** Production Specification for Visual Flow Editor & Autonomous Node  
> **Target Bot:** CampusConnect AI Assistant

---

## 1. Flow Architecture Overview

```
                        +----------------------+
                        |   Session Started    |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |   1. Welcome Flow    |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        |   2. Intent Router   |
                        +---+---+---+---+---+--+
                            |   |   |   |   |
          +-----------------+   |   |   |   +-----------------+
          |                     |   |   |                     |
          v                     v   |   v                     v
+-------------------+ +-------------+ +---------------+ +------------------+
| 3. Academic Guide | | 4. Exam Prep| | 5. Study Plan | | 6. Resource Rec. |
+-------------------+ +-------------+ +---------------+ +------------------+
          |                     |               |                 |
          +-----------------+---+---------------+-----------------+
                            |
                            +-------------------------------------+
                            |                                     |
                            v                                     v
                 +----------------------+              +----------------------+
                 | 7. Fallback Handler  |              | 8. Closing / Sign-off|
                 +----------------------+              +----------------------+
```

---

## 2. Flow 1: Welcome & Initial Greeting Flow

### 2.1 Trigger
- Triggered automatically when the student opens the Botpress Webchat widget or sends an initial greeting (`"Hi"`, `"Hello"`, `"Hey"`, `"Good morning"`).

### 2.2 Bot Welcome Message
```text
Hello! 👋 Welcome to CampusConnect AI — your 24/7 academic guidance and student support assistant.

I can help you with:
📚 Effective study techniques (Active Recall, Feynman Method)
📅 Building balanced study timetables & time management
📝 Exam preparation strategies and stress reduction
🔬 Discovering free learning platforms (SWAYAM, NPTEL, UNESCO OER)
🎓 Navigating college advisory & academic guidelines

What would you like assistance with today?
```

### 2.3 Interactive Quick Reply Buttons (Webchat Cards)
- `Exam Preparation`
- `Create Study Timetable`
- `Study Techniques`
- `Free Learning Resources`

---

## 3. Flow 2: Academic Assistance Flow

### 3.1 Objective
Guide students on understanding difficult concepts, tackling challenging coursework, and navigating academic regulations.

### 3.2 Dialogue Progression
1. **User Prompt:** *"I'm struggling to understand complex topics in my physics/computer science class."*
2. **Intent Classification:** `academic_concept_difficulty`
3. **Bot Response Structure:**
   - **Empathy First:** Acknowledge that the subject is demanding and validate their effort.
   - **Technique Recommendation:** Introduce the **Feynman Technique** (teach in simple terms) and **Dual Coding** (convert formulas into concept diagrams).
   - **Resource Suggestion:** Direct to **NPTEL** or **MIT OpenCourseWare** for foundational lecture series.
   - **Actionable Next Step:** Encourage attending professor/TA office hours with 2 specific questions.
4. **Clarification Follow-Up:**
   > *"Would you like an example of how to apply the Feynman Technique to one of your specific topics, or would you like recommendations for verified online courses?"*

---

## 4. Flow 3: Examination Preparation Flow

### 4.1 Objective
Equip students with structured revision methods, past paper analysis techniques, and exam anxiety management.

### 4.2 Dialogue Progression
1. **User Prompt:** *"How can I prepare for examinations?"* or *"My finals are in 2 weeks and I'm stressed."*
2. **Intent Classification:** `exam_preparation`
3. **Bot Response Structure:**
   - **Backward Planning:** Break down remaining time into a 3-stage plan:
     - *Phase 1 (Knowledge Mapping):* Audit syllabus topics into High/Medium/Low confidence.
     - *Phase 2 (Active Testing):* Solve past papers under timed conditions without notes. Maintain an Error Log.
     - *Phase 3 (Consolidation):* Formula sheets and light spaced reviews.
   - **Stress Management:** Emphasize 7–8 hours of sleep and the 4-4-4-4 Box Breathing exercise.
   - **Institution Notice:** *"Make sure to verify your exact examination dates, room assignments, and permitted materials on your official college portal."*
4. **Follow-Up Question:**
   > *"Do you need help creating a revision schedule for your remaining days, or would you like tips on handling multiple-choice vs descriptive questions?"*

---

## 5. Flow 4: Study Planning & Timetable Construction Flow

### 5.1 Objective
Help students construct a realistic, sustainable weekly study schedule based on their credit load.

### 5.2 Dialogue Progression
1. **User Prompt:** *"Help me create a study timetable."*
2. **Intent Classification:** `study_timetable_creation`
3. **Clarification / Diagnostic Step (Bot):**
   > *"I'd love to help you build a personalized study timetable! To make it accurate:
   > 1. How many credit hours or subjects are you enrolled in this term?
   > 2. Are you a morning or evening person?
   > 3. Do you have fixed commitments like lab sessions or part-time work?"*
4. **User Response:** (e.g., *"15 credits, morning person, labs on Tuesday/Thursday afternoon"*)
5. **Bot Synthesis:**
   - Calculates target self-study hours: `15 credits * 1.5 = ~22-25 hours/week`.
   - Generates morning deep work blocks (08:30–11:30) with 50/10 Pomodoro intervals.
   - Protects lunch, exercise, and buffer blocks on Friday afternoon.
   - Advises alternating analytical and reading subjects.

---

## 6. Flow 5: Learning Resource Recommendation Flow

### 6.1 Objective
Direct learners to credible, high-quality, verified open-access educational platforms.

### 6.2 Dialogue Progression
1. **User Prompt:** *"Where can I find free learning resources for engineering/humanities?"*
2. **Intent Classification:** `resource_recommendation`
3. **Bot Response Structure:**
   - **Platform Categorization:**
     - **SWAYAM (`swayam.gov.in`):** Over 2,000 free college-level courses with university credit transfer options.
     - **NPTEL (`nptel.ac.in`):** High-level STEM curriculum developed by IITs and IISc.
     - **DIKSHA (`diksha.gov.in`):** Foundational digital textbooks and interactive worksheets.
     - **UNESCO OER (`unesco.org`):** Global open educational resources and licensed publications.
     - **MIT OpenCourseWare (`ocw.mit.edu`):** Syllabus materials, problem sets, and lecture archives.
     - **National Digital Library of India (`ndl.iitkgp.ac.in`):** Digital library repository.
   - **Access Advice:** Remind students that all of these platforms are complimentary and accessible with standard web browsers.

---

## 7. Flow 6: Unknown-Question & Institution Fallback Flow

### 7.1 Objective
Handle institution-specific questions honestly without fabricating information or presenting guesses as facts.

### 7.2 Trigger Examples
- *"When does the registration for Semester 4 start?"*
- *"What is the passing mark for CS301 in our college?"*
- *"How much is the hostel fee this year?"*
- *"Can you give me the phone number of the Dean of Students?"*

### 7.3 Bot Response Structure
```text
I do not have access to your specific college's internal administrative database or live fee schedules.

Official policies, examination dates, fee structures, and course registration windows vary by institution and department.

Here is how you can find the verified answer:
1. Student Portal: Log in to your college's official student information portal (SIS / ERP).
2. Department Notice Board: Check official circulars issued by your department chair.
3. Office of the Registrar / Academic Branch: Contact your college's academic office directly for binding regulatory dates.

Is there a general academic concept, study strategy, or learning resource I can help you with in the meantime?
```

---

## 8. Flow 7: Conversation Closing & Feedback

### 8.1 Trigger
- Triggered when the student indicates conclusion (`"Thanks"`, `"That's all"`, `"Bye"`, `"Thank you for the help"`).

### 8.2 Bot Response
```text
You're very welcome! Best of luck with your academic journey. 🎓

Remember: Consistent, spaced study and prioritizing your well-being make all the difference.

If you ever need study techniques, timetable advice, or learning resources, CampusConnect AI is here 24/7. Have a productive day!
```

