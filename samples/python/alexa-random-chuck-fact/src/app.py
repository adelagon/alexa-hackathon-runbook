"""
Author: Alvin A. Delagon <adelagon@amazon.com>
Description:
This is a sample Alexa Skill for lambda written in python. Blurts out
random Chuck Norris facts using the chucknorris.io API. This is meant
to understand how to write Alexa Skills with AWS Lambda.
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


def getChuckFact():
    """
    This is a helper function that collects a random fact from chucknorris.io
    """
    try:
        fact = requests.get("https://api.chucknorris.io/jokes/random")
        return fact.json()['value']
    except requests.RequestException as e:
        print(e)
        raise e

    
class LaunchRequestHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle your skill's LaunchRequest
    or Invocation.
    
    Use 'chuck norris' as an invocation utterance for this RequestHandler
    """
    def can_handle(self, handler_input):
        """
        This class method specifies which is_request_type does this 
        RequestHandler will handle.
        """
        return is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        """
        This class method is then triggered once this RequestHandler 
        """
        speech = "I'm a sample Alexa Skill. Let me give you a random Chuck Norris Fact. "
        speech += getChuckFact()
        speech += ". Do you want more awesome Chuck facts?"
        
        """
        Take note of the set_should_end_session. If set to 'True', the alexa
        skill will gracefully end execution.AbstractExceptionHandler
        
        The set_card method specifies what kind of cards do you want to use when
        interacting with the user via display. A 'SimpleCard' display's text.
        
        For more info about cards, see:
        https://developer.amazon.com/docs/custom-skills/include-a-card-in-your-skills-response.html
        """
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(False)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle 'Help' intent.
    
    For more info about built-in Intents see:
    https://developer.amazon.com/docs/custom-skills/standard-built-in-intents.html
    
    Use: 'help' as an intent utterance for this RequestHandler.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)
        
    def handle(self, handler_input):
        speech = "If you want more Chuck Norris facts. You can say Yes, 'Give "
        speech += "me more!' or 'Another one'. If you want me to stop just say "
        speech += "'Goodbye' or 'Stop'."
        
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(False)
        return handler_input.response_builder.response


class StopIntentHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle 'Stop' intent.
    
    For more info about built-in Intents see:
    https://developer.amazon.com/docs/custom-skills/standard-built-in-intents.html
    
    Use: 'stop' or 'goodbye' as an intent utterance for this RequestHandler.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.StopIntent")(handler_input)
        
    def handle(self, handler_input):
        speech = "As a parting fact before I go:"
        speech += " Chuck Norris' First Program wasn't nicknamed 'HelloWorld' "
        speech += "it was 'GoodbyeWorld'. Goodbye everyone!"
        
        """
        Take note of the set_should_end_session set to True. This pretty much,
        triggers a graceful exit of your Alexa skill
        """
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(True)
        return handler_input.response_builder.response



class AnotherFactHandler(AbstractRequestHandler):
    """
    This is a custom RequestHandler class that will handle 'AChuckFact' intent.
    You can create your own Intents using this RequestHandler sample.
    
    Use: 'give me more' or 'yes' as an intent utterance for this RequestHandler.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AChuckFact")(handler_input)
        
    def handle(self, handler_input):
        speech = "So you like Chuck Norris huh. Let me give you another one. "
        speech += getChuckFact()
        speech += ". Do you want more awesome Chuck facts?"
        
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(False)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """
    This is the RequestHandler class that will handle utterances that do not
    match any of your skill's intents.
    
    For more info about built-in Intents see:
    https://developer.amazon.com/docs/custom-skills/standard-built-in-intents.html
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)
        
    def handle(self, handler_input):
        speech = "Sorry, I can't understand you. Say 'help' if you want know "
        speech += "how to use me."
        
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(False)
        return handler_input.response_builder.response


class CrashHandler(AbstractRequestHandler):
    """
    This is a custom RequestHandler class that will handle 'Crashhandler' intent.
    This is meant to be used to simulate a bug on your Alexa skill. If this
    intent is triggered, the Exception will be handled gracefully by the
    AllExceptionHandler below.
    
    Use: 'crash' as an intent utterance for this RequestHandler.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AChuckFact")(handler_input)
        
    def handle(self, handler_input):
        speech = "So you like Chuck Norris huh. Let me give you another one. "
        speech += getChuckFact()
        speech += ". Do you want more awesome Chuck facts?"
        
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(False)
        return handler_input.response_builder.response
        

class AllExceptionHandler(AbstractExceptionHandler):
    """
    This is a catch all exception handler to your skill, to ensure the skill
    returns a meaningful message for all exceptions.
    """
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        print(exception)

        speech = "Sorry there's a bug on my skill. Go blame the Developer!"
        
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(speech)).set_should_end_session(True)
        return handler_input.response_builder.response


# Initialize Alexa Skill Builder
sb = SkillBuilder()

# Registering the RequestHandlers
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(StopIntentHandler())
sb.add_request_handler(AnotherFactHandler())
sb.add_request_handler(FallbackIntentHandler())

# Registering the ExceptionHandlers
sb.add_exception_handler(AllExceptionHandler())

# Set the lambda_handler to SkillBuilder
lambda_handler = sb.lambda_handler()
