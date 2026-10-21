import os

import backend.connection.v1.models as models
import backend.app.v1.services.auth_tokens as auth_tokens
from backend.security.v1.hashing import hash_string
from sqlalchemy import select, update


def user_login(email:str, password:str, device_name: str, ip_address: str, db_session) -> dict[str | None, str | None]:
    """
    Authenticates a user by email and hashed password, and creates a login session on successful verification.
    
    Returns:
    	(access_token, refresh_token) if the email and hashed_password match a user in the database, (None, None) otherwise
    """
    
    is_entry_present = db_session.query(
        models.User.user_id
    ).filter(
        models.User.email == email,
        models.User.hashed_password == hash_string(password)
    ).first()

    if is_entry_present is not None and is_entry_present[0]:

        raw_refresh_token = auth_tokens.create_refresh_token(
            user_id = is_entry_present[0],
            device_name = device_name,
            ip_address = ip_address,
            db_session = db_session,
        )
        if raw_refresh_token is None:
            return {
                "access_token": None,
                "refresh_token": None,
            }

        client_access_token = auth_tokens.create_access_token(is_entry_present[0])
                    
        return {
            "access_token": client_access_token,
            "refresh_token": raw_refresh_token,
        }

    else:

        return {
            "access_token": None,
            "refresh_token": None,
        }
    
    
def user_log_out(db_session, raw_token: str | None = None) -> bool:
    ''' '''

    if not raw_token:
        return False
    #----If token is in DB----
    stmt = select(
            models.RefreshToken
            ).where(
                models.RefreshToken.token_hash == hash_string(raw_token)
            )
        
    result = db_session.scalars(stmt).one_or_none()
    if result is None or not result:
        return False
    db_session.execute(
        update(
            models.RefreshToken,
        ).where(
            models.RefreshToken.user_session_id == result.user_session_id,
        ).values(
            is_revoked= True,
        )
    )
    db_session.commit()
    return True
