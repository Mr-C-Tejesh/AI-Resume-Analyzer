import streamlit as st
import os
import sys
import tempfile
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import text_extraction
from src import jd_processor
from src import parser
from src import matcher
from src import scorer

# Page configuration
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# Title and Subtitle
st.title("AI Resume Analyzer")
st.markdown("Analyze how well your resume matches a job description using NLP.")

st.divider()

# Section 1: Resume Upload
st.subheader("Section 1 — Resume Upload")
resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

resume_path = None
if resume_file:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_file.write(resume_file.getbuffer())
    resume_path = temp_file.name
    st.success(f"Resume uploaded: {resume_file.name}")

st.divider()

# Section 2: Job Description Input
st.subheader("Section 2 — Job Description Input")
job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder="Paste job description text..."
)

st.divider()

# Section 3: Analyze Button
st.subheader("Section 3 — Analyze")
analysis_done = False
if st.button("Analyze Resume", type="primary"):
    if not resume_path:
        st.error("Please upload a resume first.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        st.info("Analysis pipeline running...")

        resume_text = text_extraction.extract_resume_text(resume_path)
        parsed_data = parser.parse_resume(resume_text)
        skills = parsed_data.get("skills", "")
        resume_skills_list = parser.extract_skills(skills)
        jd_text = job_description
        jd_skills_list = parser.extract_skills(jd_text)
        missing_skills = matcher.get_missing_skills(resume_skills_list, jd_skills_list)
        jd_experience = parser.extract_experience_years(jd_text)
        resume_experience = parser.extract_experience_years(resume_text)
        final_score, skill_score, experience_score, text_similarity = matcher.calculate_final_score(resume_text, jd_text, resume_skills_list, jd_skills_list, resume_experience, jd_experience)
        score_interpretation = scorer.interpret_score(final_score)
        suggestions = scorer.generate_suggestions(missing_skills, final_score, resume_experience, jd_experience)

        st.success("Analysis complete!")
        analysis_done = True

st.divider()

# Section 4: Output Display
st.subheader("Section 4 — Results")

if analysis_done:

    # Match Score (Prominent)
    st.metric(label="Match Score", value=f"{final_score}%")
    st.write(f"**Category:** {score_interpretation}")

    st.divider()

    # Experience Comparison
    st.subheader("Experience Comparison")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Your Experience:** {resume_experience} years")

    with col2:
        st.write(f"**Required Experience:** {jd_experience} years")

    st.divider()

    # Missing Skills
    st.subheader("Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"• {skill}")
    else:
        st.write("No critical skills missing.")

    st.divider()

    # Suggestions
    st.subheader("Suggestions to improve your resume")
    st.write(suggestions)

else:
    st.info("Upload a resume and paste a job description, then click 'Analyze Resume' to see the results.")