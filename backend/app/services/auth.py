import backend.connection.models as models
from backend.logging import current_function, log_info
from backend.timestamps import current_time
from backend.security.jwt_tokens import create_jwt

def user_login(email:str, hashed_password:str, db_session) -> bool:
    
    #----Is Credentials Correct----
    correct_credentials: list[object] = db_session.query(
        models.users.user_id,
        models.users.email,
        models.users.hashed_password,
    ).filter(
        models.users.email == email,
    ).first()
    if correct_credentials is not None and correct_credentials.email == email and correct_credentials.hashed_password == hashed_password:
        login_data: bool =  True
    else:
        login_data: bool =  False

    #!----TO BE REDIRECTED TO user_session.py----
    if login_data:
    #----Create JWT----
        access_token, payload = create_jwt(correct_credentials.id_user, issue_endpoint='/login_request', for_endpoint='/loged')
    #----Add User Session Entry----
        login_session = models.auth.login_session(
            user_id = correct_credentials.id_user,
            access_token = access_token,
            issued_at = payload['iat'],
            valid_till = payload['exp'],
            issued_from_endpoint = '/user_request',
            valid_for_endpoint = payload['aud'],
            status = 'Active',
            jwt_id = payload['jti'],
            created_at = str(current_time()),
        )
        try:
            db_session.add(login_session)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            log_info(current_function, e)
        return True, access_token
    else:
        return False, None
    
def user_log_out(db_session, access_token: str = None):
    ''' '''

    if access_token is None:
        log_info(current_function, 'access_token is None')
        raise TypeError
    
    status: list[any] = db_session.query(
        models.login_session.status,
        models.login_session.valid_till,
    ).filter(
        models.login_session.access_token == access_token,
    ).order_by(
        models.login_session.issued_at.desc()
    ).first()
    
    log_info(current_function, f'Status is {status[0]}')

    if status[0] == 'Active':
        try:
            db_session.query(
            models.login_session,
            ).filter_by(
                access_token = access_token,
            ).update(
                {'status': 'Revoked'}
            )
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            log_info('Log Out', e)
            return False
        return True
    elif status[0] == 'Revoked':
        log_info(current_function, 'Token is already revoked')
        return False
    else:
        log_info(current_function, 'Unexpected Value')
        return False