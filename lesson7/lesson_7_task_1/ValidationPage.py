class ValidationPage:
    def __init__(self, driver):
        self.driver = driver

    def is_zip_code_red(self):
        zip_code_field = self.driver.find_element_by_id("zip-code")
        return zip_code_field.get_attribute("class") == "form-control is-invalid"

    def are_other_fields_green(self):
        fields = self.driver.find_elements_by_class_name("form-control")
        for field in fields:
            if "is-invalid" in field.get_attribute("class"):
                return False
        return True