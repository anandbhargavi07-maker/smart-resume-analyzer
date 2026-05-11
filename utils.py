import PyPDF2
import re

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text.lower()


def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)


def calculate_match(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords

    score = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

    return round(score, 2), matched, missing
def extract_keywords(text):
    stopwords = {
        "the", "and", "or", "in", "on", "at", "a", "an", "with",
        "for", "to", "of", "is", "are", "by", "this", "that"
    }

    words = re.findall(r'\b\w+\b', text.lower())

    return set(word for word in words if word not in stopwords and len(word) > 2)