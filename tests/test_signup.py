import src.app as app_module


def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in app_module.activities[activity]["participants"]


def test_signup_activity_not_found(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_activity_full(client):
    # Arrange
    activity = "Chess Club"
    max_p = app_module.activities[activity]["max_participants"]
    app_module.activities[activity]["participants"] = [
        f"student{i}@mergington.edu" for i in range(max_p)
    ]
    email = "overflow@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"


def test_signup_duplicate_registration(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_email_with_special_characters(client):
    # Arrange
    activity = "Chess Club"
    email = "student+tag@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert email in app_module.activities[activity]["participants"]
