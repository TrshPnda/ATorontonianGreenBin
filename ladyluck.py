#!/usr/bin/python3
##Work in Progress##

import string
import requests
import random
from lxml import html # Look into using re module instead


def optgen(size=6, chars=string.digits): ##random otp generator
  return ''.join(random.choice(chars) for x in range(size))

def login():
  attempts = 0
  counter = 0
  while counter == 0:
    otp = optgen()
    s = requests.Session()
'''
Login Process goes here. 
Thinking of a way to handle different types of logins - 302s, 403s etc
200 and 403 status would be the easiest to implement. 
302 type flows would require a little more thought. Requires conditionals.
def a different function for webapps with crsf tokens? hm.
'''    
    if "" in result.text:
      print(result.cookies['']) #Session Cookie Name
      counter += 1
      return attempts
      return counter
    else:
      pass
      attempts +=1

##Attempting to multi thread###

threads = []

if __name__ == '__main__':
  for i in range (1, 20) :
    worker = login(i) 
    worker.setDaemon(True)
    worker.start()
    threads.append(worker)
  if counter == 1:
    for item in threads:
      item.join()
  print ("This took %d attempts"%attempts)

## Something like that ##

