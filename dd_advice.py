import streamlit as st
from cc_calculate_health import calculate_financial_health, interpret_score


def show_character_advice():
    st.subheader("Personalized Advice from Your Financial Advisor")

    if 'financial_data' in st.session_state and 'selected_character' in st.session_state:
        display_character_advice()
    else:
        st.error("Please ensure you have selected a character and entered your financial data.")


def display_character_advice():
    # Retrieve the selected character and financial score
    character = st.session_state['selected_character']
    data = st.session_state['financial_data']
    score = calculate_financial_health(data['income'], data['expenses'], data['savings'], data['debt'])
    advice = get_advice_by_character(character, score)

    # Display the advice
    st.write(f"{character} says: \"{advice}\"")


def get_advice_by_character(character, score):
    # Define character-specific advice based on the score
    advice_templates = {
        "Gandalf": {
            "Excellent": "You have taken wise steps in your financial journey, much like preparing for a long quest.",
            "Good": "You show much promise, young hobbit, but the road is long and fraught with peril.",
            "Fair": "Even the smallest person can change the course of the future, consider revising your financial habits.",
            "Poor": "Dark times lie ahead, prepare yourself by setting your accounts in order."
        },
        "Tony Stark": {
            "Excellent": "Your financial portfolio is as solid as Iron Man’s suit.",
            "Good": "Looking good, but let’s tweak the arc reactor a bit for better performance.",
            "Fair": "Time to get back to the workshop and work on some upgrades.",
            "Poor": "Warning: System failure imminent! Time for serious financial repairs."
        },
        "Yoda": {
            "Excellent": "Strong in saving, you are.",
            "Good": "Good, but commit you must, to more saving.",
            "Fair": "Clouded, your financial future is. Build up your savings, you should.",
            "Poor": "In great danger, your finances are. Restore balance, you must."
        },
        "Harry Potter": {
            "Excellent": "Brilliant! Your finances are as well-prepared as a N.E.W.T. exam.",
            "Good": "Quite good, but remember, managing finances is not an exact science, unless you’re Arithmancy.",
            "Fair": "More study is needed. Perhaps a trip to Gringotts for some advice?",
            "Poor": "It’s like you’ve been confounded! Time to get serious about your financial health."
        }
    }

    # Retrieve the category of the score for character-specific advice
    category, _ = interpret_score(score)
    return advice_templates[character][category]

