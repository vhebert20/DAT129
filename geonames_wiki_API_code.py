# -*- coding: utf-8 -*-
"""
Created on Wed Mar 4 2021
Virginia Hebert
DAT129 - Python 2
"""

import requests, json


def build_URL(search):
    # connect to NHTSA API by building URL-encoded GET request
    # API Endpoint:"front door our API server"
    API_ENDPOINT = 'http://api.geonames.org/wikipediaSearchJSON?q=%s&maxRows=10&username=vhebert20' % (search)
    # https://www.geonames.org/export/ws-overview.html
    # create the full URL
    full_url = API_ENDPOINT
    print('URL: ', full_url)
    return full_url

def make_api_request(url):
    # send out the request for information
    response = requests.get(url)
    # when we get the response, we'll check its status to see if all is well
    print('Made request, response status: ', response.status_code)
    # 200 is OK
    if(int(response.status_code) == 200):
        payload_obj = json.loads(response.text)
        return payload_obj
    else:
        return None

def parse_wiki_data(results):
    # iterate over list
    information = results['geonames']
    for index in range(len(information)):
        print(information[index])
        print()
        
def fancy_print(results):
        # iterate over list
    information = results['geonames']
    for index in range(len(information)):
        if 'elevation' in information[index]:
            print('title: ', information[index]['title'])
            print(information[index]['summary'])
            print('elevation: ', information[index]['elevation'])
            print('lat: ', information[index]['lat'])
            print('long: ', information[index]['lng'])
        else:
            print('title: ', information[index]['title'])
            print(information[index]['summary'])
            print('lat: ', information[index]['lat'])
            print('long: ', information[index]['lng'])
        print()

def main():
    thing = input("Please give me a topic of interest: ")
    print()
    url = build_URL(thing)
    print()
    returned_info = make_api_request(url)
#    print(returned_info)
    print()
#    parse_wiki_data(returned_info)
    fancy_print(returned_info)


main()