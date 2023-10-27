import time
import pytest
from selenium.webdriver.common.by import By
import pytest_check as check
import PageObjects
import BaseApp
from PageObjects import Question_Program
import allure
from allure_commons.types import AttachmentType




@pytest.mark.usefixtures('setup')
class TestMain:

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("фильтр по цветам")
    def test_section(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_section_question()
        first_question.do_section_question()
        first_question.do_section_question()
        first_question.do_section_question()
        check.equal(self.driver.current_url, "https://www.salita.ru/zhenshchinam/obuv/")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("добавить в избранное выбранный товар")
    def test_favorite(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_favorite_question()
        first_question.do_favorite_question()
        first_question.do_favorite_question()
        check.equal(self.driver.current_url, "https://www.salita.ru/favorites/")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Регистрация пользователя")
    def test_registr(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_registration_question("Оксана","+79207776688","dz8ms@yandex.ru","Qwerty.")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Геолокация магазинов")
    def test_shops(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_shop_question()
        check.equal(self.driver.current_url, "https://www.salita.ru/shops/")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Вход пользователя")
    def test_entrance(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_entrance_question("dz8ms@yandex.ru", "Qwerty.")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Тест строки поиска")
    def test_find(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_find_question()
        first_question.do_find_question("сапоги\n")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Негативный сценарий теста строки поиска")
    def test_findnegativ(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_findnegativ_question()
        first_question.do_findnegativ_question("123456\n")
        check.equal(self.driver.current_url, "https://www.salita.ru/?q=123456")


    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Таблица размеров")
    def test_kartopen(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_kartopen_question()
        first_question.do_kartopen_question()
        first_question.do_kartopen_question()
        check.equal(self.driver.current_url, "https://www.salita.ru/zhenshchinam/odezhda/dzhempery/658957/")

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Поиск конкретного товара и его открытие в новом окне")
    def test_newwindow(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_newwindow_question()
        first_question.do_newwindow_question("брюки женские BOSS\n")
        first_question.do_newwindow_question()

    @allure.feature("Тест интернет-магазина Salita")
    @allure.story("Тест навигации главной страницы")
    @allure.description("Фильтр сортировки и тест кнопки сбросить")
    def test_filter(self):
        first_question = Question_Program(self.driver)
        first_question.go_to_site()
        first_question.do_filter_question()
        first_question.do_filter_question()
        first_question.do_filter_question()
        first_question.do_filter_question()
        check.equal(self.driver.current_url, "https://www.salita.ru/zhenshchinam/odezhda/filter/clear/apply/")