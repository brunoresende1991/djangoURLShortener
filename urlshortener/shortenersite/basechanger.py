import string
chars = string.digits+string.ascii_lowercase+string.ascii_uppercase
base = len(chars)


def decimal2base_n(n):
     if n>= base:
          return decimal2base_n(n // base) + chars[n % base]
     else:
          return chars[n]

def base_n2decimal(n):
     if len(n) > 1:
          return base_n2decimal(n[:-1]) * base + chars.index(n[-1])
     else:
          return chars.index(n[0])
