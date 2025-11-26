"""
Módulo princial do app.
Inicia a interface do usuário e serve como frontend
para interagir com a API de backend.
"""

import streamlit as st
from genre.page import show_genres


def main():
    """
    Menu principal para mostrar a página selecionada.
    """
    st.title("Flix App")

    menu_option = st.sidebar.selectbox(
        'Select an option',
        ['Start', 'Genre', 'Actors', 'Movies', 'Reviews']

    )

    if menu_option == 'Start':
        st.write('Start')

    if menu_option == 'Genre':
        show_genres()

    if menu_option == 'Actors':
        st.write('Actors list')

    if menu_option == 'Movies':
        st.write('Movies list')

    if menu_option == 'Reviews':
        st.write('Reviews list')


if __name__ == "__main__":
    main()
