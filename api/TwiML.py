import sanic.response
from twilio.twiml.voice_response import VoiceResponse
import sanic.request
from sanic import Blueprint

bp = Blueprint("TwiML")


@bp.route("/hello", methods=["GET", "POST"])
async def post_hello(request: sanic.request.Request):
    response = VoiceResponse()
    response.say('Hello there! You have successfully configured a web hook.')
    response.say('Good luck on your Twilio quest!', voice='woman')
    return sanic.response.text(response, content_type="text/xml")
