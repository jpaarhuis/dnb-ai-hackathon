import streamlit as st

'''
This is step 4 of the app: providing personalized financial advice based on the user's financial health score.

Use the financial health score calculated in the previous step to provide personalized advice from the selected
movie character!
'''


def step4_show_character_advice():
    st.subheader("Personalized Advice from Your Financial Advisor")

    if 'financial_health' not in st.session_state or 'selected_character' not in st.session_state:
        st.error("Please ensure you have selected a character and entered your financial data.")
        return

    character = st.session_state['selected_character']
    financial_health = st.session_state['financial_health']

    advice = get_advice_by_character(character, financial_health['category'])

    # Save the advice in the session state
    st.session_state['character_advice'] = advice

    # Display the advice
    display_character_advice(character, advice)


def display_character_advice(character, advice):
    st.info(f"{character} says: \"{advice}\"")

    st.image(f"img/{character.lower().replace(' ', '_')}.jpg", caption=character, use_column_width=True)


def get_advice_by_character(character, category):
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

    return advice_templates[character][category]

