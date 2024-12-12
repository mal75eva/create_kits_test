from http.client import responses

import data
import sender_stand_request
from create_kits_tests.data import kit_body


#Функция, меняющая содержимое тела запроса
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

#Функция для позитивных проверок
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_user_kit(kit_body, sender_stand_request.get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


#Функция для негативных проверок
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_user_kit(kit_body, sender_stand_request.get_new_user_token())
    assert kit_response.status_code == 400

#Тест 1
def test_1_symbol_in_the_name_get_success_response():
    positive_assert("a")

#Тест 2
def test_511_symbols_in_the_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест 3
def test_0_symbol_in_the_name_get_error_response():
    negative_assert_code_400("")

#Тест 4
def test_512_symbols_in_the_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Тест 5
def test_english_symbols_in_the_name_get_success_response():
    positive_assert("QWErty")

#Тест 6
def test_russian_symbols_in_the_name_get_success_response():
    positive_assert("Мария")

#Тест 7
def test_special_symbols_in_the_name_get_success_response():
    positive_assert("'%@")

#Тест 8
def test_whitespace_in_the_name_get_success_response():
    positive_assert(" Человек и КО ")

#Тест 9
def test_numbers_in_the_name_get_success_response():
    positive_assert("123")

#Тест 10
def test_no_symbols_in_the_name_get_error_response():
    response = sender_stand_request.post_new_user_kit({}, sender_stand_request.get_new_user_token())
    assert response.status_code == 400

#Тест 11
def test_other_type_of_date_in_the_name_get_error_response():
    negative_assert_code_400(123)

