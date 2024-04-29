import streamlit as st
from dd_advice import get_advice_by_character
from cc_calculate_health import calculate_financial_health


def display_results():
    st.subheader("Financial Health Overview")

    if 'financial_data' not in st.session_state or 'selected_character' not in st.session_state:
        st.error("Please complete all previous steps.")
        return

    # Retrieve financial data and calculate the score
    data = st.session_state['financial_data']
    score = calculate_financial_health(data['income'], data['expenses'], data['savings'], data['debt'])
    advice = get_advice_by_character(st.session_state['selected_character'], score)

    # Display the score with a dynamic progress bar
    st.write("Your Financial Health Score:")
    progress_bar = st.progress(0)
    progress_bar.progress(score / 100)

    # Display the character-specific advice
    st.write(f"Advice from {st.session_state['selected_character']}:")
    st.info(f"{advice}")

    # Optional: Include visual enhancements or additional graphical representations
    # For example, display a chart of income vs. expenses
    st.bar_chart({"Income": [data['income']], "Expenses": [data['expenses']]})

