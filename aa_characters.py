import streamlit as st

'''
This file contains the code for the first step of the app: selecting a financial advisor character.
There are 4 example characters to choose from, but feel free to add your own!
'''


def step1_select_characters():
    st.subheader("Select your Financial Advisor")

    characters = load_character_data()
    selected_character_name = display_character_selector(characters)
    show_character_details(characters, selected_character_name)

    # Save the selected character to session state for use in other components
    st.session_state['selected_character'] = selected_character_name


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


def display_character_selector(characters):
    # Streamlit widget to let the user select a character
    character_names = [char['name'] for char in characters]

    # Check if a character has already been selected
    default_index = character_names.index(st.session_state.get('selected_character', character_names[0]))
    selected_character_name = st.selectbox("Choose your financial advisor:", character_names, index=default_index)
    return selected_character_name


def show_character_details(characters, selected_character_name):
    # Display the details of the selected character
    selected_character = next(char for char in characters if char['name'] == selected_character_name)
    st.write(f"You selected: {selected_character['name']}")
    st.write(f"Description: {selected_character['description']}")
    st.image(selected_character['image'], width=400)  # Assuming images are stored in the same directory
