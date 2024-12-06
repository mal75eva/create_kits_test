import configuration
import requests
import data

#Создание пользователя
def create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json = body,
        headers = data.headers)

# Получение токена авторизации authToken
def get_new_user_token():
    response = create_new_user(data.user_body)
    return response.json()['authToken']

#Создание набора пользователя
def post_new_user_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers)


