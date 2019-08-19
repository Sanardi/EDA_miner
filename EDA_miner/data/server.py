"""
This module is only here because of the Dash app spanning multiple files. \
General configurations of the underlying app and server go here as well.

Global Variables:
    - app: The Dash server, imported everywhere that a dash callback \
           needs to be defined.
    - r: The connection to Redis.
"""

from dash import Dash
from redis import Redis
from flask_caching import Cache

redis_conn = Redis()

app = Dash(__name__, requests_pathname_prefix="/data/",
           assets_external_path="/static/")

app.config["suppress_callback_exceptions"] = True

# app-level cache
cache = Cache(app.server, config={'CACHE_TYPE': 'redis'})
