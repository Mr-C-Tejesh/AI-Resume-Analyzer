from src import text_extraction
from src import jd_processor
from src import parser
from src import matcher

resume_path = "data/sample_resumes/software_engineer.pdf"
jd_path = "data/job_descriptions/software_intern.txt"
resume_text = text_extraction.extract_resume_text(resume_path)
jd_text = jd_processor.load_jd(jd_path)

resume_skills = parser.extract_skills(resume_text)
jd_skills = parser.extract_skills(jd_text)

final_score, skill_score, text_similarity = matcher.calculate_final_score(resume_text, jd_text, resume_skills, jd_skills)

print(f"Final Match Score: {final_score:.2f}%")
print(f"Skill Match Score: {skill_score:.2f}%")
print(f"Text Similarity Score: {text_similarity:.2f}%")