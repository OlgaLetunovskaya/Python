class DataFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element_by_id("first-name")
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element_by_id("last-name")
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_address(self, address):
        address_field = self.driver.find_element_by_id("address")
        address_field.clear()
        address_field.send_keys(address)

    def enter_email(self, email):
        email_field = self.driver.find_element_by_id("email")
        email_field.clear()
        email_field.send_keys(email)

    def enter_phone_number(self, phone_number):
        phone_field = self.driver.find_element_by_id("phone")
        phone_field.clear()
        phone_field.send_keys(phone_number)

    def enter_zip_code(self, zip_code):
        zip_code_field = self.driver.find_element_by_id("zip-code")
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)

    def enter_city(self, city):
        city_field = self.driver.find_element_by_id("city")
        city_field.clear()
        city_field.send_keys(city)

    def enter_country(self, country):
        country_field = self.driver.find_element_by_id("country")
        country_field.clear()
        country_field.send_keys(country)

    def enter_job_position(self, job_position):
        job_field = self.driver.find_element_by_id("job-position")
        job_field.clear()
        job_field.send_keys(job_position)

    def enter_company(self, company):
        company_field = self.driver.find_element_by_id("company")
        company_field.clear()
        company_field.send_keys(company)

    def submit_form(self):
        submit_button = self.driver.find_element_by_id("submit")
        submit_button.click()