def interpret_score(score):
    if 80 <= score <= 100:
        return "Excellent match – your profile is a great fit for this role."
    elif 60 <= score < 80:
        return "Good match – your profile fits most requirements."
    elif 40 <= score < 60:
        return "Average match – you meet some key requirements."
    else:
        return "Low match – your profile differs significantly from requirements."


def generate_suggestions(missing_skills, score):
    if not missing_skills:
        return "Your resume matches the job requirements well."
    
    suggestions = "Add these skills to improve your match:\n"
    suggestions += ", ".join(missing_skills)
    
    if score < 40:
        suggestions += "\n\nYour profile differs significantly from the job requirements. Consider tailoring your resume."
    
    return suggestions