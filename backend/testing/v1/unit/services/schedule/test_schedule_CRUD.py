import pytest
from sqlalchemy import select 

from backend.testing.v1.conftest import MIXED_USERS
import backend.connection.v1.models as models
import backend.app.services.v1.schedule_CRUD as v1
from backend.logging import log_error


def test_create_schedule(db_session):

    for index, user_email in enumerate(MIXED_USERS, start= 1):
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

            if result := v1.create_schedule(
                name= str(new_schedule['name']), 
                description= str(new_schedule['description']), 
                created_by= int(new_schedule['created_by']),
                db_session= db_session,
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
            assert result == False, 'Created a schedule for inexisting user'
        except:
            ...

@pytest.mark.skip
def test_update_schedule(db_session):
    orig_name: str = 'Default Name'
    orig_desc: str = 'Default Desc'
    
    #---- Test Cases -> Full Update | Partial Update | No data to update protection ----
    test_cases = [
        { # 1st - Full Change
            'name': 'Full Change - Name',
            'desc': 'Full Change - Desc',
        },
        { # 2nd - Partial Change
            'name': ' Partial Change - Name',
        },
        { # 3rd - Partial Change
            'desc': 'Partial Change - Desc',
        },
        { # 4th - No Data Change
            'name': 'Default Name',
            'desc': orig_desc
        },
    ]
    
    for case in test_cases:
        result = v1.update_schedule(
            orig_name= orig_name,
            orig_description= orig_desc,
            new_name=case.get('name'),
            new_description=case.get('desc'),
            db_session= db_session,
        )
        
    #---- Iterate through the cases with the same logic ----
    
    #---- Depending on the result send different result_codes ----
    raise NotImplementedError

@pytest.mark.skip
def test_delete_schedule():
    raise NotImplementedError
