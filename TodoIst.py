from functools import reduce
from DriverCrome import DriverCrome;


# Principio de una sola responsabilidad
class TodoIst():

    def __init__(self, driver=DriverCrome()):
        self.__driver = driver

    def save_task_array_in_todoist(self, task_to_save):
        try:
            self.open_site()
            self.login_in_site()
            self.click_en_agregar()
            self.save_tasks(task_to_save)
            self.await_is_saved()
        except:
            print('Error en el procesos de guardado')
            self.__driver.driver.close()

    def await_is_saved(self):
        try:
            while True:
                lista = self.__driver.get_elemento_by_css_esperar_a_presencia(
                    '#agenda_view > div > div.section > div > ul')
                task_in_list = lista.find_elements_by_css_selector('li:not(:last-child)')
                array_booleans_task_saved = self.get_array_booleans_task_saved(task_in_list)
                print(array_booleans_task_saved)
                is_all_saved = self.reduce_array_of_booleans(array_booleans_task_saved)
                print(is_all_saved)
                if is_all_saved: break
        except:
            print('Error en espera a guardado')
            self.__driver.driver.close()

    def get_array_booleans_task_saved(self, tasks_in_list):
        try:
            return list(map(lambda task: not task.get_attribute('data-item-id').startswith('_'), tasks_in_list))
        except:
            print('Error al mapear las tareas en pantalla de guardado')
            print(tasks_in_list)
            self.__driver.driver.close()

    def reduce_array_of_booleans(self, array_of_booleans):
        try:
            return reduce(lambda a, b: a and b, array_of_booleans)
        except:
            print('Error al reducir el arreglo boleano')
            self.__driver.driver.close()

    def save_tasks(self, tasks):
        try:
            for task in tasks:
                self.__driver.get_elemento_by_css_esperar_a_que_sea_clickeable_and_send_keys(
                    ".public-DraftEditor-content[role='textbox']", task)
                self.__driver.get_elemento_by_css_esperar_a_que_sea_clickeable_and_click(
                    '#agenda_view > div > div > div > ul > li > form > div.task_editor__form_actions > button.ist_button.ist_button_red')
        except:
            print('Error al mandar la tarea al formulario')
            self.__driver.driver.close()

    def click_en_agregar(self):
        try:
            self.__driver.get_elemento_by_css_and_click(
                '#agenda_view > div > div.section > div > ul > li > button.plus_add_button')
        except:
            print('Error al dar click en el boton agregar')
            self.__driver.driver.close()

    def open_site(self):
        try:
            self.__driver.open_window_in_url('http://todoist.com')
        except:
            print('Error al abrir el sitio')
            self.__driver.driver.close()

    def login_in_site(self):
        try:
            self.__driver.find_element_by_link_text_and_click('Inicia sesión')
            self.__driver.get_elemento_by_css_and_send_keys('#email', 'adanyanezgonzalez@gmail.com')
            self.__driver.get_elemento_by_css_and_send_keys('#password', '9CJBsq7VyK5bPS2')
            self.__driver.get_elemento_by_css_and_click('#login_form > button.submit_btn')
        except:
            print('En el proceso de login')
            self.__driver.driver.close()
