import pytest
from fastapi.testclient import TestClient

import backend.app.main as main
import backend.connection.connection as connection
import backend.testing.unit.test_database as Testdb

#!----Status Codes----
#   200 - OK
#   303 - See Other
#   404 - Error Found
#   405 - Method Not Allowed
#   500 - Internal Server Error

#----Mock DB Setup----
@pytest.fixture
def Client():
    """
    Create a test client with a mocked database dependency.
    
    Returns:
        TestClient: A test client for making HTTP requests to the FastAPI application.
    """
    main.app.dependency_overrides[connection.get_db] = Testdb.get_db
    return TestClient(main.app)

#----User Related----
def test_user_login_request(Client):
    result = Client.post("/login_request", json={
        "username":"JohnDoe", 
        "email":"johndoe@mail.jd",
        "password":"JohnDoePass",
        "policy_agreement": True,
        })

    assert result.status_code == 200
    list_of_variables: list[str] = (
        "username",
        "access_token",
        "issued_at",
        "valid_till",
        )
    for variable in list_of_variables:
        assert variable in result.json()

#----Group Related----
@pytest.mark.skip
def test_create_invitation_request(Client):
    raise NotImplementedError

@pytest.mark.skip
def test_intivation_request(Client):
    raise NotImplementedError

@pytest.mark.skip
def test_leave_group_request(Client):
    raise NotImplementedError

#----Role Related----
@pytest.mark.skip
def test_grant_role_on_schedule_request(Client):
    raise NotImplementedError

@pytest.mark.skip
def test_revoke_role_on_schedule_request(Client):
    raise NotImplementedError

#TODO----Premium Related----
@pytest.mark.skip
def test_grant_premium_request():
    raise NotImplementedError

@pytest.mark.skip
def test_renew_premium_request():
    raise NotImplementedError