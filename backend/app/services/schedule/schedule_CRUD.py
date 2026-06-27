import backend.models.models as models
from backend.timestamps import current_time
from backend.logging import log_info, current_function

def create_schedule(title: str, description: str, creator: int, db_session) -> bool:
    """
    Create a new schedule record in the database.
    
    Parameters:
        title (str): The title of the schedule
        description (str): A description of the schedule
        creator (int): The user ID of the creator
    
    Returns:
        bool: True if the schedule was successfully created and persisted, False otherwise
    """
    schedule_query = models.schedule(
        title = title,
        description = description,
        created_by = creator,
        created_at = current_time(),
        last_update_at = current_time(),
    )
    try:
        db_session.add(schedule_query)
        db_session.commit()
        status = True
    except Exception as e:
        log_info(current_function, e)
        status = False
    return status