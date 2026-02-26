from src import text_extraction
from src import jd_processor
from src import parser
from src import matcher
from src import scorer

resume_path = "data/sample_resumes/software_engineer.pdf"
jd_path = "data/job_descriptions/software_intern.txt"

resume_text = text_extraction.extract_resume_text(resume_path)
parsed_data = parser.parse_resume(resume_text)
skills = parsed_data.get("skills", "")
resume_skills_list = parser.extract_skills(skills)

jd_text = jd_processor.load_jd(jd_path)
jd_skills_list = parser.extract_skills(jd_text)

missing_skills = matcher.get_missing_skills(resume_skills_list, jd_skills_list)

jd_experience = parser.extract_experience_years(jd_text)
resume_experience = parser.extract_experience_years(resume_text)

print(f"Resume Experience: {resume_experience} years")
print(f"JD Experience: {jd_experience} years")

final_score, skill_score, experience_score, text_similarity = matcher.calculate_final_score(resume_text, jd_text, resume_skills_list, jd_skills_list, resume_experience, jd_experience)

score_interpretation = scorer.interpret_score(final_score)
suggestions = scorer.generate_suggestions(missing_skills, final_score)

print(f"Final Match Score: {final_score:.2f}%")
print(f"Skill Match Score: {skill_score:.2f}%")
print(f"Experience Score: {experience_score:.2f}%")
print(f"Text Similarity Score: {text_similarity:.2f}%")
print(f"Score Interpretation: {score_interpretation}")
print(f"Suggestions:\n{suggestions}")