import pdfplumber
import streamlit as st
from openai import OpenAI
import io
client = OpenAI(api_key='your_api')
def search_openai(query,num=5):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=query
    )
    return response.choices[0].text.strip()
def summarize_pdf(file_path, num_sentences=3):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    st.write("Text from the document: ")
    st.write(text)
    summary = search_openai("summerize this text and the number of sentences are 5 :"+text)
    return summary

def pdfsummerizermain():
    st.title("Idea-File-Compress")
    # File uploader widget
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        # Convert the bytes object to a file-like object
        file_obj = io.BytesIO(uploaded_file.read())
        # Process the PDF contents and generate summary
        summary = summarize_pdf(file_obj)
        st.write("Summerized text:")
        st.write(summary)
if __name__=='__main__':
    pdfsummerizermain()
