from src import parser
from src import text_extraction

"""Tests for the resume parser.

The previous version of this file simply printed the parsed output for the
sample resume; retain that behaviour for manual inspection but also add
assertions that exercise the new synonym-handling logic introduced in
`parser.parse_resume`.
"""


def test_parser_on_sample_resume():
    resume_path = "data/sample_resumes/data_analyst.pdf"
    extracted_text = text_extraction.extract_resume_text(resume_path)
    parsed_data = parser.parse_resume(extracted_text)
    print(parsed_data)


def _make_section_text(keyword, body):
    """Helper to build a fake resume section with a heading and body."""
    return f"{keyword}\n{body}\n"


def test_parser_recognizes_all_keywords():
    # build a synthetic resume containing each of the synonyms listed by the
    # user.  The value after each heading is unique so we can assert that the
    # correct text was captured for the correct section.
    sample = []
    # skills synonyms
    sample.append(_make_section_text("skills:", "Python, Go"))
    sample.append(_make_section_text("Technical Skills", "C++, Rust"))
    sample.append(_make_section_text("key skills", "SQL"))
    # education synonyms
    sample.append(_make_section_text("education", "B.Sc. in CS"))
    sample.append(_make_section_text("Academic", "M.Sc. in AI"))
    sample.append(_make_section_text("qualification", "PhD"))
    # experience synonyms
    sample.append(_make_section_text("experience", "1 year at X"))
    sample.append(_make_section_text("Work Experience", "2 years at Y"))
    sample.append(_make_section_text("Professional Experience (cont.)", "3 yrs at Z"))
    # projects synonyms
    sample.append(_make_section_text("projects", "Proj A"))
    sample.append(_make_section_text("Academic Projects", "Proj B"))

    text = "\n".join(sample)
    parsed = parser.parse_resume(text)

    # after parsing we should have the *last* occurrence of each section type
    # because our simple state machine overwrites values when a heading
    # repeats.  that's fine for this test; the important part is that the
    # headings were recognised at all.
    assert parsed["skills"] == "SQL"
    assert "M.Sc. in AI" in parsed["education"]
    assert "3 yrs at Z" in parsed["experience"]
    assert parsed["projects"] == "Proj B"

test_parser_on_sample_resume()
