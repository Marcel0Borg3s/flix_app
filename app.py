"""
Main module to run the Streamlit app.
This module start the app Streamlit and serve as frontend
for interacting with the backend flix_api.
"""

import streamlit as st


def main():
    """
    Main menu function to run the Streamlit app.
    """
    st.title("Flix App")

    menu_option = st.sidebar.selectbox(
        'Select an option',
        ['Start', 'Genre', 'Actors', 'Movies', 'Reviews']

    )

    if menu_option == 'Start':
        st.write('Start')

    if menu_option == 'Genre':
        st.write('Genre list')

    if menu_option == 'Actors':
        st.write('Actors list')

    if menu_option == 'Movies':
        st.write('Movies list')

    if menu_option == 'Reviews':
        st.write('Reviews list')


if __name__ == "__main__":
    main()
