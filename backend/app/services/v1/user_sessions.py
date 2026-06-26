import os

from backend.app.services.v1.auth_login import hash_password
import backend.connection.models as models
from backend.logging import log_error

def user_register(username: str, email: str, password: str, db_session, policy_agreement: bool = False, role: int = 1) -> bool:
    """
    Registers a new user in the database if the policy agreement is accepted.
    
    Returns:
        True if the user is successfully registered, False if the policy agreement is not accepted or registration fails.
    """
    if policy_agreement:
        try:
            new_user = models.User(
                username = username,
                name = ...,
                surname = ...,
                email = email,
                hashed_password = hash_password(password),
                role_id = 2,
                policy_agreement = policy_agreement,
            )
            db_session.add(new_user)
            db_session.commit()
            return True
        except Exception as e:
            db_session.rollback()
            log_error("User Creation Error", e)
            return False
    else:
        return False