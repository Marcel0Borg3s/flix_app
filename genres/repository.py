import requests
import streamlit as st
from login.service import logout


class GenreRepository:
    """
    Acessar a API e autenticar a aplicação no Bearer token
    """

    def __init__(self):
        self.__base_url = 'https://mborges76.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}/genres/'
        self.__headers ={
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        """
        Get nos Generos e checar a validade do token e se vencido, prazo de 1 dia, fará o kikoff do user
        """
        response = requests.get(
            self.__genres_url, 
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()

        raise Exception(f'Error to recive data from API. Status code {response.status_code}')

    def create_genre(self, genre):
        """
        Post nos Generos e checar a validade do token e se vencido, prazo de 1 dia, fará o kikoff do user
        """
        response = requests.post(
            self.__genres_url, 
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()

        raise Exception(f'Error to recive data from API. Status code {response.status_code}')

        
