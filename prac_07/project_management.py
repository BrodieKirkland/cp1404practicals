"""
Project Management Program
Time estimate: 2 hours  1:46pm
Actual time:
"""
from project import Project


INDEX_NAME = 0
INDEX_START_DATE = 1
INDEX_PRIORITY = 2
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = 4
FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by day\n- (A)dd new project\
\n- (U)pdate project\n- (Q)uit"


def main():
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project()
        print(MENU)
        choice = input(">>>").upper()


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            parts[INDEX_PRIORITY] = int(parts[INDEX_PRIORITY])
            parts[INDEX_COST_ESTIMATE] = float(parts[INDEX_COST_ESTIMATE])
            parts[INDEX_COMPLETION_PERCENTAGE] = int(parts[INDEX_COMPLETION_PERCENTAGE])
            projects.append(Project(*parts))
    return projects


def save_projects(projects, filename):
    with open(filename, "w") as out_file:
        for project in projects:
            project_string = "{}\t{}\t{}\t{}\t{}".format(*project)
            print(project_string)


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print(project)
    print("Complete projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(project)


def filter_projects(projects):
    pass


def add_project(projects):
    pass


def update_project():
    pass


if __name__ == '__main__':
    main()
