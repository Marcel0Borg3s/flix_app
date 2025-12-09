"""
Página de generos.
"""

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        "id": 1,
        "name": "Action",
    },
    {
        "id": 2,
        "name": "Comedy",
    },
    {
        "id": 3,
        "name": "Drama",
    },
    {
        "id": 4,
        "name": "Horror",
    },
    {
        "id": 5,
        "name": "Sci-Fi",
    },
    {
        "id": 6,
        "name": "Thriller",
    },
]


def show_genres():
    """
    Função para mostrar a pag. de Generos;
    Usando o st_aggrid para mostrar a tabela;
    Convertido (provisório, usando dados mocados) a lista de generos para um DataFrame;
    Função será trazer dados da API;
    """
    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
    )
    st.subheader("Add NewGenre")
    name = st.text_input("Name")
    if st.button("Add"):
        genres.append({"id": len(genres) + 1, "name": name})
        st.success(f"Genre {name} added successfully")
