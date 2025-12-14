from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document
import io


async def parse_resume(file: UploadFile) -> str:
    """
    Extract text from PDF or DOCX resume
    """
    contents = await file.read()

    if file.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(contents))
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif file.filename.endswith(".docx"):
        doc = Document(io.BytesIO(contents))
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        raise ValueError("Unsupported file format")
