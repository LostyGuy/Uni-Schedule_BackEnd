import pytest
from backend.testing.unit.test_database import Testengine, TestSessionLocal
from backend.app.services.schedule.schedule_CRUD import create_schedule
import backend.app.services.user.user_CRUD as user_CRUD
from backend.timestamps import current_time
from backend.logging import current_function, log_info_test_space
import backend.models.models as models
from backend.hidden.pass_hashing import hash_salt
from sqlalchemy import desc


#----Database and Session Setup----
@pytest.fixture
def db_session():
    """
    Create an isolated SQLAlchemy session for transactional testing.
    
    Yields:
    	Session: A SQLAlchemy session with transactional isolation and automatic rollback after test completion
    """
    connection = Testengine.connect()
    transaction = connection.begin()
    session = TestSessionLocal(bind=connection)
    session.begin_nested()
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()

@pytest.fixture(autouse=True)
def database_setup(db_session):
    users = users_credentials_for_setup()
    roles = roles_for_setup()
    db_session.add_all(roles)
    db_session.flush()
    db_session.add_all(users)
    db_session.flush()
    



def schedule_and_events_for_setup():
    raise NotImplementedError

#!----Tests----

#----Schedules----
def test_create_schedule(db_session):
    toms_user_id = db_session.query(
            models.user.id_user,
        ).filter(
            models.user.username == "tom",
        ).limit(1).first()
    
    new_schedule: dict[str | int] = {
        'title' : "Test Schedule",
        'description' : "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.",
        'creator' : toms_user_id[0],
    }

    result = create_schedule(
        title = new_schedule.get('title'),
        description = new_schedule.get('description'),
        creator = new_schedule.get('creator'),
        db_session = db_session,
    )

    created_schedule = db_session.query(
        models.schedule.name,
        models.schedule.created_by,
        models.schedule.status,
    ).filter(
        models.schedule.created_by == new_schedule.get('creator'),
    ).order_by(
        desc(models.schedule.scheduleId)
    ).first()

    assert result is True
    assert created_schedule[0] == new_schedule.get('title')
    assert created_schedule[1] == new_schedule.get('creator')

def test_alter_schedule():
    raise NotImplementedError

def test_delete_schedule():
    raise NotImplementedError


#----Events----
def test_create_event():
    raise NotImplementedError

def test_alter_event():
    raise NotImplementedError

def test_delete_event():
    raise NotImplementedError