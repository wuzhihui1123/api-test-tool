#!/bin/env python
# coding=utf-8
import configparser
import requests

config = configparser.ConfigParser()
print config.read('../conf/config.ini')
server_host = config['DEFAULT']['SERVER_URL']
default_headers = {"Content-Type": "application/json"}


def __get_server_url(path):
    return server_host + path


def get(path, headers=default_headers, body=None):
    url = __get_server_url(path)
    print "===> [get] | url: {0} | headers: {1} | body: {2}".format(url, headers, body)
    resp = requests.get(url, headers=headers, json=body)
    return resp.json()


def post(path, headers=default_headers, body=None):
    url = __get_server_url(path)
    print "===> [post] | url: {0} | headers: {1} | body: {2}".format(url, headers, body)
    resp = requests.post(url, headers=headers, json=body)
    print resp.content
    return resp.json()
