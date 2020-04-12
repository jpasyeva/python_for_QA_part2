from model.project import Project


def test_create_project(app):
    old_project = app.project.get_project_list()
    project = Project(name=app.project.random_name_field("project_", 4))
    app.project.create(project)
    new_project = app.project.get_project_list()
    assert len(old_project) + 1 == len(new_project)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
