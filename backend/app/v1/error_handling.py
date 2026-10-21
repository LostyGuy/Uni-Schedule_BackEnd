from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, OperationalError
from backend.logging import log_sql_handler_error

def get_attributes(exc) -> dict[str, str]:
    
    sql_statement = getattr(exc, "statement", "No Statement")
    sql_parameters = getattr(exc, "params", "N/A")
    original_message = str(getattr(exc, "orig", exc))
    
    return {
        "orig_message": original_message,
        "sql_statement": sql_statement,
        "sql_params": sql_parameters,
    }

def capture_errors(app):
    
    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request: Request, exc: IntegrityError):
        
        error_attribs = get_attributes(exc)
        
        log_sql_handler_error(
            title= "DB Integrity Error",
            original_message= error_attribs.get("orig_message"),
            sql_statement= error_attribs.get("sql_statement"),
            sql_parameters= error_attribs.get("sql_params"),
            request= request
        )
        return JSONResponse(
            status_code= 409,
            content={
                #No Frontend At The Moment
            }
        )
        
    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
        
        error_attribs = get_attributes(exc)
        
        log_sql_handler_error(
            title= "Database Error",
            original_message= error_attribs.get("orig_message"),
            sql_statement= error_attribs.get("sql_statement"),
            sql_parameters= error_attribs.get("sql_params"),
            request= request
        )
        return JSONResponse(
            status_code= 500,
            content={
                #No Frontend At The Moment
            }
        )
        
    @app.exception_handler(OperationalError)
    async def operational_error_handler(request: Request, exc: OperationalError):
        
        error_attribs = get_attributes(exc)
        
        log_sql_handler_error(
            title= "Operation Error",
            original_message= error_attribs.get("orig_message"),
            sql_statement= error_attribs.get("sql_statement"),
            sql_parameters= error_attribs.get("sql_params"),
            request= request
        )
        return JSONResponse(
            status_code= 503,
            content={
                #No Frontend At The Moment
            }
        )
    