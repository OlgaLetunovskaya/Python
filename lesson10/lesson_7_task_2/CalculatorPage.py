from selenium.webdriver.common.by import By

class CalculatorPage:
    """
    Этот класс представляет страницу калькулятора в веб-приложении.

    Методы:
    - open_page: Открыть страницу калькулятора.
    - set_delay: Установить значение задержки в поле ввода.
    - click_button: Нажать кнопку калькулятора в соответствии с текстом.
    - get_result: Вывод результата на экран калькулятора.
    - close_page: Закрыть браузер.
    """

    def __init__(self, driver):
        """
        Конструктор для класса CalculatorPage.

        Параметры:
        - драйвер: экземпляр веб-драйвера
        """
        self.driver = driver

    def open_page(self):
        """
        Открыть страницу калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value: str):
        """
        Установить значение задержки в поле ввода.

        Параметры:
        - значение (str): значение задержки, которое необходимо установить.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)

    def click_button(self, button_text: str):
        """
        Нажать кнопку калькулятора в соответствии с текстом.

        Параметры:
        - button_text (str): текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element_by_xpath(f"//button[contains(text(), '{button_text}')]").click()

    def get_result(self) -> str:
        """

        Получить результат, отображаемый на калькуляторе.

        Возвращается:
        - str: результат, отображаемый на калькуляторе.
        """
        return self.driver.find_element(By.ID, "result").text

    def close_page(self):
        """
        Закрыть браузер
        """
        self.driver.quit()
