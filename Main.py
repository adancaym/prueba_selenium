from TodoIst import TodoIst
from RandomTodoListGenerator import RandomTodoListGenerator
from DriverCrome import DriverCrome
class Main():

    def run(self):
        # Principio de inversion de dependencias
        driverRandomList = DriverCrome()
        try:
            # Principio de una sola responsabilidad
            randomListGenerator = RandomTodoListGenerator(driverRandomList)
            tasks_from_generator = randomListGenerator.get_array_task_titles(5)

            # Principio de inversion de dependencias
            driverTodoIst = DriverCrome()
            try:

                # Principio de una sola responsabilidad
                todoIst = TodoIst(driverTodoIst)
                todoIst.save_task_array_in_todoist(tasks_from_generator)
            except:
                driverTodoIst.driver.close()
            driverTodoIst.driver.close()
        except:
            driverRandomList.driver.close()
        driverRandomList.driver.close()

main = Main()

main.run()