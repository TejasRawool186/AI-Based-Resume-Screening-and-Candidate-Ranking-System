import streamlit as st
import pandas as pd
import pdfplumber
import re
import nltk
import plotly.express as px
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Function to extract text from PDFs
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    lemmatizer = WordNetLemmatizer()
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
    return " ".join(words)

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    
    job_description_vector = vectors[0].reshape(1, -1)
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity(job_description_vector, resume_vectors).flatten()
    
    return cosine_similarities

# Streamlit UI
st.title(":rainbow[AI based Resume Screening & Candidate Ranking System]")

# Job description input
st.header(":rainbow[Job Description]")
job_description = st.text_area("Enter the job description", height=200)

# Resume upload
st.header(":rainbow[Upload Resumes]")
uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

# Processing resumes
if uploaded_files and job_description:
    st.header(":rainbow[Ranking Resumes]")
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(preprocess_text(text))

    # Rank resumes
    scores = rank_resumes(preprocess_text(job_description), resumes)
    
    # Create results DataFrame
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)
    
    # Display ranking results
    st.write(results)
    
    # Download button for ranked resumes
    csv = results.to_csv(index=False).encode('utf-8')
    st.download_button("Download Ranking Results", csv, "ranking_results.csv", "text/csv")
    
    # Plot ranking chart
    fig = px.bar(results, x="Resume", y="Score", title="Resume Ranking", text_auto=True)
    st.plotly_chart(fig)
