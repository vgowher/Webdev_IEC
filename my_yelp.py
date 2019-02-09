#Maintainer Qamber Mehdi
# Created on August 25, 2018

import requests, json

def search_businesses(search_term, search_location):

    api_key = "dthgc1Y5q1UhFvbrCma-C8ip0Q4o-moHUm9EvCwdcj9VvsO19JEQIl4bY3kGyDBUJOYJyPsxPXbUv1jxhCyrFj298L7okeLfgxvpuWNUiO6iaXmQ0Db8SuzoZQdfXHYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = json.loads(businesses_object.text)

    businesses_list = businesses_dict['businesses']

    print(businesses_dict)
    list_of_businesses = []
    for each in businesses_list:
        list_of_businesses.append(each)
    return list_of_businesses
