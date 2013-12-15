import string, os

c = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

p = ''.join(c[ord(os.urandom(1)) % len(c)] for i in range(10))

print p
