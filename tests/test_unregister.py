import src.app as app_module


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email not in app_module.activities[activity]["participants"]


def test_unregister_activity_not_found(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_participant_not_found(client):
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_unregister_duplicate_delete(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]
    client.delete(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
