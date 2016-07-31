__author__ = 'sl'

import random
import string
import hashlib
import hmac
'''
Module contains common functions to be used for
hashing - either cookies or passwords or whatever les;
'''

DIVIDER = "|"


def make_salt():
    return ''.join(random.choice(string.ascii_letters) for n in range(5))


#Creates password hash in format hash + divider + salt
# uses sha256
def make_pw_hash(name, pw, salt = ""):
    if salt == "":
        salt = make_salt()
    h = hashlib.sha256(name+pw+salt).hexdigest()
    return (str(h)) + DIVIDER + salt


# validates password based on provided user name, passwot and hash value
# where hash value ==  hash(pws + salt) + divider + salt
def valid_pw(name, pw, h):
    salt = h.split(DIVIDER)[1]
    if h == make_pw_hash(name, pw, salt):
        return True

    return False


#following functions are to be used for coockie hashing
SECRET = 'imsosecret'
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return s + DIVIDER + hash_str(s)

def check_secure_val(h):
    val = h.split(DIVIDER)[0]
    if h == make_secure_val(val):
        return val


def make_secure_cookie(s):
    return make_secure_val(s)

def is_cookie_secure(cookie):
    return check_secure_val(cookie)