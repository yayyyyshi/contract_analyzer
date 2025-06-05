import streamlit as st
from model_utils import get_qa_pipeline, get_summarizer
from analyzer import analyze_contract, summarize_contract

# Load models
qa_pipeline = get_qa_pipeline()
summarizer = get_summarizer()

st.title("🤖 Contract Analyzer with Hugging Face")

# Load contract
contract_text = open("sample_contract.txt", "r", encoding="utf-8").read()

# Display contract preview
with st.expander("📄 View Contract Text"):
    st.write(contract_text)

# Option to ask questions
st.subheader("🔍 Ask a Question about the Contract")
user_question = st.text_input("Enter your question:")

if st.button("Get Answer") and user_question:
    answer = analyze_contract(contract_text, user_question, qa_pipeline)
    st.success(f"**Answer:** {answer['answer']}")

# Option to summarize
if st.button("Summarize Contract"):
    st.subheader("📝 Summary")
    summary = summarize_contract(contract_text, summarizer)
    st.write(summary)
