import requests
import random
import string
import datetime

BASE_URL= "https://gorest.co.in/public/v1/"
USER_URL = "https://gorest.co.in/public/v1/users"

TOKEN = "f0aeacc6030d0ae1bba96986fbab0e30a211c0f1aa15c52bfc1c380e2b28eb74"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer" + " " + TOKEN
}

def create_new_user():

    
    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com','example.com']
    domain = random.choice(domains)
    
    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)
    
    # new user data
    user_data = {
        "name": username,
        "email": username + '@' + domain,
        "gender": gender,
        "status": status
    }

    response = requests.post(USER_URL, headers=headers, json=user_data)

    assert response.status_code == 201, "for new data response status code is not true"

    if response.status_code == 201:

        response_data = response.json()
        just_data = response_data['data']
        # we need "id" part for posts and todos without "id" we can not create posts or todos
        user_id = just_data['id']
        print(response_data)
    else:
        print(response.status_code)

    return user_id

def create_new_post(need_user_id):

    # random variable generation part for creating new post

    title = ''.join(random.choices(string.ascii_lowercase, k=40))
    body = ''.join(random.choices(string.ascii_lowercase, k=50))
    
    # new user data
    post_data = {
        "title": title,
        "body": body,
    }

    # we need new url with "user_id"
    url_with_user = USER_URL + "/" + str(need_user_id) + "/" + "posts"

    # creating new post with these data
    response = requests.post(url_with_user, headers=headers, json=post_data)

    assert response.status_code == 201, "for new post response status code is not true"

    if response.status_code == 201:
        response_data_post = response.json()
        just_post_data = response_data_post['data']
        # we need "id" part again for comments part
        user_id_post = just_post_data['id']
        print(response_data_post)
    else:
        print(response.status_code)

    return user_id_post

def create_new_comments(need_post_id):

    # random variable generation part for creating new comments

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com','example.com']
    domain = random.choice(domains)

    body = ''.join(random.choices(string.ascii_lowercase, k=20))
    
    comment_data = {
        "name": username,
        "email": username + '@' + domain,
        "body": body
    }

    # we need new url with "post_id"

    url_with_posts = BASE_URL + "/posts/" + str(need_post_id) + "/" + "comments"

    # creating new comment with these data

    response = requests.post(url_with_posts, headers=headers, json=comment_data)

    assert response.status_code == 201, "for new comments response status code is not true"

    if response.status_code == 201:
        response_data_comment = response.json()
        print(response_data_comment)
    else:
        print(response.status_code)

def create_new_todos(need_user_id):

    # random variable generation part for creating new todos

    year = random.randint(2023, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day)

    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    microsecond = random.randint(0, 999999)
    time = datetime.time(hour, minute, second, microsecond)

    iso_dt = datetime.datetime.combine(date, time).isoformat()

    statuses = ['completed', 'pending']
    status = random.choice(statuses)

    title = ''.join(random.choices(string.ascii_lowercase, k=50))
    
    todo_data = {
        "title": title,
        "due_on": iso_dt,
        "status": status
    }

    # we need new url with "id"

    url_with_user = USER_URL + "/" + str(need_user_id) + "/" + "todos"

    response = requests.post(url_with_user, headers=headers, json=todo_data)

    assert response.status_code == 201, "for new todo response status code is not true"

    if response.status_code == 201:
        response_data_todo = response.json()
        print(response_data_todo)
    else:
        print(response.status_code)