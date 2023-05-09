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

    response_data = response.json()

    just_data = response_data['data']

    # we need "id" part for uptade this user

    user_id = just_data['id']

    return(username,domain,user_id)

def test_try_create_second_user(u1,d1):

    username = ''.join(random.choices(string.ascii_lowercase, k=10))
    
    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # new user data but with same email
    
    data = {
        "name": username,
        "email": u1 + '@' + d1,
        "gender": gender,
        "status": status
    }

    # we are trying to creating new user with these data

    response = requests.post(USER_URL, headers=headers, json=data)

    response_data = response.json()

    print(response_data)

    print(response.status_code)

u1_username, u1_domain, u1_user_id = create_user_and_return_email()
test_try_create_second_user(u1_username, u1_domain)

def test_uptade_user1(u1_user_id):
    
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

    url_with_user = USER_URL + "/" + str(u1_user_id)

    response = requests.put(url_with_user, headers=headers, json=data)

    response_data1 = response.json()

    print(response_data1)

    return(username,domain)

u2_username, u2_domain = test_uptade_user1(u1_user_id)

# we will see again we can not craete with same email but at the same time we will check this skill works for uptades 

test_try_create_second_user(u2_username, u2_domain)

def test_try_create_second_user_valid(u1_username, u1_domain):

    # random variable generation part for creating new user

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # new user data
    
    data = {
        "name": username,
        "email": u1_username + '@' + u1_domain,
        "gender": gender,
        "status": status
    }

    # creating new user with these data

    response = requests.post(USER_URL, headers=headers, json=data)

    response_data = response.json()

    just_data = response_data['data']

    print(just_data)

    # we need "id" part for uptade this user

    user_id = just_data['id']

    print(user_id)

    print(response_data)

    return user_id

# But this time this email adress free, we can use it

last_user_id = test_try_create_second_user_valid(u1_username, u1_domain)


def test_uptade_user2(u2_username, u2_domain, last_user_id):
    
    # random variable generation part for creating new user

    username = ''.join(random.choices(string.ascii_lowercase, k=10))

    genders = ['male','female']
    gender = random.choice(genders)

    statuses = ['active','inactive']
    status = random.choice(statuses)

    # user data for uptade
    
    data = {
        "name": username,
        "email": u2_username + '@' + u2_domain,
        "gender": gender,
        "status": status
    }

    # uptading user2 with these data

    last_url = USER_URL + "/" + str(last_user_id)

    response = requests.put(last_url, headers=headers, json=data)

    response_data1 = response.json()

    print(response_data1)

    print(response.status_code)

# we try to with another valid email

test_uptade_user2(u2_username, u2_domain, last_user_id)

