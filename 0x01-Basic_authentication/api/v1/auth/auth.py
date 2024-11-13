#!/usr/bin/env python3
"""
Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class Auth
    Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth public
        method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        public method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user
        public method
        """
        return None
