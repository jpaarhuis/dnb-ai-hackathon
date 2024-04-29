import streamlit as st


def collect_financial_data():
    st.subheader("Enter your financial details")

    # Collect financial inputs
    income = st.number_input("Monthly Income (€):", min_value=0.0, format="%.2f", step=100.0)
    expenses = st.number_input("Monthly Expenses (€):", min_value=0.0, format="%.2f", step=100.0)
    savings = st.number_input("Total Savings (€):", min_value=0.0, format="%.2f", step=100.0)
    debt = st.number_input("Total Debt (€):", min_value=0.0, format="%.2f", step=100.0)

    # Validate the inputs
    if expenses > income:
        st.error("Expenses cannot exceed income. Please adjust your values.")
        return None  # Returning None to indicate an error in input

    # Save inputs to session state if validation passes
    st.session_state['financial_data'] = {
        'income': income,
        'expenses': expenses,
        'savings': savings,
        'debt': debt
    }
    return income, expenses, savings, debt
