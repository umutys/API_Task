from util import create_new_user
from util import create_new_post
from util import create_new_comments
from util import create_new_todos

valid_user_id = create_new_user()

valid_post_user_id = create_new_post(valid_user_id)

create_new_comments(valid_post_user_id)

create_new_todos(valid_user_id)