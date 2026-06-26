import os

from hashlib import sha256 as algorithm

def hash_string(input , hash_salt = os.getenv("HASH_SALT")) -> str:
    return algorithm((input + hash_salt).encode()).hexdigest()