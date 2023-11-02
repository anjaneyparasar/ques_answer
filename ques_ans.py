import streamlit as st
from transformers import pipeline  #pip install transformers

model=pipeline(task='question-answering')

st.title("Question Anwering Model")
st.text("This model uses transformers.")
st.sidebar.text("This model is based on the default hugging face question answering model. It works by giving the context and the query")

def main():
	context=st.text_area("Enter Context here:")
	query=st.text_input("Enter Query here: ")
	if context and query:
		answer = model(question=query, context=context)
		st.text(answer["answer"])

main()
#streamlit run "D:\KMV\NLP\Ques answering project\ques_ans.py"