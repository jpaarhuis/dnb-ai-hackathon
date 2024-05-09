import streamlit as st

'''
This is the final step of the app: summarizing everything and displaying the user's financial health overview.

This is the place to get crazy with visualizations, add more detailed advice, or even include some interactive elements!
'''


def step5_display_results():
    st.subheader("Financial Health Overview")

    if 'financial_data' not in st.session_state or 'selected_character' not in st.session_state:
        st.error("Please complete all previous steps.")
        return

    # Retrieve financial data and calculate the score
    financial_data = st.session_state['financial_data']
    character = st.session_state['selected_character']
    score = st.session_state['financial_health']['score']
    advice = st.session_state['character_advice']

    # Display the score with a dynamic progress bar
    st.write(f"Your Financial Health Score: {score:.2f}")
    progress_bar = st.progress(0)
    progress_bar.progress(score / 100)

    # Display the character-specific advice
    st.write(f"Advice from {character}:")
    st.info(f"{advice}")

    # Optional: Include visual enhancements or additional graphical representations
    # For example, display a chart of income vs. expenses
    st.bar_chart({"Income": [financial_data['income']], "Expenses": [financial_data['expenses']]})
