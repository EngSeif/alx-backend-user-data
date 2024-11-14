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
        path_two = None
        if path is None:
            return True
        if not path.endswith('/'):
            path_two = path + '/'
        else:
            path_two = path[:-1]
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        if path_two in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        public method
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user
        public method
        """
        return None
