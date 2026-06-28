import os

import pytest

import backend.app.services.v1 as v1
import backend.connection.models as models
from backend.testing.conftest import users_data, roles_data
# from backend.timestamps import current_time
# from backend.logging import log_info_test_space, current_function
# from backend.security.tokens import jwt_validation


#!----Tests----

def test_new_user_register(db_session):
    '''This test takes user data and puts it into CRUD to register the user into system'''

    register_Emily = v1.user_CRUD.user_register(
        name= 'Emily',
        surname= 'Mayer',
        username= 'EmilyMayer',
        email= 'emilyheartbreaker@mail.to',
        password= 'my_heart_is_broken',
        policy_agreement= True,
        db_session= db_session,
    )
    assert register_Emily


def test_user_login(email: str, password: str, device_name: str, ip_address: str, db_session):
    """
    Verify that user login authentication creates an access token and corresponding login session record.
    """

    access_token, refresh_token = v1.user_login(
        email= email,
        password= password,
        device_name= device_name,
        ip_address= ip_address,
        db_session= db_session,
    )

    if access_token and refresh_token:
        ...
    else:
        raise RuntimeError


def test_user_logout(db_session):
    ''' BAD '''

    #----Log In----
    for user in users_data():
        success, access_token = v1.user_CRUD.user_login(
            email= user.email,
            hashed_password= user.hashed_password,
            db_session= db_session,
        )

        assert success == True
    #----Log Out----
        result = v1.user_CRUD.user_log_out(
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