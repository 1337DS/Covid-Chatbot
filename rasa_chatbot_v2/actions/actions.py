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


        user_message_entity = tracker.latest_message['entities']
        ent = ""
        for entity in user_message_entity:
            ent = entity['value'].title()

        if ent!="":


            try:
                ent=int(ent)
            except:
                pass

            print(ent)
            print(type(ent))

            if isinstance(ent,int):
                #dispatcher.utter_message(text=f"entity: {ent}")
                ger = RKI_API.Endpoint_Germany(False)
                df2, updated = ger.get_history("incidence")
                result=np.mean(df2['weekIncidence'][-ent:])
                print(result)
                dispatcher.utter_message(text=f"the mean incidence in germany of the last {ent} days is: {round(result, 2)} COVID-19 cases per 100'000 population")

            else:
                dispatcher.utter_message(text=f"(beta carl): try the same command with init")


        else:
            ger = RKI_API.Endpoint_Germany(False)
            df2, updated = ger.get_history("incidence")
            result=df2['weekIncidence'][-1]
            print(result)
            dispatcher.utter_message(text=f"the incidence in germany is: {int(result)} COVID-19 cases per 100'000 population")
        
        

        return []




class ActionIncidenceAllPlot(Action):
    
    def name(self) -> Text:
        return "give_incidence_all_plot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ger = RKI_API.Endpoint_Germany(True)
        url=ger.get_history("incidence")
        print(url)
        dispatcher.utter_message(image=url)
        dispatcher.utter_message(text=f"hier ist der <a href= {url}>link</a>")
        

        return []


###muss noch gemacht werden
###ruft die inzidenz eines spezifischen Landkreises ab
class ActionIncidenceLandkreis(Action):
    
    def name(self) -> Text:
        return "give_n_landkreis_incidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # ger = RKI_API.Endpoint_Germany(False)
        # df2, updated = ger.get_history("incidence")
        # result=df2['weekIncidence'][-1]
        # print(result)


        user_message_entity = tracker.latest_message['entities']
        context = ""
        for entity in user_message_entity:
            ent = entity['value'].title()


        print(ent)
        result=ent
   
        dispatcher.utter_message(text=f"entity: {result}")
        
        #dispatcher.utter_message(text=f"the Landkreis (entity landkreis) has an incidence of (api landkreis inzidenz) COVID-19 cases per 100'000 population")
        
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
        return "give_corona_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="""COVID-19 affects different people in different ways. <br>Most infected people will develop mild to moderate illness and recover without hospitalization.
           <br>\u2022 Most common symptoms:
           <br>\u2022 fever
           <br>\u2022 dry cough
           <br>\u2022 tiredness
           <br>Less common symptoms:
           <br>\u2022 aches and pains
           <br>\u2022 sore throat
           <br>\u2022 diarrhoea
           <br>\u2022 conjunctivitis
           <br>\u2022 headache
           <br>\u2022 loss of taste or smell
           <br>\u2022 a rash on skin, or discolouration of fingers or toes
           <br>
           <br>Serious symptoms:
           <br>\u2022 difficulty breathing or shortness of breath
           <br>\u2022 chest pain or pressure
           <br>\u2022 loss of speech or movement
           <br>Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility.
           <br>People with mild symptoms who are otherwise healthy should manage their symptoms at home.
           <br>On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.
           <br>\u2022 For more informations you can check the<a href='https://www.who.int/health-topics/coronavirus'>link</a>""")

        return []


###nennt dir alle corona nachweise     
class ActionVerifyCoronaSyntoms(Action):
    
    def name(self) -> Text:
        return "give_verify_corona_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="""if you suspect you have corona you can do the following:
           <br> \u2022 do a PCR or a quick test.
           <br> \u2022 alert your GP and make an appointment
           <br> \u2022 You can find more information under the following <a href='https://www.who.int/health-topics/coronavirus'>link here</a>""")

        return []


####map aller langkreise in de mit corona inzidenz
class ActionLandkreiseMap(Action):
    
    def name(self) -> Text:
        return "give_landkreise_incidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # r = req.get("https://api.corona-zahlen.org/map/districts-legend")
        # dispatcher.utter_message(image=r)
        # #dispatcher.utter_message(text="map")

        # return []


        # r = req.get("https://api.corona-zahlen.org/map/districts-legend")
        # img = Image.open(BytesIO(r.content))
        # bild=img.convert("RGB")
        # bild.save("einjpgbild.jpg")
        
        # dispatcher.utter_message(image=bild)

        bild=("https://api.corona-zahlen.org/map/districts-legend")
        dispatcher.utter_message(image=bild)



        # ger = RKI_API.Endpoint_Germany(True)
        # url=ger.get_history("incidence")
        # print(url)
        # dispatcher.utter_message(image=url)
        # #dispatcher.utter_message(text=f"hier ist der link [this link]({url})")
        

        return []