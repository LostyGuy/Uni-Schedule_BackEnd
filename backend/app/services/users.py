import backend.connection.models as models
from backend.logging import current_function, log_info
from backend.timestamps import current_time
from backend.app.services.user.user_CRUD import hash_password

def new_user_register(username: str, email: str, password: str, db_session, policy_agreement: bool = False, role: int = 1) -> bool:
    '''
    Makes query and performs INSERT operation to add user to the database.
    It takes username, email, password, policy_agreement, role, db_session and returns bool value to determine weather operation was a success or not.
    '''
    if policy_agreement:
        try:
            new_user = models.user(
                username = username,
                email = email,
                hashed_password = hash_password(password),
                created_at = current_time(),
                policy_agreement = policy_agreement,
                lastly_signed_in_on = current_time(),
                role = role,
            )
            db_session.add(new_user)
            db_session.commit()
            return True
        except Exception as e:
            db_session.rollback()
            log_info(current_function, e)
            return False
    else:
        return False