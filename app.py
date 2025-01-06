import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from htmlTemplates import css, answer_template, question_template


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

def create_conversation(vector):

    llm = ChatGoogleGenerativeAI(model="models/llm-001")
    memory = ConversationBufferMemory(memory_key="pdf_conversation", return_messages=True)
    conversation = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector.as_retriever(),
        memory=memory
    )

    return conversation

def user_question(question):

    response = st.session_state.conversation({'question': question})
    st.write(response)


def main():
    load_dotenv()
    st.set_page_config(page_title="Upload Multiple PDFs and chat with them")

    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    st.header("Chat with PDFs Application")
    question = st.text_input("Ask anything about your PDFs:")
    
    if question:
        user_question(question)
    
    st.subheader("Upload PDFs")
    uploaded_files = st.file_uploader("Upload PDF files and click 'PROCESS'", accept_multiple_files=True)

    if st.button("PROCESS"):
        with st.spinner("Processing..."):
            # get text
            simple_text = get_text_from_pdf(uploaded_files)
            st.write(simple_text)

            # create chunks
            text_chunks = create_text_chunks(simple_text)

            # create vectors
            vector = create_vectors(text_chunks)

            # convo with vectors
            st.session_state.conversation = create_conversation(vector)
    

    


if __name__ == "__main__":
    main()