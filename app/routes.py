"""
Routes to be registered on app startup.
"""
from app.api import Hello

routes = [
    {
        "rule": "/hello",
        "view_func": Hello.as_view("hello"),
        "methods": ["GET", "POST"],
    }
]