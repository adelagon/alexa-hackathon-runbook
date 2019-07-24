"""
This is a boilerplate code in python that you can use as a template
To build your Alexa skill for the hackathon.
"""
import requests
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler,
    AbstractExceptionHandler)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

    
class LaunchRequestHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle your skill's LaunchRequest
    or Invocation.
    """
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        """
        TODO: Implement your Invocation handler here
        """


class HelpIntentHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle 'Help' intent.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)
        
    def handle(self, handler_input):
        """
        TODO: Implement your HelpIntent handler here
        """
        
class StopIntentHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle 'Stop' intent.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.StopIntent")(handler_input)
        
    def handle(self, handler_input):
        """
        TODO: Immplent your StopIntent handler here
        """


class FallbackIntentHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle utterances that do not
    match any of your skill's intents.
 
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)
        
    def handle(self, handler_input):
        """
        TODO: Implement your FallbackIntent handler here
        """


class AllExceptionHandler(AbstractExceptionHandler):
    """
    This is a catch all exception handler to your skill, to ensure the skill
    returns a meaningful message for all exceptions.
    """
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        """
        TODO: Implement your Exception handler here
        """

"""
After implementing the built-in IntentHandlers, you my implement your Custom
IntentHandlers here. Be sure that you add them on your SkillBuilder instance
"""

# Initialize Alexa Skill Builder
sb = SkillBuilder()

# Registering the RequestHandlers
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(StopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())

# Registering the ExceptionHandlers
sb.add_exception_handler(AllExceptionHandler())

# Set the lambda_handler to SkillBuilder
lambda_handler = sb.lambda_handler()
