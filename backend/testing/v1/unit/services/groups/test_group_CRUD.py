import pytest
from sqlalchemy import select

import backend.app.services.v1 as v1
import backend.connection.v1.models as models
#!----Tests----

#----Groups----

def test_create_group(db_session):

    try:
        v1.create_group(
            name= "some name",
            db_session= db_session,
        )

        id_in_database: str = db_session.execute(
            select(
                models.Group.unique_uuid,
            ).where(
                models.Group.name == "some name",
            ).order_by(
                models.Group.group_id.desc()
            )
        ).scalar()
    except:
        raise

    assert id_in_database is not None
    assert isinstance(id_in_database, str)

@pytest.mark.skip
def test_remove_group():
    raise NotImplementedError

@pytest.mark.skip
def test_join_group():
    raise NotImplementedError

@pytest.mark.skip
def test_leave_group():
    raise NotImplementedError

@pytest.mark.skip
def test_remove_user_from_group():
    raise NotImplementedError


#----Group Permission----
@pytest.mark.skip
def test_grant_editing_on_group_schedule():
    raise NotImplementedError

@pytest.mark.skip
def test_revoke_editing_on_group_schedule():
    raise NotImplementedError


#----Group Invitation----
@pytest.mark.skip
def test_generate_join_QRcode():
    raise NotImplementedError

@pytest.mark.skip
def test_generate_join_url():
    raise NotImplementedError