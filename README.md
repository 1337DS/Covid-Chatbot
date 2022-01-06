# Covid-Chatbot
The chatbot should answer the questions of the user to topics concerning Covid-19.

The bot will display r-index and similar up-to-date statistics as well as information on how to prevent and cope with covid. A focus of the bot is on creating statistics as plots. To achieve this the text input is interpreted and reasonable x and y-axis labels are applied. The data for the plot is received through APIs from credible sources like the Robert Koch Institute.

## Status: 
API running: :heavy_check_mark:

Rasa connected: :heavy_check_mark:  

Working Functions: 1

GUI: coming soon

## Installation Instructions:
docker network create rasa_project &&
docker run -d -v ${pwd}/actions:/app/actions --net rasa_project --name action-server rasa/rasa-sdk:3.0.2 &&
docker run -v ${pwd}:/app rasa/rasa:3.0.4-full train --domain domain.yml --data data --out models #train
ocker run -it -v ${pwd}:/app -p 5005:5005 --net rasa_project rasa/rasa:3.0.4-full shell

## Team members:

Andreas Edte  
Canberk Alkan  
Dominic Viola  
Jendrik Hülsmeyer  
Johannes Damke  
Killian Ebi  
