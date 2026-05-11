## Live Demo
[Click Here to Try the App](https://smart-resume-analyzer-8eyslg4wzu2skstrpw4vsx.streamlit.app)

# Smart Resume Analyzer

A Python + Streamlit-based Smart Resume Analyzer that compares resumes with job descriptions, calculates ATS match scores, identifies missing keywords, and provides skill-gap suggestions for better job alignment.

---

## Features
- Upload Resume in PDF format
- Paste Job Description
- ATS Match Score Calculation
- Matched Keywords Detection
- Missing Skills Identification
- Resume Improvement Suggestions

---

## Tech Stack
- Python
- Streamlit
- PyPDF2
- Regular Expressions (Regex)
- Basic NLP

---

## How It Works
1. Upload your resume (PDF)
2. Paste a target job description
3. The system extracts resume text
4. Compares job keywords with resume keywords
5. Calculates ATS score
6. Suggests missing skills for improvement

---

## Installation
```bash
pip install -r requirements.txt
streamlit run app.py

