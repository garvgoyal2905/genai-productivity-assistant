import streamlit as st
from transformers import pipeline

st.title("GenAI Productivity Assistant")
st.write("Summarize text, extract topics, and generate questions.")

text_input = st.text_area("Enter your text:")

if st.button("Generate Summary"):
    summarizer = pipeline("summarization", model="flan-t5-base")
    summary = summarizer(text_input, max_length=50, min_length=20, do_sample=False)
    st.write("Summary:")
    st.write(summary[0]['summary_text'])
