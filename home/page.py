import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title("Welcome to the Stats Home Page")

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader("Movies by Genre")
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Movies by Genre Distribution'
        )
        st.plotly_chart(fig)

    st.subheader("Add Movies:")
    st.write(movie_stats['total_movies'])

    st.subheader("Movies by Genre:")
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader("Total Reviews:")
    st.write(movie_stats['total_reviews'])  

    st.subheader("Average Rating:")
    st.write(movie_stats['average_stars'])