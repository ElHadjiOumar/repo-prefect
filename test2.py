from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner

# Définir les tâches
@task
def print_hello():
    print("Bonjour")

@task
def print_goodbye():
    print("Au revoir")


@flow(task_runner=SequentialTaskRunner())
def calcule() :
    print_hello.submit()
    print_goodbye.submit()
    # goodbye_task.set_upstream(hello_task)

if __name__ == "__main__":
    calcule()
