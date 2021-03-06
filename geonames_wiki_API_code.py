# -*- coding: utf-8 -*-
"""
Created on Wed Mar 5 2021
Virginia Hebert
DAT129 - Python 2
"""

import requests, json, csv


def build_URL(search):
    # connect to NHTSA API by building URL-encoded GET request
    # API Endpoint: "front door our API server"
    # currently set up to return only 10 search results
    API_ENDPOINT = 'http://api.geonames.org/wikipediaSearchJSON?q=%s&maxRows=10&username=vhebert20' % (search)
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

def print_to_file(results):
    # print results to list
    information = results['geonames']
    # establish field names
    fieldnames = ['title', 'feature', 'summary', 'elevation', 'lat', 'lng', 'countryCode', 'wikipediaUrl', 'rank', 'geoNameId', 'thumbnailImg', 'lang']
    with open('wiki_search.csv', 'w') as search_output: 
        # link field names and assign line end terminator to remove blank line in csv
        written_file = csv.DictWriter(search_output, fieldnames = fieldnames, lineterminator = '\n')
        # write field names
        written_file.writeheader()
        # pull in information based on field names
        written_file.writerows(information)
    return

def fancy_print(results):
    # iterate over list and print out values of interest
    information = results['geonames']
    for index in range(len(information)):
        if 'elevation' in information[index]:
            print('title: ', information[index]['title'])
            print(information[index]['summary'])
            print('elevation: ', information[index]['elevation'])
            print('lat: ', information[index]['lat'])
            print('long: ', information[index]['lng'])
            print()
        else:
            print('title: ', information[index]['title'])
            print(information[index]['summary'])
            print('lat: ', information[index]['lat'])
            print('long: ', information[index]['lng'])
            print()
    return


def main():
    thing = input("Please give me a topic of interest: ")
    print()
    url = build_URL(thing)
    print()
    returned_info = make_api_request(url)
    print()
    fancy_print(returned_info)
    print_to_file(returned_info)


main()
