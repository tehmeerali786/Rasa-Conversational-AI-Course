from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action 
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher 
from rasa_sdk.types import DomainDict

ALLOWED_PIZZA_SIZES = ["small", "medium", "large", "extra-large", "extra large", "s", "m", "l", "xl"]
ALLOWED_PIZZA_TYPES = ["mozarrella", "fungi", "veggie", "pepperoni", "hawaii"]

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ValidateSimplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_pizza_form"

    def validate_pizza_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""

        if slot_value.lower() not in ALLOWED_PIZZA_SIZES:
            dispatcher.utter_message(text = f"We only accept pizza sizes: s/m/l/xl.")
            return {"pizza_size": None}

        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"pizza_size": slot_value}

    def validate_pizza_type(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_type` value."""

        if slot_value not in ALLOWED_PIZZA_TYPES:
            dispatcher.utter_message(text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}.")
            return {"pizza_type": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
        return {"pizza_type": slot_value}

