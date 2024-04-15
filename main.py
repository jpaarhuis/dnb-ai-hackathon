import streamlit as st
from characters import select_characters
from collect_data import collect_financial_data
from calculate_health import show_financial_health
from advice import show_character_advice
from results import display_results


def main():
    st.title("Movie Character Financial Advisor App")

    select_characters()

    if "selected_character" not in st.session_state:
        st.write("Please start from the character selection.")
        return

    st.write(f"Advisor chosen: {st.session_state['selected_character']}")

    collect_financial_data()

    if "financial_data" not in st.session_state:
        return

    show_financial_health()
    show_character_advice()
    display_results()


if __name__ == "__main__":
    main()
