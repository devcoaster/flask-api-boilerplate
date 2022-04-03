"""
Base class for api method views.
"""
from flask.views import MethodView


class BaseMethodView(MethodView):
    """
    Shared logic for all api endpoints like auth etc.
    """
    # Decorator functions can be added here.
    # Order here matters, last in list is evaluated first.
    decorators = []