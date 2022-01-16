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




    



# class ActionIncidence(Action):
    
#     def name(self) -> Text:
#         return "give_test_incidence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         #ger = RKI_API.Endpoint_Germany()
#         #df2, updated = ger.get_history("incidence")
#         #result=df2['weekIncidence'][-1]
#         #print(result)
        
#         #r = req.get("https://api.corona-zahlen.org/map/districts-legend")
#         #img = Image.open(BytesIO(r.content))
#         #bild=img.convert("RGB")
#         #bild.save("einjpgbild.jpg")
        
#         #dispatcher.utter_message(image=bild)


#         result="too high"       
#         dispatcher.utter_message(text=f" {result}")

#         return []

    



class ActionLandkreise(Action):
    
    def name(self) -> Text:
        return "give_landkreise_incidence_map"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #r = req.get("https://api.corona-zahlen.org/map/districts-legend")
        #dispatcher.utter_message(image=r)
        dispatcher.utter_message(text="map")

        return []





class ActionCoronaSyntoms(Action):
    
    def name(self) -> Text:
        return "give_corona_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #r = req.get("https://api.corona-zahlen.org/map/districts-legend")
        #dispatcher.utter_message(image=r)
        dispatcher.utter_message(text="""COVID-19 affects different people in different ways. \nMost infected people will develop mild to moderate illness and recover without hospitalization.
           \n \u2022 Most common symptoms:
           \n \u2022 fever
           \n \u2022 dry cough
           \n \u2022 tiredness
           \nLess common symptoms:
           \n\u2022 aches and pains
           \n\u2022 sore throat
           \n\u2022 diarrhoea
           \n\u2022 conjunctivitis
           \n\u2022 headache
           \n\u2022 loss of taste or smell
           \n\u2022 a rash on skin, or discolouration of fingers or toes
           \nSerious symptoms:
           \n\u2022 difficulty breathing or shortness of breath
           \n\u2022 chest pain or pressure
           \n\u2022 loss of speech or movement
           \nSeek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility.
           \nPeople with mild symptoms who are otherwise healthy should manage their symptoms at home.
           \nOn average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.
           \nfor more informations you can click [here](https://www.who.int/health-topics/coronavirus)""")

        return []
    


# class ActionIncidence(Action):
    
#     def name(self) -> Text:
#         return "give_day_incidence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_message_entity = tracker.latest_message['entities']
#         context = ""
#         for entity in user_message_entity:
#             ent = entity['value'].title()


#         result=ent

        
#         #dispatcher.utter_message(image=bild)

#         dispatcher.utter_message(text=f" {result}")

#         return []
    




class ActionDayIncidence(Action):
    
    def name(self) -> Text:
        return "give_test_incidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        user_message_entity = tracker.latest_message['entities']
        context = ""
        for entity in user_message_entity:
            ent = entity['value'].title()


        print(ent)
        result=ent
   
        dispatcher.utter_message(text=f"entity: {result}")

        return []