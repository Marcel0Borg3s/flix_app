"""
Página de atores.
"""

import pandas as pd
import streamlit as st
from datetime import datetime
from actors.service import ActorService
from st_aggrid import AgGrid


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()
        
    if actors:
        st.write('Actors List:')
        """
        Usando o pandas para converter a lista de atores para um DataFrame;
        """
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('No actors found')

    st.subheader("Add New Actore")
    name = st.text_input("Name")
    birthday = st.date_input(
        label='Birthday',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = ['USA', 'UK', 'CAN', 'AUS']
    nationality = st.selectbox(
        label='Nationality',
        options=nationality_dropdown
    )
    if st.button("Add"):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.success(f"Actor {name} added successfully")
            st.rerun()
        else:
            st.error('Error creating actor')

