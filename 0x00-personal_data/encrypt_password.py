#!/usr/bin/env python3
"""
Encrypt Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash Password
    """
    salt = bcrypt.gensalt()
    hashedPass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashedPass


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if the Hash password is right
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
