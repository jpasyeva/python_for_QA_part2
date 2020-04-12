

def test_signup_new_account(app):
    username = app.project.random_name_field("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()
