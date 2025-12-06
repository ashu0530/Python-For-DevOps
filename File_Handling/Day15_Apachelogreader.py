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
    print(type(logreader))
#    print(logreader)
    out = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', logreader)
    print(out)
    m = out.group('IP')
    print(m)


line = '127.0.0.1 - rj [13/Nov/2019:14:34:30 -0000] "GET HTTP/1.0" 200'
regularexpressionforip = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
ip = re.search(regularexpressionforip,line)
print(ip)
onlyip= ip.group('IP')
print(onlyip)


'''
\s	Matches one whitespace (space, tab, etc.) — in your log it's the space before timezone
[-+]	Matches either - or + (timezone can start with either)
\d{4}	Matches exactly 4 digits – timezone offset (e.g., 0000, 0530, 0800)
\]	Matches the closing square bracket ]
'''
line = '127.0.0.1 - rj [13/Nov/2019:14:34:30  -0000] "GET HTTP/1.0" 200'
regularexpressionfortime =  r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\s\s[-+]\d{4}\]'                #r'\[(?P<Time>\d+/\w+/\d+:\d+:\d+:\d+)\]'
time = re.search(regularexpressionfortime,line)
print(time)
onlytime = time.group('Time')
print(onlytime)


#print request
regexpformethod = r'\"(?P<method>\w+\s\w+/\d+\.\d+\"\s\d+)'
requestvar = re.search(regexpformethod,line)
print(requestvar)
onlyrequest = requestvar.group('method')
print(onlyrequest)


#print only ip
path = r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\apache.log'
with open(path,'r') as log:
    logoutvar=log.readlines()
    print(type(logoutvar))
    logoutvar = str(logoutvar)
    print(type(logoutvar))
    print(logoutvar)
    regexpforip = r'(?P<ip>\d+\.\d+\.\d+\.\d+)'   
    ip = re.search(regexpforip,logoutvar)
    print(ip)


# Use the finditer method to process the log, printing the IP addresses of the matching lines:

    # matchedip = re.finditer(regexpforip,logoutvar)
    # for m in matchedip:
    #     print(m.group('ip'))











#full function for finding ip in logs with error handling

import re
def findingIp():
    logspath = r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\apache.log'
    regularexp = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'

    try:
        with open(logspath,'r') as file:
            logvar = str(file.readlines())
#            output = re.search(regularexp,logvar)

            allmatchIp = re.finditer(regularexp,logvar)
            for i in allmatchIp:
                print("Found IP are : ",i.group('IP'))

    except Exception as e:
        print("Program error",e)


findingIp()
print("Program ended")
        

















