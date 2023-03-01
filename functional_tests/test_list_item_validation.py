from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from functional_tests.base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith vai para a página inicial e acidentalmente tenta enviar
        # um item de lista vazia. Ela pressiona Enter na caixa de entrada vazia
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # A página inicial é atualizada e há uma mensagem de erro dizendo
        # os itens da lista não podem ficar em branco
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "Você não pode fazer uma lista fazia"
        ))

        # Ela tenta novamente com algum texto para o item, que agora funciona
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversamente, ela agora decide enviar um segundo item da lista em branco
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "Você não pode fazer uma lista fazia"
        ))

        # E ela pode corrigi-lo preenchendo algum texto em
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
