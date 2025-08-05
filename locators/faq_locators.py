from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    # Questions section
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']")

    # Cookie
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def get_answer_locator(question_index):
        return (By.XPATH, f"//div[@aria-labelledby='{question_index}']/p")