import re


def parse_resume(text):
    """
    Parse resume text and extract sections: skills, education, experience, projects.
    Recognizes common synonyms for each section heading as defined by the
    keyword lists below. Returns a dictionary with the extracted section text.
    """

    # keywords that may appear in section headings (case insensitive)
    SKILL_KEYWORDS = ["skills", "technical skills", "key skills"]
    EDU_KEYWORDS = ["education", "academic", "qualification"]
    EXP_KEYWORDS = ["experience", "work experience", "professional experience"]
    PROJ_KEYWORDS = ["projects", "academic projects"]

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

    # prepare result structure with all categories
    result = {"skills": "", "education": "", "experience": "", "projects": ""}

    current_section = None
    # iterate through lines and switch context when a heading keyword is seen
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()

        matched_heading = False
        for keyword, section in keyword_to_section.items():
            if lower.startswith(keyword):
                # heading found; set new current_section
                current_section = section
                matched_heading = True
                # if there's text on the same line after the heading, capture it
                remainder = stripped[len(keyword):].lstrip(':').strip()
                if remainder:
                    result[current_section] += remainder + "\n"
                break
        if matched_heading:
            continue

        # if we are inside a section, append the line
        if current_section:
            result[current_section] += line + "\n"

    # strip whitespace from each section
    for k in result:
        result[k] = result[k].strip()

    # fallback for skills: try SUMMARY/Technologies if no explicit section
    if not result["skills"]:
        skills_set = set()
        tech_matches = re.findall(r'Technologies:\s*([^\n]+)', text, re.IGNORECASE)
        for match in tech_matches:
            skills_set.update([s.strip() for s in match.split(',')])
        summary_match = re.search(
            r'SUMMARY\s*([^\n]+(?:\n(?!PROFESSIONAL|EDUCATION)[^\n]+)*)',
            text,
            re.IGNORECASE,
        )
        if summary_match:
            skills_set.update([s.strip() for s in summary_match.group(1).split(',')])
        result["skills"] = ", ".join(sorted(skills_set))

    return result
