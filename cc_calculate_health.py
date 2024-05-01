import streamlit as st

'''
This is step 3 of the app: calculating the user's financial health score based on their financial data.

Use all the financial data collected in the previous step to calculate the financial health score.
Show the score to the user and optionally add some basic commentary on their financial health.
'''


def step3_show_financial_health():
    st.subheader("Your Financial Health Score")

    # This component depends on the user having entered their financial data
    if 'financial_data' not in st.session_state:
        st.error("Financial data is missing. Please go back and enter your financial details.")
        return

    financial_data = st.session_state['financial_data']

    score = calculate_financial_health(
        financial_data['income'],
        financial_data['expenses'],
        financial_data['savings'],
        financial_data['debt']
    )
    category = interpret_score(score)

    st.session_state['financial_health'] = {
        'score': score,
        'category': category
    }

    display_financial_health(score, category)


def calculate_financial_health(income, expenses, savings, debt):
    # Basic financial health metrics
    debt_to_income_ratio = debt / income if income else 0
    savings_rate = savings / income if income else 0
    expenses_to_income_ratio = expenses / income if income else 0

    # Calculate financial health score
    # The formula here is illustrative; you might want to refine it based on your criteria
    score = 100 - (debt_to_income_ratio * 30) + (savings_rate * 50) - (expenses_to_income_ratio * 20)
    score = max(min(score, 100), 0)  # Ensure score is between 0 and 100

    return score


def interpret_score(score):
    # Interpret the financial health score
    if score >= 75: return "Excellent"
    elif score >= 50: return "Decent"
    elif score >= 25: return "Poor"
    else: return "Rubbish"


def display_financial_health(score, category):
    description = get_health_description(category)

    # Display results
    st.metric("Financial Health Score", f"{score:.2f}", category)
    st.info(description)

    financial_data = st.session_state['financial_data']
    st.write("Income:", financial_data['income'])
    st.write("Expenses:", financial_data['expenses'])
    st.write("Savings:", financial_data['savings'])
    st.write("Debt:", financial_data['debt'])


def get_health_description(category):
    # Define descriptions for each category
    descriptions = {
        "Excellent": "You are in great financial health! Keep up the good work!",
        "Decent": "Your financial health is good, but there's room for improvement.",
        "Poor": "Consider reviewing your financial habits to improve your health.",
        "Rubbish": "It's important to take immediate action to improve your financial situation."
    }

    return descriptions[category]