from sanic import Blueprint
from . import TwiML

bp_group = Blueprint.group(
    TwiML.bp,
    url_prefix="/api",
)
