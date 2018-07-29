#coding:utf-8
import urllib2
import re

url = "http://mirrors.163.com/debian-cd/"
response = urllib2.urlopen(url)
html = response.read()

release_list = re.findall(r'<a href=".*?">(.*?)</a>',html)
print(release_list)

response2 = urllib2.urlopen(url+release_list[1])
print(response2.read())