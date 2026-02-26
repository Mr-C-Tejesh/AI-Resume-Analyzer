from src import parser
from src import text_extraction
resume_path = "data/sample_resumes/software_engineer.pdf"
extracted_text = text_extraction.extract_resume_text(resume_path)
parsed_data = parser.parse_resume(extracted_text)
skills = parsed_data.get("skills", "")
skills_list = parser.extract_skills(skills)
print("Extracted Skills:", skills_list)