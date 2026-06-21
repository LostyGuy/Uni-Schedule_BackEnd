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
    main.app.dependency_overrides[connection.get_db] = Testdb.get_db
    with TestClient(main.app) as client:
        yield client
    main.app.dependency_overrides.pop(connection.get_db, None)

@pytest.mark.skip
def test_create_group_request(Client):
    raise NotImplementedError

@pytest.mark.skip
def test_delete_group_request(Client):
    raise NotImplementedError