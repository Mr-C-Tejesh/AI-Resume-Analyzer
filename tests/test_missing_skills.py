from src import text_extraction
from src import jd_processor
from src import parser
from src import matcher

resume_path = "data/sample_resumes/data_analyst.pdf"
jd_path = "data/job_descriptions/python_intern.txt"

extracted_text = text_extraction.extract_resume_text(resume_path)
parsed_data = parser.parse_resume(extracted_text)
skills = parsed_data.get("skills", "")
resume_skills_list = parser.extract_skills(skills)

jd_text = jd_processor.load_jd(jd_path)
jd_skills_list = parser.extract_skills(jd_text)

missing_skills = matcher.get_missing_skills(resume_skills_list, jd_skills_list)
print("Missing Skills:", missing_skills)