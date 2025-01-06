import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Upload Multiple PDFs and chat with them")
    
    st.subheader("Upload PDFs")
    uploaded_files = st.file_uploader("Upload PDF files and click 'PROCESS'", accept_multiple_files=True)

    st.button("PROCESS")

    st.header("Chat with PDFs")
    st.text_input("Ask anything about your PDFs:")


if __name__ == "__main__":
    main()