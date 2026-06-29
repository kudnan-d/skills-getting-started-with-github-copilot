from urllib.parse import quote


def test_unregister_participant_removes_email_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{quote(email)}")

    # Assert
    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_nonexistent_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    email = "noone@example.com"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{quote(email)}")

    # Assert
    assert response.status_code == 404


def test_unregister_from_nonexistent_activity_returns_404(client):
    # Arrange
    activity_name = "No Such Activity"
    email = "someone@example.com"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{quote(email)}")

    # Assert
    assert response.status_code == 404
