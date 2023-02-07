#!/usr/bin/env python3
""" Main 0
Run: API_HOST=0.0.0.0 API_PORT=5000 python3 -m test.main_0
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.authorization_header())
print(a.current_user())
