from util import create_new_user
from util import create_new_post
import requests

USER_URL = "https://gorest.co.in/public/v1/users"
BASE_URL= "https://gorest.co.in/public/v1/"

TOKEN = "f0aeacc6030d0ae1bba96986fbab0e30a211c0f1aa15c52bfc1c380e2b28eb74"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer" + " " + TOKEN
}

def create_new_user_fail():

    # new user data (empty)
    
    data = {
        
    }

    # we can't craete a new user because all these data mandatory for new user

    # we will see "[{'field': 'email', 'message': "can't be blank"}, 
    # {'field': 'name', 'message': "can't be blank"}, 
    # {'field': 'gender', 'message': "can't be blank, can be male of female"}, 
    # {'field': 'status', 'message': "can't be blank"}]}"
    # and "422" (Data validation failed (in response to a POST request, for example). 
    # (Please check the response body for detailed error messages.)

    response = requests.post(USER_URL, headers=headers, json=data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 422

create_new_user_fail()

def create_new_post_fail(user_id):

    # new post data (empty)

    data = {
        
    }

    # we can't craete a new post because all these data mandatory for new post

    # we will see {'field': 'title', 'message': "can't be blank"},
    # {'field': 'body', 'message': "can't be blank"}
    # and "422" (Data validation failed (in response to a POST request, for example). 
    # (Please check the response body for detailed error messages.)

    # we need new url with "id"

    url_with_user = USER_URL + "/" + str(user_id) + "/" + "posts"

    # creating new post with these data

    response = requests.post(url_with_user, headers=headers, json=data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 422

def create_new_todos_fail(user_id):

    # new todo data (empty)

    data = {
        
    }

    # we can't craete a new todo because all these data mandatory for new todo

    # we will see {'field': 'title', 'message': "can't be blank"}, 
    # {'field': 'status', 'message': "can't be blank, can be pending or completed"}
    # and "422" (Data validation failed (in response to a POST request, for example). 
    # (Please check the response body for detailed error messages.)

    # we need new url with "id"

    url_with_user = USER_URL + "/" + str(user_id) + "/" + "todos"

    response = requests.post(url_with_user, headers=headers, json=data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 422

# we return "user_id" for new posts and we have to start from new_user part because we can't do anything without "user_id"

user_id_for_post_todos_fail = create_new_user()

# we used "user_id" for new posts

create_new_post_fail(user_id_for_post_todos_fail)

# we used "user_id" for new todos

create_new_todos_fail(user_id_for_post_todos_fail)

def create_new_comments_fail(post_id):

    # new comment data (empty)

    data = {
        
    }

    # we can't craete a new comments because all these data mandatory for new comments
    # we will see {'field': 'name', 'message': "can't be blank"}, 
    # {'field': 'email', 'message': "can't be blank, is invalid"}, 
    # {'field': 'body', 'message': "can't be blank"}
    # and "422" (Data validation failed (in response to a POST request, for example). 
    # (Please check the response body for detailed error messages.)

    # we need new url with "post_id"

    url_with_posts = BASE_URL + "/posts/" + str(post_id) + "/" + "comments"

    # creating new comment with these data

    response = requests.post(url_with_posts, headers=headers, json=data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 422

# we return "user_id" for new posts and we have to start from new_user part because we can't do anything without "user_id"

user_id_for_comments_fail  = create_new_user()

# we used "user_id" for new posts and we return "user_id_post" for new comments

user_id_post_for_comments_fail = create_new_post(user_id_for_comments_fail)

# we used "user_id_post" for new posts

create_new_comments_fail(user_id_post_for_comments_fail)