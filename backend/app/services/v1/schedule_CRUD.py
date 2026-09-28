from sqlalchemy import select

import backend.app.services.v1 as v1
import backend.connection.v1.models as models


def create_schedule(name: str, description: str, created_by: int, db_session) -> bool:

    group_id: int = v1.create_group()
    try:
        new_schedule = models.Schedule(
            name = name,
            description = description,
            status = ...,
            group_id = group_id,
            created_by = created_by,
        )

        db_session.add(new_schedule)
        db_session.commit()
    except:
        db_session.rollback()