from datetime import datetime, timedelta


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.status = False
        self.deadline = deadline

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        status_str = "Done" if self.status else "Not Done"
        return f"Task: {self.description}, Deadline: {self.deadline}, Status: {status_str}"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)


class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)
        return project


manager = ProjectManager()

project1 = manager.create_project("Project A")
task1 = Task("Task 1", datetime.now() + timedelta(days=3))
task2 = Task("Task 2", datetime.now() + timedelta(days=5))

project1.add_task(task1)
project1.add_task(task2)

project2 = manager.create_project("Project B")
task3 = Task("Task 3", datetime.now() + timedelta(days=7))
task4 = Task("Task 4", datetime.now() + timedelta(days=10))

project2.add_task(task3)
project2.add_task(task4)

task1.mark_as_done()
task4.mark_as_done()

print("Tasks for Project A:")
project1.show_tasks()

print("\nTasks for Project B:")
project2.show_tasks()
