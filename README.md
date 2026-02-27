# AI Resume Analyzer (NLP)

An AI-powered web application that analyzes resumes against job descriptions and provides a match score along with improvement suggestions.

## Live Demo

https://ai-resume-analyzer-sp7bqre3htdhzjq6u66psd.streamlit.app/

## Features

* Upload Resume (PDF / DOCX)
* Paste Job Description
* Extracts:

  * Skills
  * Experience (years)
* Calculates Match Score using:

  * Skill Matching
  * Experience Matching
  * NLP-based Text Similarity
* Identifies Missing Skills
* Provides Resume Improvement Suggestions

## Tech Stack

* Python
* NLP: spaCy
* Text Similarity: TF-IDF (scikit-learn)
* Streamlit (UI & Deployment)

## Project Structure

```
app/        -> Streamlit UI  
src/        -> Core logic (parser, matcher, scorer)  
```

## How It Works

1. Extract text from resume
2. Parse skills and experience
3. Extract requirements from Job Description
4. Calculate weighted match score
5. Display missing skills and suggestions

## Future Improvements

* Semantic matching using Sentence Transformers
* Multiple resume ranking
* ATS-style resume feedback
