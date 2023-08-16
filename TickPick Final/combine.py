import streamlit as st
from youtube import youmain
from summarize import spmain
from pdfsummerizer import pdfsummerizermain
from mcq import cqmain
from front import fmain


def main():
    
    st.title("TICK_PICK")
    st.subheader("Your Personalised Tutor")

    # Sidebar for app selection
    st.sidebar.title("Navigation")
    app_selection = st.sidebar.selectbox("Select Service", ["About","My Tutee","Text-Shorty", "You-Text","Idea-File-Compress"])

    # Display App 1
    
    if app_selection == "About":
         fmain()
    if app_selection == "My Tutee":
        cqmain()
    elif app_selection == "Text-Shorty":
         spmain()
        

    # Display App 2
    elif app_selection == "You-Text":
        youmain()
    # Display App 3
   

    elif app_selection == "Idea-File-Compress":
        pdfsummerizermain()
   

if __name__ == "__main__":
    main()
