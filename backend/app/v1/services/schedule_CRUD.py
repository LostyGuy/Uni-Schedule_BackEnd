from sqlalchemy import select, update

import backend.app.v1.services as services
import backend.connection.v1.models as models


def create_schedule(name: str, description: str, created_by: int, db_session) -> bool:

    try:
        user_id = db_session.execute(
            select(
                models.User.user_id
            ).where(
                models.User.user_id == created_by
            )
        ).scalar()
        
        group_id: str = services.create_group(name= name, db_session= db_session)

        new_schedule = models.Schedule(
            name = name,
            description = description,
            status = "active",
            group_id = group_id,
            created_by = user_id,
        )

        db_session.add(new_schedule)
        db_session.commit()
        return True
    except:
        db_session.rollback()
        return False

def update_schedule(orig_name: str, orig_description: str, new_name: str | None, new_description: str | None, db_session) -> None:
    
    new_name = orig_name if new_name is None else new_name
    new_description = orig_description if new_description is None else new_description
    
    #---- Values that can be changed: name, desc ----
    
    try:
        db_session.execute(
            update(
                models.Schedule
            ).where(
                models.Schedule.name == orig_name,
                models.Schedule.description == orig_description,
                models.Schedule.created_by == ...,
            ).values(
                name = new_name,
                description = new_description,
            )
        )
    except Exception:
        raise NotImplementedError