import requests
import streamlit as st 
from login.service import logout


class ActorRepository:

    def __init__(self):
        self.__base_url = 'https://mborges76.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers ={
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
                self.__actors_url,
                headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        raise Exception(f'Error to recive data from API. Status code {response.status_code}')
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error to recive data from API. Status code {response.status_code}')
    def get_actor(self, actor_id):
        response = requests.get(
                self.__actors_url,
                headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        raise Exception(f'Error to recive data from API. Status code {response.status_code}')


    def create_actor(self, actor):
        """
        Post nos Generos e checar a validade do token e se vencido, prazo de 1 dia, fará o kikoff do user
        """
        response = requests.post(
            self.__actors_url, 
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error to recive data from API. Status code {response.status_code}')


