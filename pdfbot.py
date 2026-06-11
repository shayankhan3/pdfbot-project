import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from pypdf import PdfReader


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("PDF Q&A Bot")
st.caption("Upload PDF,Ask question!..")

upload_file= st.file_uploader("PDF upload here ",type="pdf")

if upload_file:
    reader = PdfReader(upload_file)
    text=""
    for page in reader.pages:
        text+= page.extract_text()

    st.success("PDF parh liya! ab sawaal poocho. ") 

    question = st.text_input("Apna sawaal likho :")   

    if question:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"system",
                    "content":f"this the content of pdf:\n\n{text}\n\nSirf is content ke basis pe jawab do."
                },
                {
                    "role":"user",
                    "content":question
                }


            ]


        )
        st.write("### jawab:")
        st.write(response.choices[0].message.content)