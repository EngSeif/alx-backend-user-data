#!/usr/bin/env python3
"""
Basic Authentication module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session Auth Class
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sessionId = uuid.uuid4()
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId
