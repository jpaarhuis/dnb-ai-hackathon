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
    st.info(f"{character} says: \"{advice}\"")

    # Display the characters image
    st.image(f"img/{character.lower().replace(' ', '_')}.jpg", caption=character, use_column_width=True)


def get_advice_by_character(character, score):
    # Define character-specific advice based on the score
    advice_templates = {
        "Gandalf": {
            "Excellent": "You have taken wise steps in your financial journey, much like preparing for a long quest.",
            "Decent": "You show much promise, young hobbit, but the road is long and fraught with peril.",
            "Poor": "Even the smallest person can change the course of the future, consider revising your financial habits.",
            "Rubbish": "Dark times lie ahead, prepare yourself by setting your accounts in order."
        },
        "Tony Stark": {
            "Excellent": "Your financial portfolio is as solid as Iron Man’s suit.",
            "Decent": "Looking good, but let’s tweak the arc reactor a bit for better performance.",
            "Poor": "Time to get back to the workshop and work on some upgrades.",
            "Rubbish": "Warning: System failure imminent! Time for serious financial repairs."
        },
        "Yoda": {
            "Excellent": "Strong in saving, you are.",
            "Decent": "Good, but commit you must, to more saving.",
            "Poor": "Clouded, your financial future is. Build up your savings, you should.",
            "Rubbish": "In great danger, your finances are. Restore balance, you must."
        },
        "Harry Potter": {
            "Excellent": "Brilliant! Your finances are as well-prepared as a N.E.W.T. exam.",
            "Decent": "Quite good, but remember, managing finances is not an exact science, unless you’re Arithmancy.",
            "Poor": "More study is needed. Perhaps a trip to Gringotts for some advice?",
            "Rubbish": "It’s like you’ve been confounded! Time to get serious about your financial health."
        }
    }

    # Retrieve the category of the score for character-specific advice
    category, _ = interpret_score(score)
    return advice_templates[character][category]

