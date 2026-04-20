EXPECTED_KEYS = {"description", "schedule", "max_participants", "participants"}


def test_get_activities_returns_200(client):
    # Arrange
    # (no setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert expected_activity in data


def test_get_activities_each_has_required_fields(client):
    # Arrange
    # (no setup needed)

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for activity in data.values():
        assert EXPECTED_KEYS.issubset(activity.keys())
