import streamlit as st
from aa_characters import select_characters
from bb_collect_data import collect_financial_data
from cc_calculate_health import show_financial_health
from dd_advice import show_character_advice
from ee_results import display_results


def main():
    st.title("Movie Character Financial Advisor")

    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    steps = {
        1: select_characters,
        2: collect_financial_data,
        3: show_financial_health,
        4: show_character_advice,
        5: display_results
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
