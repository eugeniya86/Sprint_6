from .base_page import BasePage
from locators.faq_locators import QuestionsPageLocators
import allure


class QuestionsPage(BasePage):
    @allure.step("Accept cookies")
    def accept_cookies(self):
        if self.is_element_displayed(QuestionsPageLocators.COOKIE_BUTTON):
            self.click(QuestionsPageLocators.COOKIE_BUTTON)

    @allure.step("Клик на вопрос")
    def click_question(self, question_index):
        locator = (QuestionsPageLocators.QUESTION[0],
                   QuestionsPageLocators.QUESTION[1].format(question_index))
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Получить текст")
    def get_answer_text(self, question_index):
        locator = (QuestionsPageLocators.ANSWER[0],
                   QuestionsPageLocators.ANSWER[1].format(question_index))
        return self.get_text(locator)

    @allure.step("Проверить ответ")
    def is_answer_displayed(self, question_index):
        answer_locator = QuestionsPageLocators.get_answer_locator(question_index)
        answer = self.is_answer_displayed(answer_locator)
        self.wait.until(lambda d: answer.text.strip() != "")
        return answer.text

