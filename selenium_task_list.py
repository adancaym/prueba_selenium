import unittest
from python import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from functools import reduce


# password 9CJBsq7VyK5bPS2

# correo adanyanezgonzalez@gmail.com

class SeleniumPreConfig(unittest.TestCase):

    def setUp(self):
        """
        Configurando el driver
        """
        self.driver = webdriver.Chrome(executable_path=r"./drivers/chromedriver")

    def tearDown(self):
        """
        Cerrando el driver
        """
        self.driver.close()

    def test_1(self):

        task_to_save = [];

        driver = self.driver

        try:
            driver.get('https://randomtodolistgenerator.herokuapp.com/library')
            task_cards_container = WebDriverWait(driver, 2).until(
                Ec.presence_of_element_located((By.CSS_SELECTOR, '.tasks-card-container.row')))
            taskCards = task_cards_container.find_elements_by_class_name('taskCard')

            if len(taskCards) >= 5:
                for i in range(0, 5):
                    title = taskCards[i].find_element_by_css_selector('.task-title>div')
                    task_to_save.append(title.text)

            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])

            driver.get('http://todoist.com')

            boton_login = driver.find_element_by_link_text('Inicia sesión')
            boton_login.click()

            input_email = WebDriverWait(driver, 2).until(Ec.presence_of_element_located((By.CSS_SELECTOR, '#email')))
            input_email.send_keys('adanyanezgonzalez@gmail.com')

            input_password = WebDriverWait(driver, 2).until(
                Ec.presence_of_element_located((By.CSS_SELECTOR, '#password')))
            input_password.send_keys('9CJBsq7VyK5bPS2')

            submit_button = WebDriverWait(driver, 2).until(
                Ec.presence_of_element_located((By.CSS_SELECTOR, '#login_form > button.submit_btn')))
            submit_button.click()

            boton_list_tasks = WebDriverWait(driver, 2).until(Ec.presence_of_element_located(
                (By.CSS_SELECTOR, '#agenda_view > div > div.section > div > ul > li > button.plus_add_button')))
            boton_list_tasks.click()

            for task in task_to_save:
                text_area_new_task = WebDriverWait(driver, 20).until(
                    Ec.element_to_be_clickable((By.CSS_SELECTOR, ".public-DraftEditor-content[role='textbox']")))
                text_area_new_task.send_keys(task)
                btn_submit_task = WebDriverWait(driver, 5).until(Ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                             '#agenda_view > div > div > div > ul > li > form > div.task_editor__form_actions > button.ist_button.ist_button_red')))
                btn_submit_task.click()

            while True:
                lista = WebDriverWait(driver, 2).until(
                    Ec.presence_of_element_located((By.CSS_SELECTOR, '#agenda_view > div > div.section > div > ul')))
                tasks_saved = lista.find_elements_by_css_selector('li:not(:last-child)')
                result_save = list(
                    map(lambda task: not task.get_attribute('data-item-id').startswith('_'), tasks_saved))
                ends = reduce(lambda a, b: a and b, result_save)
                if ends == True: break


        except:
            driver.quit()


if __name__ == '__main__':
    unittest.main()
