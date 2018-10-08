
import urllib2
import json
import time
import socket
import sys

versions_list = ['1.0.5.120','1.0.6.120']
addresses_list = ['http://localhost:8000/5.json', 'http://localhost:8000/6.json']
query_address = 'http://localhost:8000/query.json'

count = 1

while True:
  print("count: %d" % count)
  # step = count % 2
  qurey_count = 5*60/10
  version = ''

  while qurey_count > 0 and version == '': 
    try: 
      query_result  = urllib2.urlopen(query_address, timeout = 1).read()
      json_qurey_result = json.loads(query_result)
      version = json_qurey_result['version']

    except urllib2.URLError, e:
      # For Python 2.7
      time.sleep(2)
      qurey_count -= 1
      # print qurey_count
      sys.stdout.write('=')
      sys.stdout.flush()


  # json_qurey_result = json.loads(query_result)
  # version = json_qurey_result['version']
  print("current version is %s" % version)
  version_index = versions_list.index(version)
  addresses_index = (version_index + 1) % 2
  print("do call %s to update to %s" % (addresses_list[addresses_index], versions_list[addresses_index]))
  count += 1
  time.sleep(15)	

