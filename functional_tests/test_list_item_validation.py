from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from functional_tests.base import FunctionalTest
from unittest import skip


class NewVisitorTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        pass