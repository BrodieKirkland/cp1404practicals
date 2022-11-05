"""
Project Management Program
Time estimate: 2 hours
Actual time: 3 hours + 2 hours for confusing datetime stuff
"""
from project import Project
import datetime

INDEX_NAME = 0
INDEX_START_DATE = 1
INDEX_PRIORITY = 2
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = 4
FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by day\n- (A)dd new project\
\n- (U)pdate project\n- (Q)uit"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"


def main():
    """Load, manage, and save projects from filename"""
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
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
            update_project(projects)
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from filename"""
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
    """Save projects to filename"""
    with open(filename, "w") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            project_string = f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t" \
                             f"{project.completion_percentage}"
            print(project_string, file=out_file)


def display_projects(projects):
    """Display projects neatly"""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print(f"  {project}")
    print("Complete projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(f"  {project}")


def filter_projects(projects):
    """Filter projects by start_date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_date > date:
            print(project)


def add_project(projects):
    """Add new project"""
    name = input("Project name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update project priority and completion percentage"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = int(input("New percentage: "))
    if new_percentage != "":
        projects[choice].completion_percentage = new_percentage
    new_priority = int(input("New priority: "))
    if new_priority != "":
        projects[choice].priority = new_priority


if __name__ == '__main__':
    main()
