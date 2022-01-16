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


###wie viele corona faelle es heute gab
class ActionIncidence(Action):
    
    def name(self) -> Text:
        return "give_test_incidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ger = RKI_API.Endpoint_Germany(False)
        df2, updated = ger.get_history("incidence")
        result=df2['weekIncidence'][-1]
        print(result)
        dispatcher.utter_message(text=f"the incidence in germany is: {round(result, 2)} COVID-19 cases per 100'000 population")
        

        return []
    
###wie viele corona tote es letzte woche gab 
class ActionDeaths(Action):
    
    def name(self) -> Text:
        return "give_deaths"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ger = RKI_API.Endpoint_Germany(False)
        df2, updated = ger.get_history("deaths")
        print(df2)
        result=sum(df2['deaths'][-7:])
        print(result)
        dispatcher.utter_message(text=f"there were {round(result, 2)} corona deaths in germany last week")
        

        return []
    


###nennt dir alle corona symptome    
class ActionCoronaSyntoms(Action):
    
    def name(self) -> Text:
        return "give_verify_corona_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
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


###nennt dir alle corona symptome    
class ActionCoronaSyntoms(Action):
    
    def name(self) -> Text:
        return "give_corona_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="""if you suspect you have corona you can do the following:
           \n \u2022 do a PCR or a quick test.
           \n \u2022 alert your GP and make an appointment
           \n \u2022 You can find more information under the following link [here](https://www.who.int/health-topics/coronavirus)""")

        return []



##hier kommt der plot raus und als zweites link(geht noch nicht)

# class ActionIncidence(Action):
    
#     def name(self) -> Text:
#         return "give_test_incidence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         ger = RKI_API.Endpoint_Germany(True)
#         url=ger.get_history("incidence")
#         print(url)
#         dispatcher.utter_message(image=url)
#         dispatcher.utter_message(text=f"hier ist der link [this link]({url})")
        

#         return []
