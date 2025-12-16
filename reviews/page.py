"""
Página de reviews.
"""

import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewService
from st_aggrid import AgGrid


def show_reviews():
    """
    Função para mostrar a pag. de Reviews;
    Usando o st_aggrid para mostrar a tabela;
    Função será trazer dados da API;
    """
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Reviews List:')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid',
        )
    else:
        st.warning('No reviews found')
    
    st.subheader("Add NewReview")

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_title = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Movie', list(movie_title.keys()))

    stars = st.number_input(
        label='Stars',
        min_value=1,
        max_value=5,
        step=1,
    )
    comment = st.text_area(
        label='Comment',
    )
    if st.button('Add Review'):
        new_review = review_service.create_review(
            movie=movie_title[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.success('Review added successfully')
            st.rerun()
        else:
            st.error('Failed to add review')