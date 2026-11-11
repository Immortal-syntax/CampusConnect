#!/usr/bin/env python3
"""
CampusConnect AI - Academic Report & PDF Generator
Author Designation: Student Project Contributor
Project: CampusConnect AI – Generative AI Powered Student Assistance Chatbot
Target SDG: SDG 4 – Quality Education
Output Files:
  - final-submission/SDG_CampusConnectAI_Report.docx
  - final-submission/SDG_CampusConnectAI_Report.pdf
"""

import os
import subprocess
from typing import cast

import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Pt, RGBColor
from docx.styles.style import _ParagraphStyle

# Palette Constants
NAVY_PRIMARY = RGBColor(10, 25, 47)      # #0A192F
BLUE_ACCENT = RGBColor(0, 102, 255)      # #0066FF
TEXT_DARK = RGBColor(30, 41, 59)         # #1E293B
TEXT_MUTED = RGBColor(100, 116, 139)     # #64748B
WHITE = RGBColor(255, 255, 255)

HEX_BLUE = "0066FF"
HEX_LIGHT_BLUE = "F0F7FF"
HEX_BORDER = "CBD5E1"


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)


def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)


def set_cell_border(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            val = edge_data.get('val', 'single')
            color = edge_data.get('color', 'auto')
            sz = edge_data.get('sz', '4')
            tag = f'<w:{edge} {nsdecls("w")} w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            tcBorders.append(parse_xml(tag))
        else:
            tag = f'<w:{edge} {nsdecls("w")} w:val="none"/>'
            tcBorders.append(parse_xml(tag))
    tcPr.append(tcBorders)


def add_hyperlink(paragraph, url, text, color=HEX_BLUE, underline=True):
    part = paragraph.part
    r_id = part.relate_to(url, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink = parse_xml(f'<w:hyperlink {nsdecls("w", "r")} r:id="{r_id}"/>')
    new_run = parse_xml(f'<w:r {nsdecls("w")}>'
                        f'<w:rPr>'
                        f'<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>'
                        f'<w:color w:val="{color}"/>'
                        f'{"<w:u w:val=\"single\"/>" if underline else ""}'
                        f'</w:rPr>'
                        f'<w:t>{text}</w:t>'
                        f'</w:r>')
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def add_callout(doc, text, title=None, border_color=HEX_BLUE, bg_color=HEX_LIGHT_BLUE):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=160)
    set_cell_shading(cell, bg_color)
    set_cell_border(cell, left={'val': 'single', 'sz': '24', 'color': border_color})
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    if title:
        run_t = p.add_run(f"{title}\n")
        run_t.font.name = "Calibri"
        run_t.font.size = Pt(10.5)
        run_t.font.bold = True
        run_t.font.color.rgb = BLUE_ACCENT
    
    run_body = p.add_run(text)
    run_body.font.name = "Calibri"
    run_body.font.size = Pt(10)
    run_body.font.italic = True
    run_body.font.color.rgb = TEXT_DARK
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)


def add_code_box(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_margins(cell, top=120, bottom=120, left=160, right=160)
    set_cell_shading(cell, "F8FAFC")
    set_cell_border(cell,
                    top={'val': 'single', 'sz': '4', 'color': HEX_BORDER},
                    bottom={'val': 'single', 'sz': '4', 'color': HEX_BORDER},
                    left={'val': 'single', 'sz': '4', 'color': HEX_BORDER},
                    right={'val': 'single', 'sz': '4', 'color': HEX_BORDER})
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(15, 23, 42)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)


def add_screenshot_placeholder(doc, fig_num, title, filename, viewport, target_url, details, caption):
    table = doc.add_table(rows=2, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Header
    cell_hdr = table.cell(0, 0)
    cell_hdr.width = Inches(6.5)
    set_cell_margins(cell_hdr, top=100, bottom=100, left=160, right=160)
    set_cell_shading(cell_hdr, "0A192F")
    set_cell_border(cell_hdr,
                    top={'val': 'single', 'sz': '6', 'color': '0A192F'},
                    left={'val': 'single', 'sz': '6', 'color': '0A192F'},
                    right={'val': 'single', 'sz': '6', 'color': '0A192F'},
                    bottom={'val': 'single', 'sz': '4', 'color': '0066FF'})
    
    p_hdr = cell_hdr.paragraphs[0]
    p_hdr.paragraph_format.space_before = Pt(0)
    p_hdr.paragraph_format.space_after = Pt(0)
    
    run_hdr = p_hdr.add_run(f"SCREENSHOT PROOF-OF-WORK: {fig_num} – {title}")
    run_hdr.font.name = "Calibri"
    run_hdr.font.size = Pt(10)
    run_hdr.font.bold = True
    run_hdr.font.color.rgb = WHITE
    
    # Body
    cell_body = table.cell(1, 0)
    cell_body.width = Inches(6.5)
    set_cell_margins(cell_body, top=140, bottom=140, left=160, right=160)
    set_cell_shading(cell_body, "F8FAFC")
    set_cell_border(cell_body,
                    left={'val': 'single', 'sz': '6', 'color': 'CBD5E1'},
                    right={'val': 'single', 'sz': '6', 'color': 'CBD5E1'},
                    bottom={'val': 'single', 'sz': '6', 'color': 'CBD5E1'})
    
    p_b = cell_body.paragraphs[0]
    p_b.paragraph_format.space_before = Pt(0)
    p_b.paragraph_format.space_after = Pt(2)
    p_b.paragraph_format.line_spacing = 1.15
    
    p_b.add_run("• Expected Asset: ").bold = True
    r_fval = p_b.add_run(f"{filename}\n")
    r_fval.font.name = "Consolas"
    r_fval.font.size = Pt(9)
    r_fval.font.color.rgb = BLUE_ACCENT
    
    p_b.add_run("• Viewport / Source: ").bold = True
    p_b.add_run(f"{viewport}  |  URL: {target_url}\n")
    
    p_b.add_run("• Required Evidence: ").bold = True
    p_b.add_run(f"{details}\n")
    
    p_b.add_run("• Capture Status: ").bold = True
    r_sval = p_b.add_run("Documented Specification (Manual Browser Capture by Student Required Prior to Final Submission)")
    r_sval.font.size = Pt(9)
    r_sval.font.color.rgb = RGBColor(180, 83, 9)
    r_sval.bold = True
    
    # Caption
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(4)
    p_cap.paragraph_format.space_after = Pt(12)
    r_cap = p_cap.add_run(f"{fig_num}: {caption}")
    r_cap.font.name = "Calibri"
    r_cap.font.size = Pt(9.5)
    r_cap.font.italic = True
    r_cap.font.color.rgb = TEXT_MUTED


def add_custom_table(doc, headers, data_rows, col_widths=None):
    table = doc.add_table(rows=len(data_rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    # Header
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = ""
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
        set_cell_shading(hdr_cells[i], "0A192F")
        set_cell_border(hdr_cells[i],
                        top={'val': 'single', 'sz': '4', 'color': '0A192F'},
                        bottom={'val': 'single', 'sz': '12', 'color': '0066FF'},
                        left={'val': 'none'}, right={'val': 'none'})
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(h)
        run.font.name = "Calibri"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = WHITE
        if col_widths and i < len(col_widths):
            hdr_cells[i].width = col_widths[i]
            
    # Rows
    for r_idx, row in enumerate(data_rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = ""
            set_cell_margins(row_cells[c_idx], top=90, bottom=90, left=140, right=140)
            set_cell_shading(row_cells[c_idx], bg_col)
            set_cell_border(row_cells[c_idx],
                            bottom={'val': 'single', 'sz': '4', 'color': 'E2E8F0'},
                            top={'val': 'none'}, left={'val': 'none'}, right={'val': 'none'})
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(val)
            run.font.name = "Calibri"
            run.font.size = Pt(9.5)
            run.font.color.rgb = TEXT_DARK
            if col_widths and c_idx < len(col_widths):
                row_cells[c_idx].width = col_widths[c_idx]
                
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(6)


def build_word_and_pdf():
    doc = docx.Document()
    
    # Page Margins & A4 setup
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        
        header = section.header
        p_hdr = header.paragraphs[0]
        p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_hdr = p_hdr.add_run("CampusConnect AI – Academic Project Report")
        r_hdr.font.name = "Calibri"
        r_hdr.font.size = Pt(8.5)
        r_hdr.font.color.rgb = TEXT_MUTED
        
        footer = section.footer
        p_ftr = footer.paragraphs[0]
        p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r_ftr = p_ftr.add_run("CampusConnect AI (SDG 4: Quality Education)  |  Academic Evaluation Report")
        r_ftr.font.name = "Calibri"
        r_ftr.font.size = Pt(8.5)
        r_ftr.font.color.rgb = TEXT_MUTED

    # Style
    normal_style = cast(_ParagraphStyle, doc.styles['Normal'])
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = TEXT_DARK
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)

    # ==================== TITLE PAGE ====================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(18)
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("ACADEMIC PROJECT EVALUATION REPORT")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = NAVY_PRIMARY

    p_dept = doc.add_paragraph()
    p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dept.paragraph_format.space_before = Pt(0)
    p_dept.paragraph_format.space_after = Pt(24)
    r_dept = p_dept.add_run("Department of Computer Science & Engineering / Information Science\nContinuous Assessment & Evaluation")
    r_dept.font.name = "Calibri"
    r_dept.font.size = Pt(10.5)
    r_dept.font.color.rgb = TEXT_MUTED

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(16)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("CAMPUSCONNECT AI")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(26)
    r_title.font.bold = True
    r_title.font.color.rgb = BLUE_ACCENT

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(18)
    r_sub = p_sub.add_run("Generative AI Powered Student Assistance Chatbot")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(16)
    r_sub.font.bold = True
    r_sub.font.color.rgb = NAVY_PRIMARY

    add_callout(doc,
                "Project aligned with United Nations Sustainable Development Goal 4 (Quality Education): "
                "Ensuring inclusive and equitable quality higher education and promoting lifelong learning opportunities "
                "through 24/7 accessible, grounded Generative AI guidance.",
                title="UNITED NATIONS SUSTAINABLE DEVELOPMENT GOAL 4: QUALITY EDUCATION")

    p_meta_lbl = doc.add_paragraph()
    p_meta_lbl.paragraph_format.space_before = Pt(18)
    p_meta_lbl.paragraph_format.space_after = Pt(4)
    r_ml = p_meta_lbl.add_run("Academic Submission Details")
    r_ml.bold = True
    r_ml.font.size = Pt(11)
    r_ml.font.color.rgb = NAVY_PRIMARY

    meta_headers = ["Project Parameter", "Official Specification"]
    meta_rows = [
        ["Author Designation", "Student Author / Project Contributor"],
        ["Institution", "Engineering Institution / University"],
        ["Project Title", "CampusConnect AI – Generative AI Powered Student Assistance Chatbot"],
        ["Selected United Nations SDG", "SDG 4 – Quality Education (Targets 4.3, 4.4, 4.a)"],
        ["Academic Year", "2026"],
        ["Frontend Architecture", "HTML5 (Semantic) • CSS3 (Navy & Electric Blue) • Vanilla JS (ES6+)"],
        ["Conversational AI Engine", "Botpress Cloud (Autonomous Node, NLU, RAG Vector Engine)"],
        ["Open Source GitHub Repository", "https://github.com/Immortal-syntax/CampusConnect"],
        ["Live Production Deployment", "https://campus-connect-kohl-alpha.vercel.app/"],
        ["Operational Status", "Completed, Audited, Open Source & Deployed (HTTP 200)"]
    ]
    add_custom_table(doc, meta_headers, meta_rows, col_widths=[Inches(2.5), Inches(4.0)])

    doc.add_page_break()

    # ==================== SECTION 1: SELECTED SDG ====================
    doc.add_heading("1. Selected SDG and Reason for Selection", level=1)
    doc.add_heading("1.1 Overview of United Nations SDG 4 (Quality Education)", level=2)
    doc.add_paragraph(
        "In September 2015, the United Nations General Assembly adopted the 2030 Agenda for Sustainable Development, "
        "comprising 17 Sustainable Development Goals (SDGs). Among these, Sustainable Development Goal 4 (SDG 4) is formally defined as:"
    )
    add_callout(doc, "\"Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.\"",
                title="United Nations SDG 4 Mission Statement")
    doc.add_paragraph(
        "SDG 4 recognizes that high-quality education is the fundamental catalyst for enabling upward socioeconomic mobility, "
        "reducing inequality, and unlocking individual human potential. While primary education establishes foundational literacy, "
        "higher tertiary and technical education equip students with specialized cognitive, computational, and problem-solving "
        "competencies essential for modern industrial and knowledge economies."
    )

    doc.add_heading("1.2 Importance of Equal Access to Quality Education", level=2)
    doc.add_paragraph(
        "Equal access to educational support ensures that academic success is determined by intellectual merit rather than socioeconomic "
        "privilege or administrative familiarity. When academic guidance is confined to physical offices during limited 9 AM to 5 PM business "
        "hours, commuter, working, and first-generation learners face severe informational handicaps. Equalizing access through always-on "
        "conversational guidance directly dismantles these structural barriers."
    )

    doc.add_heading("1.3 Challenges in Accessing Academic Guidance", level=2)
    doc.add_paragraph(
        "Higher education students routinely encounter systemic obstacles when attempting to obtain academic guidance:\n"
        "• Severe Information Fragmentation: Guidelines, exam rules, and student services are dispersed across siloed websites and static PDFs.\n"
        "• Administrative Queuing Latency: Enrollment weeks and exams result in multi-day backlogs for academic advising desks.\n"
        "• Out-of-Hours Guidance Void: Students study and experience academic anxiety during evening and late-night hours when advising desks are closed.\n"
        "• Resource Discovery Friction: Many students remain unaware of accredited, government-funded open learning repositories (SWAYAM, NPTEL, NDLI)."
    )

    doc.add_heading("1.4 Relevance of CampusConnect AI to SDG 4", level=2)
    sdg_headers = ["SDG 4 Target", "International Mandate", "CampusConnect AI Direct Operationalization"]
    sdg_rows = [
        ["Target 4.3", "Equal access to affordable tertiary and technical education",
         "Provides 24/7 continuous guidance on degree requirements, course add/drop deadlines, and prerequisite rules, ensuring commuter and working students have identical access to advising."],
        ["Target 4.4", "Increase youth competencies and digital skills",
         "Delivers an ultra-lightweight, high-performance web application built with native web standards (HTML5/CSS3/Vanilla JS) that operates flawlessly on low-cost smartphones and weak networks."],
        ["Target 4.a", "Build and upgrade inclusive and safe learning facilities",
         "Instantly directs students to campus psychological counseling (CAPS), disability accommodations, peer tutoring centers, and emergency student financial relief funds."]
    ]
    add_custom_table(doc, sdg_headers, sdg_rows, col_widths=[Inches(1.2), Inches(2.3), Inches(3.0)])

    # ==================== SECTION 2: PROBLEM STATEMENT ====================
    doc.add_heading("2. Problem Statement", level=1)
    doc.add_paragraph(
        "In higher educational institutions, students must navigate a highly intricate operational environment governed by extensive "
        "academic regulations, prerequisite trees, examination ordinances, and student life policies. However, the systems used to communicate "
        "this information to students are fundamentally manual, fragmented, and latency-prone."
    )
    doc.add_heading("2.1 Operational Context & Affected Stakeholders", level=2)
    doc.add_paragraph(
        "This problem is prevalent across engineering colleges, universities, and technical institutes where administrative data is divided "
        "among isolated silos: the Registrar manages registration; the Examination Controller manages exam timetables and GPA scales; "
        "academic departments oversee prerequisites; and Student Affairs oversees hostels and counseling. Affected stakeholders include:\n"
        "1. Undergraduate & Graduate Students: Experiencing advising delays, missed add/drop deadlines, and severe exam anxiety.\n"
        "2. Faculty Advisors: Overburdened by repetitive transactional queries (e.g. 'How do I drop a class?').\n"
        "3. Administrative Staff: Facing overwhelming communication surges during semester milestones."
    )
    doc.add_heading("2.2 Limitations of Status Quo Channels", level=2)
    doc.add_paragraph(
        "Physical advising desks operate strictly during business hours, queues require physical presence, and institutional circulars "
        "are often published as non-searchable scanned PDFs. Left unaddressed, academic probation rates increase, student retention suffers, "
        "and administrative costs needlessly escalate."
    )

    # ==================== SECTION 3: PROPOSED SOLUTION ====================
    doc.add_heading("3. Proposed Solution", level=1)
    doc.add_paragraph(
        "CampusConnect AI pairs an accessible, dependency-free web portal with an authentic Botpress Cloud Generative AI assistant "
        "powered by Retrieval-Augmented Generation (RAG). The platform acts as a 24/7 digital academic advisor that answers student "
        "inquiries in natural language, grounding its outputs strictly in verified institutional documents."
    )
    doc.add_heading("3.1 System Architecture & Data Flow", level=2)
    add_code_box(doc,
"""Student Client (HTML5 / CSS3 / Vanilla JS)
  │
  ▼  (Official Webchat v3.7 Embed)
Botpress Cloud NLU & Autonomous Node
  │
  ▼  (Vector Similarity Search)
RAG Knowledge Base (/knowledge-base/*.md)
  │
  ▼  (Grounded Context Injection)
LLM Synthesis & Anti-Hallucination Guardrail
  │
  ▼  (Real-Time Streaming Response)
Student Webchat Interface""")

    doc.add_heading("3.2 Anti-Hallucination Guardrails", level=2)
    doc.add_paragraph(
        "To protect academic integrity, the agent enforces strict behavioral boundaries:\n"
        "• Refusal to Guess Dates/Fees: Explicitly directs students to official college portals for semester dates, tuition, and cutoffs.\n"
        "• Academic Integrity: Refuses to write complete graded assignments; instead explains concepts and outlines logic.\n"
        "• Scope Enforcement: Politely redirects non-academic queries back to collegiate guidance."
    )

    # ==================== SECTION 4: PROJECT FEATURES ====================
    doc.add_heading("4. Project Features", level=1)
    doc.add_paragraph(
        "The live production release incorporates 12 fully verified capabilities:\n"
        "1. Responsive Student Portal: Accessible Navy/Electric Blue SaaS layout fluid across 320px to 4K displays.\n"
        "2. Header Navigation & Mobile Drawer: Keyboard-accessible anchor navigation with animated mobile drawer.\n"
        "3. UN SDG Banner & Live Indicator: Real-time Botpress readiness badge reflecting cloud connectivity.\n"
        "4. High-Impact Hero Section: Interactive SaaS preview card showcasing sample queries and pipeline.\n"
        "5. Interactive Guidance Topic Search: Real-time client-side filter dynamically isolating support cards.\n"
        "6. Six Core Support Categories: Academic Support, Exam Rules, Study Planning, Resources, Admissions, Campus Life.\n"
        "7. Five Pre-Engineered Prompts: One-click interactive inquiry cards launching rich conversational sessions.\n"
        "8. Curated Knowledge Base Suite: Modular markdown files covering degree criteria, grading scales, and library commons.\n"
        "9. Official Botpress Webchat Integration: Direct embed of Webchat v3.7 with custom styling and event hooks.\n"
        "10. Natural Language Understanding: Interprets colloquial syntax, typos, and shorthand gracefully.\n"
        "11. Anti-Hallucination Guardrails: Strict refusal to guess official college schedules or fees.\n"
        "12. Real-User Telemetry: Edge-level Core Web Vitals monitoring ensuring sub-second load times."
    )

    # ==================== SECTION 5: TECHNOLOGY STACK ====================
    doc.add_heading("5. Technology Stack", level=1)
    tech_headers = ["Technology", "Layer", "Architectural Role & Justification"]
    tech_rows = [
        ["HTML5", "Markup & Semantics", "Semantic DOM landmarks, ARIA accessibility, WCAG 2.1 AA compliance."],
        ["CSS3", "Styling & Layout", "CSS Custom Properties, Flexbox, CSS Grid; zero utility framework overhead."],
        ["Vanilla JavaScript", "Client Logic", "DOM event binding, dynamic topic search filter, Botpress lifecycle sync."],
        ["Botpress Cloud", "Conversational AI", "Autonomous Node, NLU, dialogue management, LLM orchestration."],
        ["Botpress Knowledge Base", "RAG Vector Store", "Vector similarity retrieval over curated campus markdown documentation."],
        ["Botpress Webchat v3.7", "Chat Interface", "Slide-over drawer, typing indicators, secure HTTPS/WSS communication."],
        ["Git & GitHub", "Version Control", "Semantic commits, branch workflows, public open-source repository."],
        ["Edge Infrastructure", "Hosting & Telemetry", "SSL/TLS encryption, edge CDN caching, real-user Core Web Vitals tracking."]
    ]
    add_custom_table(doc, tech_headers, tech_rows, col_widths=[Inches(1.5), Inches(1.8), Inches(3.2)])

    # ==================== SECTION 6: SCREENSHOT PROOF OF WORK ====================
    doc.add_heading("6. Project Screenshots (Proof of Work)", level=1)
    doc.add_paragraph(
        "Screenshots represent mandatory proof of work verifying the authentic development and live production status of "
        "CampusConnect AI. In accordance with academic integrity guidelines, no synthetic mockups or AI-generated images are used. "
        "The 13 screenshots specified below document genuine application interactions across desktop, mobile, and cloud environments."
    )

    for i in range(1, 14):
        num_str = f"0{i}" if i < 10 else f"{i}"
        titles = [
            "Homepage and Navigation Overview",
            "Main Hero Section & SaaS Card Preview",
            "Platform Features Section",
            "Student Support Categories & Search Filter",
            "Actual Integrated Botpress Webchat Interface",
            "Real AI-Generated Conversational Response",
            "RAG Knowledge-Base-Supported Answering",
            "Study-Related Assistance Interaction",
            "Handling of Unknown Question (Anti-Hallucination Guardrail)",
            "Botpress Cloud Knowledge Base Configuration",
            "Botpress Autonomous Node Configuration & Agent Prompt",
            "Mobile Responsive Layout",
            "Live Production Website Deployment"
        ]
        add_screenshot_placeholder(
            doc, f"Figure 6.{i}", titles[i-1],
            f"screenshots/{num_str}-screenshot.png", "Production / Cloud Studio",
            "https://campus-connect-kohl-alpha.vercel.app/",
            f"Authentic visual evidence for {titles[i-1]}.",
            f"Demonstration of {titles[i-1]} within the live CampusConnect AI production environment."
        )

    # ==================== SECTION 7: OPEN SOURCE REPOSITORY ====================
    doc.add_heading("7. Open Source Repository", level=1)
    p_repo = doc.add_paragraph()
    p_repo.add_run("The complete source code, architectural documentation, Botpress configuration, and knowledge base repository "
                   "for CampusConnect AI are maintained publicly on GitHub:\n\n")
    p_repo.add_run("Official GitHub Repository: ").bold = True
    add_hyperlink(p_repo, "https://github.com/Immortal-syntax/CampusConnect", "https://github.com/Immortal-syntax/CampusConnect")
    doc.add_paragraph(
        "• Repository Identifier: Immortal-syntax/CampusConnect\n"
        "• Default Branch: main\n"
        "• License: MIT Open Source License\n"
        "• Hosting: GitHub Cloud Infrastructure"
    )

    # ==================== SECTION 8: FUTURE SCOPE & CONCLUSION ====================
    doc.add_heading("8. Future Scope & Conclusion", level=1)
    doc.add_paragraph(
        "Realistic enhancements for future iterations include:\n"
        "1. Multilingual Support: Regional vernacular language translation (Kannada, Hindi, Tamil, Telugu, Bengali).\n"
        "2. Voice Interface: Speech-to-Text and Text-to-Speech capabilities for hands-free and accessible interaction.\n"
        "3. Personalized Trajectories: Secure opt-in course enrollments to suggest customized weekly review timetables.\n"
        "4. Progressive Web App: Service Worker caching for home-screen installability and offline emergency access.\n"
        "5. Institutional ERP / SIS SSO: Authenticated queries for personal attendance and transcript credit audits.\n"
        "6. Human Advisor Escalation: Intelligent routing of sensitive student crises to counseling staff."
    )
    doc.add_paragraph(
        "Conclusion: CampusConnect AI demonstrates how Generative AI, when thoughtfully combined with standard web technologies "
        "and grounded in factual institutional knowledge, serves as an equitable digital assistant. By providing 24/7 academic advising, "
        "teaching evidence-based study methods, and connecting learners with verified open educational repositories, CampusConnect AI "
        "transforms the collegiate experience and makes a tangible contribution toward realizing United Nations Sustainable Development "
        "Goal 4: Quality Education."
    )

    # ==================== REFERENCES ====================
    doc.add_heading("References", level=1)
    refs = [
        ("United Nations. (2015). ", "Transforming our world: The 2030 Agenda for Sustainable Development. Resolution adopted by the General Assembly on 25 September 2015 (A/RES/70/1). United Nations Sustainable Development Goals. ", "https://sdgs.un.org/goals/goal4"),
        ("Botpress Inc. (2026). ", "Botpress Cloud Documentation: Autonomous Nodes, Knowledge Bases, and Webchat Integration. ", "https://botpress.com/docs"),
        ("World Wide Web Consortium (W3C). (2018). ", "Web Content Accessibility Guidelines (WCAG) 2.1. W3C Recommendation 05 June 2018. ", "https://www.w3.org/TR/WCAG21/"),
        ("Ministry of Education, Government of India. (2026). ", "SWAYAM: Study Webs of Active-Learning for Young Aspiring Minds. National Online Education Platform. ", "https://swayam.gov.in/"),
        ("National Programme on Technology Enhanced Learning (NPTEL). (2026). ", "NPTEL Online Courses and Certification. Joint Initiative of IITs and IISc. ", "https://nptel.ac.in/"),
        ("National Digital Library of India (NDLI). (2026). ", "Ministry of Education Digital Resource Repository. IIT Kharagpur. ", "https://ndl.iitkgp.ac.in/"),
        ("Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). ", "Improving Students' Learning With Effective Learning Techniques: Promising Directions From Cognitive and Educational Psychology. Psychological Science in the Public Interest, 14(1), 4–58. ", "https://doi.org/10.1177/1529100612453266"),
        ("Ebbinghaus, H. (1885). ", "Memory: A Contribution to Experimental Psychology. Teachers College, Columbia University (English translation, 1913). ", "https://psychclassics.yorku.ca/Ebbinghaus/"),
        ("CampusConnect AI Open Source Repository. (2026). ", "CampusConnect Project Team. ", "https://github.com/Immortal-syntax/CampusConnect")
    ]
    for prefix, title_text, url in refs:
        p_ref = doc.add_paragraph(style='List Bullet')
        p_ref.add_run(prefix)
        p_ref.add_run(title_text).italic = True
        add_hyperlink(p_ref, url, url)

    # Save Word document
    out_dir = os.path.dirname(os.path.abspath(__file__))
    docx_path = os.path.join(out_dir, "SDG_CampusConnectAI_Report.docx")
    pdf_path = os.path.join(out_dir, "SDG_CampusConnectAI_Report.pdf")
    doc.save(docx_path)
    print(f"[SUCCESS] Word document generated at: {docx_path}")

    # Export to PDF via Word COM Automation
    print(f"Exporting to PDF: {pdf_path}...")
    ps_command = f"""
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open('{docx_path}')
    $doc.ExportAsFixedFormat('{pdf_path}', 17)
    $doc.Close([ref]0)
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    """
    res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_command], capture_output=True, text=True, check=False)
    if os.path.exists(pdf_path):
        size = os.path.getsize(pdf_path)
        print(f"[SUCCESS] PDF generated successfully at: {pdf_path} ({size} bytes)")
    else:
        print(f"[WARNING] PDF export status: {res.stderr}")


if __name__ == "__main__":
    build_word_and_pdf()

