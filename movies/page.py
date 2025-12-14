"""
Página de filmes.
"""
import pandas as pd
import streamlit as st  
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    """
    Função para mostrar a pag. de Filmes;
    Usando o st_aggrid para mostrar a tabela;
    Função será trazer dados da API;
    """
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Films list:')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])

        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('No movies found.')

    # Cadastrar novo filmes
    st.subheader("Add NewMovie")

    title = st.text_input('Title')

    release_date = st.date_input(
        label='relase date',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Genre', list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect('Actors', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_name]

    resume = st.text_area('Preview')

    if st.button('Add'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Wrong to add new movie. See the fields')

