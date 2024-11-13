#!/usr/bin/env python3
"""
Basic Authentication module
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Base 64 Extractor
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header,
                                       validate=True)
            return decoded.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str) :
        """
        returns the user email and password
        from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if not ':' in decoded_base64_authorization_header:
            return (None, None)
        splitted = decoded_base64_authorization_header.split(':')
        return (splitted[0], splitted[1])
