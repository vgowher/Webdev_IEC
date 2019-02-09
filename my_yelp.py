<<<<<<< HEAD
import requests

api_key = "dthgc1Y5q1UhFvbrCma-C8ip0Q4o-moHUm9EvCwdcj9VvsO19JEQIl4bY3kGyDBUJOYJyPsxPXbUv1jxhCyrFj298L7okeLfgxvpuWNUiO6iaXmQ0Db8SuzoZQdfXHYx"

url = "https://api.yelp.com/v3/businesses/search"

my_headers = {
    "Authorization": "Bearer %s" % api_key
}

my_params = {
    "term": "restaurants",
    "location": "chicago",
    "limit": 3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

businesses_dict = businesses_object.text

print(businesses_dict)
=======
import requests

api_key = "dthgc1Y5q1UhFvbrCma-C8ip0Q4o-moHUm9EvCwdcj9VvsO19JEQIl4bY3kGyDBUJOYJyPsxPXbUv1jxhCyrFj298L7okeLfgxvpuWNUiO6iaXmQ0Db8SuzoZQdfXHYx"

url = "https://api.yelp.com/v3/businesses/search"

my_headers = {
    "Authorization": "Bearer %s" % api_key
}

my_params = {
    "term": "restaurants",
    "location": "chicago",
    "limit": 3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

businesses_dict = businesses_object.text

print(businesses_dict)
>>>>>>> 0dfa9ec4fe87451058f4311978603dd1d5986dab
