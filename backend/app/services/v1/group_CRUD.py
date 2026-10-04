from sqlalchemy import select
from uuid import uuid4

import backend.app.services.v1 as v1
import backend.connection.v1.models as models

def create_group(name: str, db_session) -> str:

    try:
        uuid: str = str(uuid4())
        new_group = models.Group(
            name = name,
            unique_uuid = uuid,
            # created_by = ...,
        )
        db_session.add(new_group)
        db_session.commit()
    except:
        raise

    return uuid