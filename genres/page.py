"""
Página de generos.
"""

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    """
    Função para mostrar a pag. de Generos;
    Usando o st_aggrid para mostrar a tabela;
    Convertido (provisório, usando dados mocados) a lista de generos para um DataFrame;
    Função será trazer dados da API;
    """

    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Genres List: ')
        """
        Usando o pandas para converter a lista de generos para um DataFrame;
        """
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid',
        )

    else:
        st.warning('No genres found')

    st.subheader("Add NewGenre")
    name = st.text_input("Name")
    if st.button("Add"):
        new_genre = genre_service.create_genre(
            name=name,
        )
        if new_genre:
            st.success(f"Genre {name} added successfully")
            st.rerun()
        else:
            st.error('Error creating genre')

