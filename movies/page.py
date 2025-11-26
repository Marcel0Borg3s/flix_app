"""
Página de filmes.
"""

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        "id": 1,
        "name": "The Godfather",
    },
    {
        "id": 2,
        "name": "The Dark Knight",
    },
    {
        "id": 3,
        "name": "The Godfather: Part II",
    },
    {
        "id": 4,
        "name": "The Lord of the Rings: The Return of the King",
    },
    {
        "id": 5,
        "name": "Pulp Fiction",
    },
    {
        "id": 6,
        "name": "The Good, the Bad and the Ugly",
    },
]


def show_movies():
    """
    Função para mostrar a pag. de Filmes;
    Usando o st_aggrid para mostrar a tabela;
    Convertido (provisório, usando dados mocados) a lista de filmes para um DataFrame;
    Função será trazer dados da API;
    """
    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )
    st.subheader("Add NewMovie")
    name = st.text_input("Name")
    if st.button("Add"):
        movies.append({"id": len(movies) + 1, "name": name})
        st.success(f"Movie {name} added successfully")
