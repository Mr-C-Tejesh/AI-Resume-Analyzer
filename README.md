# AI Resume Analyzer

An NLP-powered web app that scores resumes against job descriptions and suggests improvements.

**Live Demo:** https://ai-resume-analyzer-sp7bqre3htdhzjq6u66psd.streamlit.app/

---

## Features

- Upload resume in PDF or DOCX format
- Paste any job description
- Extracts skills and years of experience
- Calculates match score using skill matching, experience matching, and TF-IDF text similarity
- Identifies missing skills
- Provides actionable resume improvement suggestions

## Tech Stack

- **Language:** Python
- **NLP:** spaCy
- **Text Similarity:** TF-IDF (scikit-learn)
- **UI & Deployment:** Streamlit

## Screenshots

<img width="1832" height="901" alt="image" src="https://github.com/user-attachments/assets/37f09cca-7c72-4803-8687-7b9a1559726e" />

<img width="1275" height="925" alt="image" src="https://github.com/user-attachments/assets/5c544a5e-a6c6-4190-a666-8c009533aec1" />

## Getting Started
```bash
git clone https://github.com/Mr-C-Tejesh/AI-Resume-Analyzer
cd AI-Resume-Analyzer
pip install -r requirements.txt
streamlit run app/main.py
```

---

Built by [Tejesh C](mailto:tejeshc17@gmail.com)
