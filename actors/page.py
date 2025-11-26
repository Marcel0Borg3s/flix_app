"""
Página de atores.
"""

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        "id": 1,
        "name": "Tom Hanks",
    },
    {
        "id": 2,
        "name": "Leonardo DiCaprio",
    },
    {
        "id": 3,
        "name": "Meryl Streep",
    },
    {
        "id": 4,
        "name": "Morgan Freeman",
    },
    {
        "id": 5,
        "name": "Meryl Streep",
    },
    {
        "id": 6,
        "name": "Morgan Freeman",
    },
]


def show_actors():
    """
    Função para mostrar a pag. de Atores;
    Usando o st_aggrid para mostrar a tabela;
    Convertido (provisório, usando dados mocados) a lista de generos para um DataFrame;
    Função será trazer dados da API;
    """
    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )
    st.subheader("Add New Actor")
    name = st.text_input("Name")
    if st.button("Add"):
        actors.append({"id": len(actors) + 1, "name": name})
        st.success(f"Actor {name} added successfully")
