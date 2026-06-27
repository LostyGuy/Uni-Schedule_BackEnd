from typing import Annotated
import os

import pytest

import backend.app.services.user.user_CRUD as user_CRUD
import backend.connection.models as models
from backend.connection.connection import Base
from backend.timestamps import current_time
from backend.logging import log_info_test_space, current_function
from backend.testing.unit.test_database import Testengine, TestSessionLocal
from backend.security.tokens import jwt_validation

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

def users_credentials_for_setup() -> list[dict]:
    """
    Create test user records for database seeding in unit tests.
    
    Returns:
        A tuple of two user model instances with test credentials and hashed passwords.
    """
    models.us
    new_user_John = models.users.User(
        name = 'John',
        surname = 'Doe',
        username = 'Havent seen anything',
        email = 'johndoe@mail.com',
        hashed_password = user_CRUD.hash_password('to_be_hashed'),
        role_id = 2,
        policy_agreement = True,
        
    )
    new_user_Tom = models.users.User(
        name = 'Tom',
        surname = 'Prince',
        username = 'tom',
        email = 'tomprince@mail.com',
        hashed_password = user_CRUD.hash_password('$ome_cr@zy_p@$$'),
        role_id = 2,
        policy_agreement = True,
    )
    return new_user_John, new_user_Tom

def roles_for_setup() -> list[dict]:
    """
    Create and return role objects for test database seeding.
    
    Returns two predefined roles: an 'owner' role with ID 1 and a 'user' role with ID 2.
    
    Returns:
    	tuple: A tuple containing two models.roles objects (owner_role, user_role)
    """
    admin_role = models.auth.Role(
        role_id = 1,
        name = 'owner',
        description = 'none',
        can_manage_events = True,
        can_invite_members = True,
    )
    user_role = models.auth.Role(
        role_id = 2,
        name = 'user',
        description = 'none',
        can_manage_events = False,
        can_invite_members = False,
    )
    return admin_role, user_role

#!----Tests----
def test_is_user_in_database(db_session):
    """
    Verify that seeded test users exist in the database with correct credentials.
    
    Queries the database for each seeded user and asserts that their username, email, and policy agreement status match expected values.
    """

    for user in users_credentials_for_setup():
        try:
            result = db_session.query(
                models.users.User.username,
                models.users.User.email,
                models.users.User.policy_agreement,
            ).filter(models.users.User.username == user.username).first()
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

    register_Emily = user_CRUD.user_register(
        name = 'Emily',
        surname = 'Mayer',
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
            email = user.email,
            hashed_password = user.hashed_password,
            db_session = db_session,
        )
    #----Check if access token was created----
        if not login_result[0]:
            assert False
        elif login_result[1] is not None:
            assert login_result[0]
        session_result = db_session.query(
            models.refresh_tokens.user_session.user_session_id
        ).filter(models.refresh_tokens.user_session.access_token == login_result[1]).first()

        assert session_result is not None
    #----Check Cookie----

def test_user_logout(db_session):
    ''' BAD '''

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
            models.refresh_tokens.User_session.acess_token == access_token,
        ).order_by(
            models.refresh_tokens.User_session.issued_at.desc()
        ).first()

        assert result == True
        assert status[0] == 'Revoked'
        
#!---Suspended for now----
# def test_get_user_profile():
#   pass