import os

import backend.connection.models as models
import backend.security.tokens as tokens
from backend.security.hashing import hash_string


async def user_login(email:str, password:str, device_name: str, ip_address: str, db_session) -> str:
    """
    Authenticates a user by email and hashed password, and creates a login session on successful verification.
    
    Returns:
    	(True, access_token) if the email and hashed_password match a user in the database, (False, None) otherwise
    """
    
    try:
        is_entry_present = db_session.query(
            models.User.user_id
        ).filter(
            models.User.email == email,
            models.User.hashed_password == hash_string(password)
        ).first()
    except:
        #---- Get most possible errors and show them to user in a friendly way ----#
        ...
        
    if is_entry_present[0]:
        
        client_access_token = await tokens.create_refresh_token(
            user_id = is_entry_present[0],
            device_name = device_name,
            ip_address = ip_address,
            db_session = db_session,
        )
        
        return client_access_token
    
    else:
        
        return ""
    
    
def user_log_out(db_session, access_token: str = None):
    ''' '''



    #---- OLD LOGIC ----#
    # if access_token is None:
    #     log_info(current_function, 'access_token is None')
    #     raise ValueError
    
    # status: list[any] = db_session.query(
    #     models.login_session.status,
    #     models.login_session.valid_till,
    # ).filter(
    #     models.login_session.access_token == access_token,
    # ).order_by(
    #     models.login_session.issued_at.desc()
    # ).first()
    
    # log_info(current_function, f'Status is {status[0]}')

    # if status[0] == 'Active':
    #     try:
    #         db_session.query(
    #         models.login_session,
    #         ).filter_by(
    #             access_token = access_token,
    #         ).update(
    #             {'status': 'Revoked'}
    #         )
    #         db_session.commit()
    #     except Exception as e:
    #         db_session.rollback()
    #         log_info('Log Out', e)
    #         return False
    #     return True
    # elif status[0] == 'Revoked':
    #     log_info(current_function, 'Token is already revoked')
    #     return False
    # else:
    #     log_info(current_function, 'Unexpected Value')
    #     return False