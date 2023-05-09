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

def create_new_user_for_cheking_inputs():

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

    response = requests.post(USER_URL, headers=headers, json=data)

    # we are going to check status_code if it's different from "201" we will see a warning 

    assert response.status_code == 201, "response status code is not true"

    if response.status_code == 201:

        response_data = response.json()
        print(response_data)

        # data verification part
        assert response.json()["data"]["name"] == username, "username is not true"
        assert response.json()["data"]["email"] == username + '@' + domain, "email is not true"
        assert response.json()["data"]["gender"] == gender, "gender is not true"
        assert response.json()["data"]["status"] == "busy", "status is not true"
    
create_new_user_for_cheking_inputs()