"""
Project Management Program
Time estimate: 2 hours  1:46pm
Actual time:
"""

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by day\n- (A)dd new project\
\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []
    load_projects(FILENAME)
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename)
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
    pass


def save_projects(filename):
    pass


def display_projects(projects):
    pass


def filter_projects(projects):
    pass


def add_project(projects):
    pass


def update_project():
    pass


if __name__ == '__main__':
    main()
