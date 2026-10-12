from sqlalchemy import select

import backend.app.services.v1 as v1
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
        
        group_id: str = v1.create_group(name= name, db_session= db_session)

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