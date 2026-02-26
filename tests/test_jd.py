from src import jd_processor
from src import parser

jd_path = "data/job_descriptions/python_intern.txt"
jd_text = jd_processor.load_jd(jd_path)
skills = parser.extract_skills(jd_text)
print("Extracted skills from JD:")
print(skills)