import re
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

skill_dict = {
    "programming": [
        "python", "java", "c", "c++", "c#", "javascript", "typescript",
        "go", "ruby", "php", "r", "matlab", "kotlin", "swift"
    ],

    "data": [
        "sql", "mysql", "postgresql", "mongodb",
        "pandas", "numpy", "scipy",
        "machine learning", "deep learning",
        "data analysis", "data visualization",
        "power bi", "tableau", "excel",
        "statistics"
    ],

    "web": [
        "html", "css", "bootstrap", "tailwind",
        "react", "angular", "vue",
        "node", "express",
        "django", "flask",
        "rest api", "graphql"
    ],

    "tools": [
        "git", "github", "gitlab",
        "docker", "kubernetes",
        "linux", "bash", "shell scripting",
        "jira", "postman"
    ],

    "cloud_devops": [
        "aws", "azure", "google cloud",
        "ci/cd", "jenkins", "terraform"
    ]
}



def parse_resume(text):
    """
    Parse resume text and extract sections: skills, education, experience, projects.
    Rule-based detection using section keywords.
    """

    # keywords that may appear in section headings (case insensitive)
    SKILL_KEYWORDS = ["skills", "technical skills", "key skills"]
    EDU_KEYWORDS = ["education", "academic", "qualification"]
    EXP_KEYWORDS = ["experience", "work experience", "professional experience"]
    PROJ_KEYWORDS = ["projects", "academic projects"]
    CERT_KEYWORDS = ["certification", "certifications"]

    # map normalized keyword -> target section name
    keyword_to_section = {}
    for k in SKILL_KEYWORDS:
        keyword_to_section[k] = "skills"
    for k in EDU_KEYWORDS:
        keyword_to_section[k] = "education"
    for k in EXP_KEYWORDS:
        keyword_to_section[k] = "experience"
    for k in PROJ_KEYWORDS:
        keyword_to_section[k] = "projects"
    for k in CERT_KEYWORDS:
        keyword_to_section[k] = None

    # prepare result structure
    result = {
        "skills": "",
        "education": "",
        "experience": "",
        "projects": ""
    }

    current_section = None

    # process text line by line
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()

        if not stripped:
            continue  # skip empty lines

        matched_heading = False

        # check if this line is a section heading
        for keyword, section in keyword_to_section.items():
            # matches:
            # "Skills"
            # "Skills:"
            # "TECHNICAL SKILLS"
            # but NOT "I have good skills in Python"
            pattern = rf"^{re.escape(keyword)}\s*:?\s*$"
            if re.match(pattern, lower):
                current_section = section
                matched_heading = True
                break

        if matched_heading:
            continue

        # append content if inside a section
        if current_section:
            result[current_section] += stripped + "\n"

    # strip extra whitespace
    for k in result:
        result[k] = result[k].strip()

    # fallback for skills (your original logic)
    if not result["skills"]:
        skills_set = set()

        tech_matches = re.findall(
            r'Technologies:\s*([^\n]+)',
            text,
            re.IGNORECASE
        )
        for match in tech_matches:
            skills_set.update([s.strip() for s in match.split(',')])

        summary_match = re.search(
            r'SUMMARY\s*([^\n]+(?:\n(?!PROFESSIONAL|EDUCATION)[^\n]+)*)',
            text,
            re.IGNORECASE,
        )
        if summary_match:
            skills_set.update(
                [s.strip() for s in summary_match.group(1).split(',')]
            )

        result["skills"] = ", ".join(sorted(skills_set))

    return result

def extract_skills(skills_text):
    if not skills_text:
        return []

    # Convert to lowercase
    skills_text = skills_text.lower()

    # Run spaCy
    doc = nlp(skills_text)

    # Convert doc back to text (cleaned by spaCy)
    processed_text = doc.text

    matched_skills = []

    for category, skills in skill_dict.items():
        for skill in skills:
            if skill in processed_text:
                matched_skills.append(skill)

    # remove duplicates
    return list(set(matched_skills))