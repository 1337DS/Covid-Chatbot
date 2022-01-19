# Covid-Chatbot
The chatbot should answer the questions of the user to topics concerning Covid-19.

The bot will display r-index and similar up-to-date statistics as well as information on how to prevent and cope with covid. A focus of the bot is on creating statistics as plots. To achieve this the text input is interpreted and reasonable x and y-axis labels are applied. The data for the plot is received through APIs from credible sources like the Robert Koch Institute.


## possible questions for Carl 

Whats the incidence in Germany?
Whats the incidence in Mannheim?
Whats the incidence in Cottbus?
Give me the incidence map of Germany?
What are Covid-19 symptoms?
How many died last week?
I think i have corona


## Installation Instructions:
*Rasa is required for the execution. If you don't have Rasa installed yet then you can do this e.g. in a Conda environment. For this you should use the command:
pip3 install -U --user pip && pip3 install rasa
*For more information, please follow the instruction of the official Rasa documentation: https://rasa.com/docs/rasa/installation
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


