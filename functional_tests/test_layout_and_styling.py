from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from functional_tests.base import FunctionalTest

import time
import sys

MAX_WAIT = 10


class LayoutAndStylingTest(FunctionalTest):
    pass