import streamlit as st
from utils import extract_text_from_pdf, calculate_match

st.set_page_config(page_title="Smart Resume Analyzer")

st.title("Smart Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    score, matched, missing = calculate_match(resume_text, job_description)

    st.subheader(f"ATS Match Score: {score}%")
    st.progress(int(score))

    if score >= 80:
        st.success("Excellent ATS match!")
    elif score >= 60:
        st.info("Moderate match. Can be improved.")
    else:
        st.warning("Low match. Add more relevant skills.")

    st.write("### Matched Keywords")
    st.write(", ".join(list(matched)[:30]))

    st.write("### Missing Keywords")
    st.write(", ".join(list(missing)[:30]))

    if missing:
        st.write("### Suggestions to Improve")
        st.write("Consider adding these important skills if relevant:")
        st.write(", ".join(list(missing)[:10]))