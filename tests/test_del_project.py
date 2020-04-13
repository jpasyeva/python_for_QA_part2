from model.project import Project
import random


def test_del_some_project(app):
    config = app.config["webadmin"]
    if len(app.soap.get_project_list(config["username"], config["password"])) == 0:
        app.project.create(Project(name=app.project.random_name_field("project_", 4)))
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project_by_id(project.id)
    new_projects = app.soap.get_project_list(config["username"], config["password"])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
