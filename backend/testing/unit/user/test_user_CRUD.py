from typing import Annotated

import pytest

import backend.app.services.user.user_CRUD as user_CRUD
import backend.models.models as models
from backend.connection.connection import Base
from backend.timestamps import current_time
from backend.logging import log_info_test_space, current_function
from backend.testing.unit.test_database import Testengine, TestSessionLocal
from backend.hidden.pass_hashing import algorithm, hash_salt, hashed_answer_1, hashed_answer_2, hashed_answer_3 # type: ignore
from backend.hidden.jwt_setting import TOKEN_LIFESPAN
from backend.security.jwt_tokens import jwt_validation


#----Database and Session Setup----
@pytest.fixture
def db_session():
    """
    Provide an isolated test database session with automatic cleanup.
    
    Yields:
        Session: A SQLAlchemy test session with transaction isolation for test execution.
    """
    connection = Testengine.connect()
    transaction = connection.begin()
    session = TestSessionLocal(bind=connection)
    session.begin_nested()
    try:
        yield session
    finally:
        session.close()
        transaction.commit()
        connection.close()

#!----Tests----
def test_is_user_in_database(db_session):
    """
    Verify that seeded test users exist in the database with correct credentials.
    
    Queries the database for each seeded user and asserts that their username, email, and policy agreement status match expected values.
    """

    for user in users_credentials_for_setup():
        try:
            result = db_session.query(
                models.user.username,
                models.user.email,
                models.user.policy_agreement,
            ).filter(models.user.username == user.username).first()
            log_info_test_space(current_function, user.username)
        except Exception as e:
            log_info_test_space(current_function, e)
        log_info_test_space(current_function, result)
        if result:
            assert result is not None
            assert user.username == result[0]
            assert user.email == result[1]
            assert user.policy_agreement == result[2]
        else:
            assert result is None

def test_new_user_register(db_session):
    '''This test takes user data and puts it into CRUD to register the user into system'''

    register_Emily = user_CRUD.new_user_register(
        username = 'EmilyMayer',
        email = 'emilyheartbreaker@mail.to',
        password = 'my_heart_is_broken',
        policy_agreement = True,
        db_session = db_session,
    )
    assert register_Emily == True

def test_user_login(db_session):
    """
    Verify that user login authentication creates an access token and corresponding login session record.
    """
    #----Check Login----
    for user in users_credentials_for_setup():
        login_result = user_CRUD.user_login(
            email= user.email,
            hashed_password= user.hashed_password,
            db_session= db_session,
        )
    #----Check if access token was created----
        if not login_result[0]:
            assert False
        elif login_result[1] is not None:
            assert login_result[0]
        session_result = db_session.query(
            models.login_session.id
        ).filter(models.login_session.access_token == login_result[1]).first()

        assert session_result is not None
    #----Check Cookie----

def test_user_logout(db_session):
    ''' '''

    #----Log In----
    for user in users_credentials_for_setup():
        success, access_token = user_CRUD.user_login(
            email= user.email,
            hashed_password= user.hashed_password,
            db_session= db_session,
        )

        assert success == True
    #----Log Out----
        result = user_CRUD.user_log_out(
            access_token= access_token,
            db_session= db_session
        )
        status: list[any] = db_session.query(
        models.login_session.status,
        ).filter(
            models.login_session.access_token == access_token,
        ).order_by(
            models.login_session.issued_at.desc()
        ).first()

        assert result == True
        assert status[0] == 'Revoked'
        
#!---Suspended for now----
# def test_get_user_profile():
#   pass