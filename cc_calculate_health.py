import streamlit as st


def show_financial_health():
    # This component depends on the user having entered their financial data
    if 'financial_data' in st.session_state:
        display_financial_health()
    else:
        st.error("Financial data is missing. Please go back and enter your financial details.")


def calculate_financial_health(income, expenses, savings, debt):
    # Basic financial health metrics
    debt_to_income_ratio = debt / income if income else 0
    savings_rate = savings / income if income else 0

    # Calculate a simple financial health score
    # The formula here is illustrative; you might want to refine it based on your criteria
    score = 100 - (debt_to_income_ratio * 50) + (savings_rate * 50)
    score = max(min(score, 100), 0)  # Ensure score is between 0 and 100

    return score


def interpret_score(score):
    # Interpret the financial health score
    if score >= 75:
        return "Excellent", "You are in great financial health! Keep up the good work!"
    elif score >= 50:
        return "Good", "Your financial health is good, but there's room for improvement."
    elif score >= 25:
        return "Fair", "Consider reviewing your financial habits to improve your health."
    else:
        return "Poor", "It's important to take immediate action to improve your financial situation."


def display_financial_health():
    st.subheader("Your Financial Health Score")

    if 'financial_data' not in st.session_state:
        st.warning("Please enter your financial data first.")
        return

    # Retrieve financial data from session state
    data = st.session_state['financial_data']
    score = calculate_financial_health(data['income'], data['expenses'], data['savings'], data['debt'])
    category, advice = interpret_score(score)

    # Display results
    st.metric("Financial Health Score", f"{score:.2f}", category)
    st.info(advice)
