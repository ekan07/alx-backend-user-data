#!/usr/bin/env python3
"""
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication
        """
        if path is not None and excluded_paths is not None:
            for exc_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exc_path[-1] == "*":
                    pattern = "{}.*".format(exc_path[0:-1])
                elif exc_path[-1] == "/":
                    pattern = "{}/*".format(exc_path[0:-1])
                else:
                    pattern = "{}/*".format(exc_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ handles authorization header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user
        """
        return None