import pytest
from sqlalchemy import select 

from backend.testing.v1.conftest import MIXED_USERS
import backend.connection.v1.models as models
import backend.app.services.v1.schedule_CRUD as v1
from backend.logging import log_error


@pytest.mark.skip
def test_create_schedule(db_session):

    for index, user_email in enumerate(MIXED_USERS, start= 1):
        if index == 1:
            try:
                user_id = db_session.execute(
                    select(
                        models.User.user_id
                    ).where(
                        models.User.email == user_email
                    )
                ).scalar()

                new_schedule: dict[str, str | int] = {
                    "name" : f"Test_Schedule_of_{user_id}",
                    "description" : "Some desc",
                    "created_by" : user_id
                }

                if v1.create_schedule(
                    name= new_schedule['name'], 
                    description= new_schedule['description'], 
                    created_by= new_schedule['created_by'],
                    ):

                    newly_created_schedule = db_session.execute(
                        select(
                            models.Schedule.name,
                            models.Schedule.description,
                            models.Schedule.group_id,
                        ).where(
                            models.Schedule.created_by == user_id
                        ).order_by(
                            models.Schedule.schedule_id.desc()
                        ).limit(1)
                    ).first()

                    assert newly_created_schedule is not None, 'Newly Created Schedule returned None'
                    assert newly_created_schedule[0] == new_schedule['name'], 'Could not retrieve the name of the schedule'
                    assert newly_created_schedule[1] == new_schedule['description'], 'Could not retrieve the description of the schedule'
                    assert isinstance(newly_created_schedule[2], int), '`group_id` is not a integer value'
            except:
                ...
        elif index == 2:
            result = v1.create_schedule(**new_schedule)
            assert result == False, 'Created a schedule for inexisting user'
        else:
            ...


@pytest.mark.skip
def test_update_schedule():
    raise NotImplementedError

@pytest.mark.skip
def test_delete_schedule():
    raise NotImplementedError
