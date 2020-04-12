from model.project import Project


def test_create_project(app):
    username = "administrator"
    password = "root"
    old_projects = app.soap.get_project_list(username, password)
    project = Project(name=app.project.random_name_field("project_", 4))
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
