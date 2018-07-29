#coding:utf-8
import urllib2
import re

url = "http://mirrors.163.com/debian-cd/"
response = urllib2.urlopen(url)
html = response.read()
release_list = re.findall(r'<a href="[^.].*?">(.*?/)</a>',html)
print(release_list)

print('---------------ok--')
for i in xrange(0,len(release_list)):
    html2 = urllib2.urlopen(url+release_list[i]).read()
    sub_list = re.findall(r'<a href="[^.].*?">(.*?/)</a>', html2)
    print(sub_list)
    print('--------------')
print("nothing")

