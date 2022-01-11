# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import rki_api_v1 as RKI_API
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime as dt 


import requests as req
import json
import datetime as dt

# modules for visualization and storing / modifying data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image



class ActionIncidence(Action):
    
    def name(self) -> Text:
        return "give_test_incidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ger = RKI_API.Endpoint_Germany(True)
        #df2, updated = ger.get_history("incidence")
        url=ger.get_history("incidence")
        #result=df2['weekIncidence'][-1]
        #print(result)
        print(url)
        #bild="http://localhost:4321/plot/einjpgbild.jpg"
        #bild="http://localhost:4321/plot/incidence.png"
        #bild="https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
        dispatcher.utter_message(image=url)
        dispatcher.utter_message(text=f"hier ist der link [this link]({url})")
        #dispatcher.utter_message(text=f"the incidence in germany is {result}")
        dispatcher.utter_template(utter_info, tracker,link=url)

        return []
    
    



    
