from src import parser
from src import text_extraction


resume_path = "data/sample_resumes/data_analyst.pdf"
extracted_text = text_extraction.extract_resume_text(resume_path)
parsed_data = parser.parse_resume(extracted_text)
print(parsed_data)


