import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth import get_user_model
from selenium.webdriver.chrome.options import Options

class AccountsLoginTest(StaticLiveServerTestCase):


    @classmethod
    def setUpClass(self):
        super().setUpClass()
        CHROME_BIN = "/usr/local/bin/chrome"
        CHROME_DRIVER = os.path.expanduser('/usr/local/bin/chromedriver')
        options = Options()
        options.binary_location = CHROME_BIN
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.selenium = webdriver.Chrome(CHROME_DRIVER, options=options)
        self.selenium.implicitly_wait(10)
        User = get_user_model()
        User.objects.create_user(username="test", password="test1234")

    @classmethod
    def tearDownClass(self):
        self.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        self.selenium.find_element_by_name("username").send_keys('test')
        self.selenium.find_element_by_name("password").send_keys('test1234')
        self.selenium.find_element_by_xpath('//button').click()
        self.assertEquals('Jail List', self.selenium.title)