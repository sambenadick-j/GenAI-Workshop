import streamlit as st
import chains

def mcq_generator_app():
    """
    Generates MCQ Generator App with Streamlit, providing user input and displaying output.
    """
    st.title("Lets generate MCQ's! 👋")

    with st.form("mcq_generator"):
        subject = st.text_input("Enter a subject for the mcq:")
        submitted = st.form_submit_button("Submit")

        if submitted:
            response = chains.generate_mcq_chain(subject)
            st.info(response)
mcq_generator_app()
