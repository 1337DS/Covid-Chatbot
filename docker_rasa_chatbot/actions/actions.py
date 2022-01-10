# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
#import rki_api_v1 as RKI_API
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



# import requests as req
# import json
#import datetime as dt

# modules for visualization and storing / modifying data
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt







    

class ActionIncidence(Action):
    
    def name(self) -> Text:
        return "give_test_incidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #ger = RKI_API.Endpoint_Germany()
        #df2, updated = ger.get_history("incidence")
        #result=df2['weekIncidence'][-1]
        #print(result)
        result="too high"
    #    r = req.get("https://api.corona-zahlen.org/map/districts-legend")
   #     img = Image.open(BytesIO(r.content))
  #      bild=img.convert("RGB")
 #       bild.save("einjpgbild.jpg")
#        dispatcher.utter_message(image=bild)

        dispatcher.utter_message(text=f"the incidence in germany is {result}")

        return []
    
    



class ActionLandkreise(Action):
    
    def name(self) -> Text:
        return "landkreise_incidence_map"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        r = req.get("https://api.corona-zahlen.org/map/districts-legend")
        dispatcher.utter_message(image=r)

        return []
    
