import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


def get_text_from_pdf(uploaded_files):
    text = ""
    for pdf in uploaded_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def create_text_chunks(text):
    
    # text_chunks = []
    # #split text into chunks of 1000 characters
    # for i in range(0, len(text), 1000):
    #     text_chunks.append(text[i:i+1000])
    # return text_chunks

    text_splitter = CharacterTextSplitter(
        separator=".",
        chunk_size=1000,
        chunk_overlap=100,
        length_function = len
    )
    text_chunks = text_splitter.split_text(text)
    return text_chunks

def create_vectors(text_chunks):

    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vector_store





def main():
    load_dotenv()
    st.set_page_config(page_title="Upload Multiple PDFs and chat with them")

    st.header("Chat with PDFs Application")
    st.text_input("Ask anything about your PDFs:")
    
    st.subheader("Upload PDFs")
    uploaded_files = st.file_uploader("Upload PDF files and click 'PROCESS'", accept_multiple_files=True)

    if st.button("PROCESS"):
        with st.spinner("Processing..."):
            #get text
            simple_text = get_text_from_pdf(uploaded_files)

            #create chunks
            text_chunks = create_text_chunks(simple_text)

            #create vectors
            vector = create_vectors(text_chunks)
            st.write(vector)


    


if __name__ == "__main__":
    main()