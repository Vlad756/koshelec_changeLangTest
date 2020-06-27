import unittest
from selenium import webdriver
import time


class ChangeLang(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://coinmarketcap.com')

    def test_German(self):
        try:
            # находим и нажимаем кнопку для выбора языков
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            # находим меню сайта
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            # кнопка выбора языка
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        # находим необходимый язык
        lang = self.driver.find_element_by_link_text('Deutsch')
        lang.click()
        time.sleep(5)
        # проверяем, поменялся ли язык на заданный
        assert 'Top 100 Kryptowährungen nach Börsenwert' in self.driver.page_source

    def test_English(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('English')
        lang.click()
        time.sleep(5)
        assert 'Top 100 Cryptocurrencies by Market Capitalization' in self.driver.page_source

    def test_Spanish(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Español')
        lang.click()
        time.sleep(5)
        assert 'Principales 100 Criptomonedas por capitalización de mercado' in self.driver.page_source

    def test_Filipino(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Filipino')
        lang.click()
        time.sleep(5)
        assert 'Nangungunang 100 Mga Cryptocurrency ng Market Capitalization' in self.driver.page_source

    def test_French(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Français')
        lang.click()
        time.sleep(5)
        assert 'Top 100 Crypto-monnaies par capitalisation de marché' in self.driver.page_source

    def test_Arab(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('हिन्दी')
        lang.click()
        time.sleep(5)
        assert 'क्रिप्टोकरेंसी' in self.driver.page_source

    def test_Italian(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Italiano')
        lang.click()
        time.sleep(5)
        assert 'Migliori 100 Criptovalute per Capitalizzazioni di mercato' in self.driver.page_source

    def test_Japan(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('日本語')
        lang.click()
        time.sleep(5)
        assert '仮想通貨時価総額上位100' in self.driver.page_source

    def test_Korean(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('한국어')
        lang.click()
        time.sleep(5)
        assert '시가총액에' in self.driver.page_source

    def test_Portuguese(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Português Brasil')
        lang.click()
        time.sleep(5)
        assert 'Top 100 Criptomoedas por Capitalização de Mercado' in self.driver.page_source

    def test_Russian(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Русский')
        lang.click()
        time.sleep(5)
        assert 'Топ-100 Криптовалюты по рыночной капитализации' in self.driver.page_source

    def test_Turkish(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Türkçe')
        lang.click()
        time.sleep(5)
        assert 'Piyasa Değerine Göre' in self.driver.page_source

    def test_Vietnamese(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('Tiếng Việt')
        lang.click()
        time.sleep(5)
        assert 'Top 100 Các loại tiền điện tử theo vốn hóa thị trường' in self.driver.page_source

    def test_China1(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('简体中文')
        lang.click()
        time.sleep(5)
        assert '市值前100 加密货币' in self.driver.page_source

    def test_China2(self):
        try:
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'sc-14gaqg0-0 jGQJR')]")
            lang_but.click()
            time.sleep(1)
        except Exception:
            menu = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'sc-1xylbka-0 jIivyD')]")
            menu.click()
            time.sleep(1)
            lang_but = self.driver.find_element_by_xpath(
                "//button[contains(@class, 'jacumr-0 fCcmrJ')]")
            lang_but.click()
            time.sleep(1)
        lang = self.driver.find_element_by_link_text('繁體中文')
        lang.click()
        time.sleep(5)
        assert '市值前 100 加密貨幣' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
