import streamlit as st

'''
This file contains the code for the first step of the app: selecting a financial advisor character.
There are 4 example characters to choose from, but feel free to add your own!
'''


def step1_select_characters():
    st.subheader("Select your Financial Advisor")

    st.write("TODO")

    characters = load_character_data()

    # Hint: use st.selectbox to allow the user to select a character
    # Hint: display the selected characters info
    # Hint: store the selected character in the session state for later use


def load_character_data():
    # This function returns a list of dictionaries, each containing details about a character
    return [
        {
            "name": "Gandalf",
            "image": "img/gandalf.jpg",
            "description": "Wise and prudent, offering sage advice on risk and reward."
        },
        {
            "name": "Tony Stark",
            "image": "img/tony_stark.jpg",
            "description": "Tech-savvy and innovative, providing cutting-edge financial strategies."
        },
        {
            "name": "Yoda",
            "image": "img/yoda.jpg",
            "description": "Ancient wisdom on long-term investment and patience."
        },
        {
            "name": "Harry Potter",
            "image": "img/harry_potter.jpg",
            "description": "Smart and practical, focusing on safe and steady growth."
        }
    ]

