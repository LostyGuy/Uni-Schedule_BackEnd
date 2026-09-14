import pytest
from sqlalchemy import select
import secrets

from datetime import timedelta
import jwt

import backend.connection.models as models
import backend.security.tokens as token
from backend.security.hashing import hash_string
from backend.logging import log_error
from backend.testing.conftest import EXISTING_USERS
from backend.timestamps import current_time
from backend.config import get_environmental_variables

@pytest.mark.skip
def test_on_password_change(db_session):
    
    Toms_id = db_session.execute(
        select(
            models.User.user_id
        ).where(
            models.User.email == EXISTING_USERS[0]["email"]
        )
    ).scalar_one()