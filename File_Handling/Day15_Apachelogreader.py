'''
Docstring for File_Handling.Day15_Apachelogreader

The Apache HTTP server is an open source web server widely used to serve web con
tent. The web server can be configured to save log files in different formats. One
 widely used format is the Common Log Format (CLF). A variety of log analysis tools
 can understand this format. Below is the layout of this format:
 <IP Address> <Client Id> <User Id> <Time> <Request> <Status> <Size>
 What follows is an example line from a log in this format:
 127.0.0.1 - swills [13/Nov/2019:14:43:30 -0800] "GET /assets/234 HTTP/1.0" 200 2326
'''
import re
with open(r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\apache.log','r') as apachelog:
    logreader = apachelog.readlines()
    logreader=str(logreader)
#    print(logreader)
    out = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', logreader)
    print(out)
    m = out.group('IP')
    print(m)