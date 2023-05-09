import random
import string
import requests

# We need to different data types

username = ''.join(random.choices(string.ascii_lowercase, k=10))

domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com','example.com']
domain = random.choice(domains)

genders = ['male','female']
gender = random.choice(genders)

statuses = ['active','inactive']
status = random.choice(statuses)

# these are our data types
# if we want to more data types we can add more data (do not forget add the list)

data1 = {
    "name": username,
    "email": '@' + domain,
    "gender": gender,
    "status": status
}

data2 = {
    "name": username,
    "email": username + domain,
    "gender": gender,
    "status": status
}

data3 = {
    "name": username,
    "email": username + '@' + '.' + domain,
    "gender": gender,
    "status": status
}

data4 = {
    "name": username,
    "email": username + '@' + domain[:-3],
    "gender": gender,
    "status": status
}

data5 = {
    "name": username,
    "email": username + '@',
    "gender": gender,
    "status": status
}

data6 = {
    "name": username,
    "email": "",
    "gender": gender,
    "status": status
}

data7 = {
    "name": username,
    "email": username + '@' + domain + "a" * 250,
    "gender": gender,
    "status": status
}

data8 = {
    "name": username,
    "email": username + '$' + domain,
    "gender": gender,
    "status": status
}

data9 = {
    "name": username,
    "email": username + '@' + '.',
    "gender": gender,
    "status": status
}

data10 = {
    "name": username,
    "email": username + '@' + domain + '_',
    "gender": gender,
    "status": status 
}

data11 = {
    "name": username,
    "email": '/' + username + '@' + domain,
    "gender": gender,
    "status": status
}

data12 = {
    "name": username,
    "email": 'ş' + username + '@' + domain,
    "gender": gender,
    "status": status
}

invalid_data_list = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12]

# do not forget add more data this list!

USER_URL = "https://gorest.co.in/public/v1/users"

TOKEN = "f0aeacc6030d0ae1bba96986fbab0e30a211c0f1aa15c52bfc1c380e2b28eb74"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer" + " " + TOKEN
}

def try_invalid_email():
        
    for i in invalid_data_list:

        # we are using every list elements

        response = requests.post(USER_URL, headers=headers, json=i)
        
        if response.status_code == 201:

            # if we can catch "201" stop the for method and print this data

            print("this mail address is valid" ,i ,response.status_code)

            break

        else:
            
            print(response.status_code, i)
        
try_invalid_email() 
