import configparser
config = configparser.RawConfigParser()
config.read(r"C:\Users\HP\Python_Selenium_Pytest_in_pycharm\05.OrangeHRM_Pytest_framework\configuration\config.ini")

class ReadConfig:

    @staticmethod
    def get_login_url():
        login_url = config.get('application url','login_url')
        return login_url

    @staticmethod
    def get_username():
        username = config.get('login data','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login data','password')
        return password


