import requests
import random
import string

USER_URL = "https://gorest.co.in/public/v1/users"

TOKEN = "f0aeacc6030d0ae1bba96986fbab0e30a211c0f1aa15c52bfc1c380e2b28eb74"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer" + " " + TOKEN
}

def create_user_and_return_email():
    
    # random variable generation part for creating new user

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com','example.com']
    domain = random.choice(domains)

    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # new user data
    
    data = {
        "name": username,
        "email": username + '@' + domain,
        "gender": gender,
        "status": status
    }

    # creating new user with these data

    response = requests.post(USER_URL, headers=headers, json=data)

    assert response.status_code == 201, "for new data response status code is not true"

    if response.status_code == 201:

        response_data = response.json()
        just_data = response_data['data']
        # we need "id" part for posts and todos without "id" we can not create posts or todos
        user_id = just_data['id']
        print(response_data)
    else:
        print(response.status_code)

    return(username,domain,user_id)

def try_create_second_user_with_same_email(need_username,need_domain):

    username = ''.join(random.choices(string.ascii_lowercase, k=10))
    
    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # new user data but with same email
    
    data = {
        "name": username,
        "email": need_username + '@' + need_domain,
        "gender": gender,
        "status": status
    }

    # we are trying to creating new user with these data

    response = requests.post(USER_URL, headers=headers, json=data)

    if response.status_code == 201:
        assert response.status_code == 201
        response_data = response.json()
        print(response_data)
    else:
        assert response.status_code == 422
        response_data = response.json()
        print(response_data)

first_username, first_domain, first_user_id = create_user_and_return_email()
try_create_second_user_with_same_email(first_username, first_domain)

def uptade_first_user(need_first_user_id):
    
    # random variable generation part for creating new user

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com','example.com']
    domain = random.choice(domains)

    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # user data for uptade
    
    data = {
        "name": username,
        "email": username + '@' + domain,
        "gender": gender,
        "status": status
    }

    # uptading user1 with these data

    url_with_user = USER_URL + "/" + str(need_first_user_id)

    response = requests.put(url_with_user, headers=headers, json=data)

    assert response.status_code == 200, "for new data response status code is not true"

    if response.status_code == 200:

        response_data = response.json()
        print(response_data)
    else:
        print(response.status_code)

    return(username,domain)

updated_first_username, updated_first_domain = uptade_first_user(first_user_id)

# we will see again we can not craete with same email but at the same time we will check this skill works for uptades 

try_create_second_user_with_same_email(updated_first_username, updated_first_domain)

def create_second_user_with_first_email(need_first_username, need_first_domain):

    # random variable generation part for creating new user

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # new user data
    
    data = {
        "name": username,
        "email": need_first_username + '@' + need_first_domain,
        "gender": gender,
        "status": status
    }

    # creating new user with these data

    response = requests.post(USER_URL, headers=headers, json=data)

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

# But this time this email adress free, we can use it

second_user_id = create_second_user_with_first_email(first_username, first_domain)


def try_to_uptade_second_user_with_updated_first_user_same_email(need_updated_first_username, need_updated_first_domain, need_second_user_id):
    
    # random variable generation part for creating new user

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # user data for uptade
    
    data = {
        "name": username,
        "email": need_updated_first_username + '@' + need_updated_first_domain,
        "gender": gender,
        "status": status
    }

    # uptading user2 with these data

    last_url = USER_URL + "/" + str(need_second_user_id)

    response = requests.put(last_url, headers=headers, json=data)

    assert response.status_code == 422

    response_data = response.json()

    print(response_data)

# we try to with another valid email

try_to_uptade_second_user_with_updated_first_user_same_email(updated_first_username, updated_first_domain, second_user_id)

