#!/usr/bin/env python3
"""
Basic Authentication module
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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
        sessionId = str(uuid.uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value
        """
        sessionId = self.session_cookie(request)
        userId = self.user_id_for_session_id(sessionId)
        return User.get(userId)

    def destroy_session(self, request=None):
        """
        deletes the user session / logout
        """
        if request is None:
            return False
        SessionID_cookie = self.session_cookie(request)
        if SessionID_cookie is None:
            return False
        user_id = self.user_id_for_session_id(SessionID_cookie)
        if SessionID_cookie in self.user_id_by_session_id:
            del self.user_id_by_session_id[SessionID_cookie]
            return True
        return False
