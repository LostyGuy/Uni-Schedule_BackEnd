import os

import pytest

import backend.app.v1.services as services
import backend.connection.v1.models as models
from backend.testing.v1.conftest import users_data, roles_data
from backend.security.v1.hashing import hash_string
from backend.logging import log_error


def test_new_user_register(db_session):
    '''This test takes user data and puts it into CRUD to register the user into system'''

    register_Emily = services.user_CRUD.user_register(
        name= 'Emily',
        surname= 'Mayer',
        username= 'EmilyMayer',
        email= 'emilyheartbreaker@mail.to',
        password= 'my_heart_is_broken',
        policy_agreement= True,
        db_session= db_session,
    )
    assert register_Emily



        
#!---Suspended for now----
# def test_get_user_profile():
#   pass