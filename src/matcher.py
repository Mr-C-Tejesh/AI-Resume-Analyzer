from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    """
    Calculate match score between resume and job description using TF-IDF + Cosine Similarity.
    
    Args:
        resume_text (str): Full resume text
        jd_text (str): Full job description text
    Returns:
        float: Match score between 0 and 100
    """
    documents = [resume_text, jd_text]
    
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    
    score = similarity * 100
    
    return score

def calculate_experience_score(resume_years, jd_years):

    if resume_years == 0 and jd_years > 0:
        return 0
    elif resume_years >= jd_years:
        return 100
    else:
        return (resume_years / jd_years) * 100

def calculate_final_score(resume_text, jd_text, resume_skills, jd_skills, resume_years, jd_years):

    # Step 1: Calculate skill score
    matched_skills = set(resume_skills) & set(jd_skills)  # intersection
    skill_score = (len(matched_skills) / len(jd_skills)) * 100 if jd_skills else 0

    # Step 2: Get experience score
    experience_score = calculate_experience_score(resume_years, jd_years)

    # Step 3: Calculate text similarity
    text_similarity = calculate_similarity(resume_text, jd_text)

    # Step 4: Calculate final score
    final_score = (0.7 * skill_score) + (0.2 * experience_score) + (0.1 * text_similarity)
    return final_score, skill_score, experience_score, text_similarity

def get_missing_skills(resume_skills, jd_skills):
    """
        Find skills required in job description that are missing from resume.
        
        Args:
            resume_skills (list): Skills extracted from resume
            jd_skills (list): Skills extracted from job description
        Returns:
            list: Skills in jd_skills but not in resume_skills"""
    
    resume_skills_lower = set(skill.lower() for skill in resume_skills)
    jd_skills_lower = set(skill.lower() for skill in jd_skills)
    missing_skills = list(jd_skills_lower - resume_skills_lower)
        
    return missing_skills
