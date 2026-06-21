import backend.connection.models as models
from backend.timestamps import current_time
from backend.logging import current_function, log_info

def create_schedule(title: str, description: str, creator: int, db_session) -> bool:
    try:
        schedule_query = models.schedules.Schedule(
        title = title,
        description = description,
        created_by = creator,
        created_at = current_time(),
        last_update_at = current_time(),
        )

        db_session.add(schedule_query)
        db_session.commit()
        status = True
    except Exception as e:
        log_info(current_function, e)
        db_session.rollback()
        status = False
    return status