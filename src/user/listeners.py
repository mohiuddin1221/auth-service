from sqlalchemy import event, insert
from .models import User, UserProfile


@event.listens_for(User, 'after_insert')
def receive_after_insert(mapper, connection, target):

    user_id = target.uid
    print(f"User created with id={user_id}")

    connection.execute(insert(UserProfile).values(
        user_uid=user_id,
        bio="",
        profile_image=""
    ))
