def create_schedule(title: str, description: str, creator: int, db_session) -> bool:
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