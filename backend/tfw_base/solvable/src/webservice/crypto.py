from os import urandom
from hashlib import scrypt


class PasswordHasher:
    n = 16384
    r = 8
    p = 1
    dklen = 32

    @classmethod
    def hash(cls, password):
        salt = urandom(32)
        return cls.scrypt(password, salt).hex() + salt.hex()

    @classmethod
    def verify(cls, password, salted_hash):
        salt = bytes.fromhex(salted_hash)[32:]
        hashdigest = bytes.fromhex(salted_hash)[:32]
        return cls.scrypt(password, salt) == hashdigest

    @classmethod
    def scrypt(cls, password, salt):
        return scrypt(password.encode(), salt=salt, n=cls.n, r=cls.r, p=cls.p, dklen=cls.dklen)
