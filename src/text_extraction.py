import os
from pathlib import Path
from typing import Union
import PyPDF2
from docx import Document

def extract_resume_text(file_path: Union[str, Path]) -> str:
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_extension = file_path.suffix.lower()
    
    if file_extension == ".pdf":
        return _extract_from_pdf(file_path)
    elif file_extension == ".docx":
        return _extract_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}. Use PDF or DOCX.")


def _extract_from_pdf(file_path: Path) -> str:
    try:
        text = []
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text.append(page.extract_text())
    
        return "\n".join(text).strip()
    except ImportError:
        raise ImportError("PyPDF2 not installed. Run: pip install PyPDF2")


def _extract_from_docx(file_path: Path) -> str:
    """Extract text from DOCX file."""
    try:
        doc = Document(file_path)
        text = [paragraph.text for paragraph in doc.paragraphs]
        
        return "\n".join(text).strip()
    except ImportError:
        raise ImportError("python-docx not installed. Run: pip install python-docx")
    
