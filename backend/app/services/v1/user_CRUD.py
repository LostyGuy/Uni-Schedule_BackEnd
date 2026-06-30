import backend.connection.models as models
from backend.logging import current_function, log_error
from backend.timestamps import current_time
from backend.security.hashing import hash_string

def user_register(name: str, surname: str, username: str, email: str, password: str, db_session, policy_agreement: bool = False, role_id: int = 1) -> bool:
    """
    Registers a new user in the database if the policy agreement is accepted.
    
    Returns:
        True if the user is successfully registered, False if the policy agreement is not accepted or registration fails.
    """
    if policy_agreement:
        try:
            new_user = models.User(
                username = username,
                name = name,
                surname = surname,
                email = email,
                hashed_password = hash_string(password),
                role_id = role_id,
                policy_agreement = policy_agreement,
            )
            db_session.add(new_user)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            log_error("User Creation Error", e)
            return False
        return True
    else:
        return False
    
def get_user_profile():
    raise NotImplementedError

def delete_user():
    raise NotImplementedError