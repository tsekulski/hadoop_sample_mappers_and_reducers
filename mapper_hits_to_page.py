#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
#       # date, time, store, item, cost, payment = data
        ip_address, identity, username, time, time_zone, request_method,\
            request_path,request_protocol, status, object_size = data
        
        if request_path == '/assets/js/the-associates.js':
            print "{0}\t{1}".format(request_path, status)

#data = '10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202'

#split_data = data.split()

#print split_data
