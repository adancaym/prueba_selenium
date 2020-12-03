from DriverCrome import DriverCrome

# Principio de una sola responsabilidad
class RandomTodoListGenerator():
    def __init__(self, driver=DriverCrome()):
        self.__driver = driver
    def get_array_task_titles(self, cantidad):
        task_to_save = []
        try:
            self.__driver.open_window_in_url('https://randomtodolistgenerator.herokuapp.com/library')
            tasks_container = self.__driver.get_elemento_by_css_esperar_a_presencia('.tasks-card-container.row')
            taskCards = tasks_container.find_elements_by_css_selector('.taskCard')
            for i in range(0, cantidad):
                task_to_save.append(taskCards[i].find_element_by_css_selector('.task-title>div').text)

        except:
            print('Error al obtener las tareas')
            self.__driver.close_driver()

        return task_to_save