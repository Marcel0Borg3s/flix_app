"""
Módulo princial do app.
Inicia a interface do usuário e serve como frontend
para interagir com a API de backend.
"""

import streamlit as st
from actors.page import show_actors
from genre.page import show_genres
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    """
    Confere se está logado e mostra o menu principal para mostrar a página selecionada.
    """
    if 'token' not in st.session_state:
        show_login()
    else:
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
            show_actors()

        if menu_option == 'Movies':
            show_movies()

        if menu_option == 'Reviews':
            show_reviews()


if __name__ == "__main__":
    main()
