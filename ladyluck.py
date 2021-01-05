#!/usr/bin/python3
##Work in Progress##

import string
import requests
import random
from lxml import html # Look into using re module instead

def login(otp):
'''
Login Process goes here. 
Thinking of a way to handle different types of logins - 302s, 403s etc
200 and 403 status would be the easiest to implement. 
302 type flows would require a little more thought. Requires conditionals.
def a different function for webapps with crsf tokens? hm.
'''
  if:
    print(result3.cookies['']) #name of cookie variable
  else:
    pass

def optgen(size=6, chars=string.digits):
  return ''.join(random.choice(chars) for x in range(size))
  
def main:
  while counter == 0 
  otp = otpgen()
  login(otp)
## Something like that ##

