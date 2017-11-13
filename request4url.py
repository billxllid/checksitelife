#!/usr/bin/env python
#_*_coding:utf-8_*_
import requests
import sys

f = open('url_zw.txt', 'r')
url = f.readlines()
length = len(url)
url_result_success=[]
url_result_failed=[]
for i in range(0,length):
    try:
        response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)
        if response.status_code != 200:
            raise requests.RequestException(u"Status code error: {}".format(response.status_code))
    except requests.RequestException as e:
            url_result_failed.append(url[i])
            continue
    url_result_success.append(url[i])
f.close()
result_len = len(url_result_success)
for i in range(0,result_len):
    print '[%d]  %s' % (i+1,url_result_success[i].strip())+' '' ''success'

result_len = len(url_result_failed)
for i in range(0,result_len):
    print '[%d]  %s' % (i+1,url_result_failed[i].strip())+' '' ''!! WARNING !!'
