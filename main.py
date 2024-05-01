import streamlit as st
from aa_characters import step1_select_characters
from bb_collect_data import step2_collect_financial_data
from cc_calculate_health import step3_show_financial_health
from dd_advice import step4_show_character_advice
from ee_results import step5_display_results

# Welcome to the Movie Character Financial Advisor app!

# This app helps you get financial advice from your favorite movie characters.
# The main function is already implemented for you, see the README on how to run it.
# Now it's your turn to complete the missing parts in the other Python files!
# Have fun and good luck!


def main():
    st.title("Movie Character Financial Advisor")

    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    steps = {
        1: step1_select_characters,
        2: step2_collect_financial_data,
        3: step3_show_financial_health,
        4: step4_show_character_advice,
        5: step5_display_results
    }

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Back") and st.session_state['current_step'] > 1:
            st.session_state['current_step'] -= 1
    with col3:
        if st.button("Next") and st.session_state['current_step'] < steps.__len__():
            st.session_state['current_step'] += 1
    with col2:
        st.write(f"Step {st.session_state['current_step']} of {steps.__len__()}")

    steps[st.session_state['current_step']]()


if __name__ == "__main__":
    main()
