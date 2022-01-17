# Covid-Chatbot
The chatbot should answer the questions of the user to topics concerning Covid-19.

The bot will display r-index and similar up-to-date statistics as well as information on how to prevent and cope with covid. A focus of the bot is on creating statistics as plots. To achieve this the text input is interpreted and reasonable x and y-axis labels are applied. The data for the plot is received through APIs from credible sources like the Robert Koch Institute.

## Status: 
API running: :heavy_check_mark:

Rasa connected: :heavy_check_mark:  

Working Functions: +6

GUI: :heavy_check_mark:  

Docker Deployment: in progress

## To Do
- Custom Actions erweitern

- Anzeige Grafen + Karte (möglich?)

- Portierung in Docker

- evtl. GUI ändern


## Installation Instructions:
install rasa
install ner_crf
*Start rasa*
rasa run -m models --enable-api --cors "*" --debug
*Start actionserver*
rasa run actions
*Start Imageserver*
python3 picture_server.py

## Team members:

Andreas Edte  
Canberk Alkan  
Dominic Viola  
Jendrik Hülsmeyer  
Johannes Damke  
Killian Ebi  
