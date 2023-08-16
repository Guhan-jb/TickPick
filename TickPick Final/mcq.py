import streamlit as st
import random
import json
def generate_mcqs(grade, subject):
    # Generate MCQs logic...
    with open(grade+'_'+subject+'.json') as file:
        data = json.load(file)
    subject_questions = data['questions']
    # Check if there are enough questions available
    if len(subject_questions) < 5:
        st.warning("Insufficient questions available for the selected grade and subject.")
        return []

    # Randomly select 10 questions from the subject
    mcqs = random.sample(subject_questions, k=5)

    return mcqs

# Main Streamlit app
def cqmain():
    st.title("Your Personal Tutor for Content")
    st.sidebar.title("Options")

    # Get user inputs for grade and subject
    grade = st.sidebar.selectbox("Select Grade", ["Grade 10","Grade 11","Grade 12"])
    subject = st.sidebar.selectbox("Select Subject", ["math","social","physics","biology","chemistry"])
    # Generate MCQs based on user inputs
    generate_mcqs_button = st.sidebar.button("Generate MCQs")
    if generate_mcqs_button:
        mcqs = generate_mcqs(grade, subject)

        # Check if there are enough MCQs available
        if not mcqs:
            st.warning("No MCQs available for the selected grade and subject.")
            return

        # Display the MCQs and get user answers
        st.header("Generated MCQs")
        user_answers = []
        for i, mcq in enumerate(mcqs):
            st.subheader(f"Question {i+1}:")
            st.write(mcq["question"])
            selected_option = st.radio(f"Answer {i+1}:", options=mcq["options"], key=f"answer_{i}")
            user_answers.append(selected_option)

        # Store the user answers in session state
        st.session_state.user_answers = user_answers
        st.session_state.show_score = False

    # Submit button to evaluate answers
    submit_button = st.sidebar.button("Submit")
    if submit_button:
        if "user_answers" in st.session_state:
            user_answers = st.session_state.user_answers

            # Check if user has answered all the questions
            if len(user_answers) != len(mcqs):
                st.warning("Please answer all the questions before submitting.")
                return

            score = 0
            st.session_state.show_score = True
        else:
            st.warning("Please generate MCQs before submitting.")

    # Calculate and display the total score
    if "show_score" in st.session_state and st.session_state.show_score:
        st.header("Result")
        if "user_answers" in st.session_state:
            user_answers = st.session_state.user_answers

            for i, (mcq, user_answer) in enumerate(zip(mcqs, user_answers)):
                st.subheader(f"Question {i+1}:")
                st.write(mcq["question"])
                st.write(f"Correct Answer: {mcq['answer']}")
                st.write(f"Your Answer: {user_answer}")
                if user_answer == mcq["answer"]:
                    score += 1
            st.sidebar.subheader("Total Score:")
            st.sidebar.write(f"{score} / {len(mcqs)}")


if __name__ == "_main_":
    cqmain()