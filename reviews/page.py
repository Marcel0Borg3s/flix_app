"""
Página de reviews.
"""

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        "id": 1,
        "stars": 1,
    },
    {
        "id": 2,
        "stars": 2,
    },
    {
        "id": 3,
        "stars": 3,
    },
    {
        "id": 4,
        "stars": 4,
    },
    {
        "id": 5,
        "stars": 5,
    },
    {
        "id": 6,
        "stars": 6,
    },
]


def show_reviews():
    """
    Função para mostrar a pag. de Reviews;
    Usando o st_aggrid para mostrar a tabela;
    Convertido (provisório, usando dados mocados) a lista de reviews para um DataFrame;
    Função será trazer dados da API;
    """
    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
    )
    st.subheader("Add NewReview")
    stars = st.number_input("Stars", min_value=1, max_value=5)
    if st.button("Add"):
        reviews.append({"id": len(reviews) + 1, "stars": stars})
        st.success(f"Review {stars} added successfully")
