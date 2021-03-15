#!/usr/bin/env python3

import os
import requests

# external ip address for qwiklabs
corpweb_extip = "34.70.247.156"
url = "http://{}/feedback/".format(corpweb_extip)

# depending on linux use below (/data/feedback/)
# feedback_dir = os.path.join(os.sep, "data", "feedback", "")

# depending on windows use below (data/feedback/)
feedback_dir = os.path.join("data", "feedback", "")

# list name file in /data/feedback
feedback_list = os.listdir(feedback_dir)


def prosess_text():
    """
    Used to perform the process of changing from file.txt to a list dictionary
    :rtype: list
    :return: list of dict text
    """
    list_dict = []
    key = ['title', 'name', 'date', 'feedback']
    for name_file in feedback_list:
        file_dir = os.path.join(feedback_dir, name_file)
        with open(file_dir) as file:
            text_list = [n.strip() for n in file]
            text_dict = {}
            for index, value in enumerate(text_list):
                text_dict[key[index]] = value
            list_dict.append(text_dict)
    return list_dict


def post_request():
    """
    Performs HTTP protocol to post dict data requests to the url from the extracted file.txt
    """
    p = prosess_text()
    for data in p:
        response = requests.post(url, data=data)
        if response.ok and response.status_code == 201:
            print("Success")
        else:
            raise Exception("GET failed with status code {}".format(response.status_code))


if __name__ == '__main__':
    post_request()
