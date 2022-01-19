# Covid-Chatbot
The chatbot should answer the questions of the user to topics concerning Covid-19.

The bot will display r-index and similar up-to-date statistics as well as information on how to prevent and cope with covid. A focus of the bot is on creating statistics as plots. To achieve this the text input is interpreted and reasonable x and y-axis labels are applied. The data for the plot is received through APIs from credible sources like the Robert Koch Institute.

## File structure
The current development state is in the ```rasa_chatbot_v2``` folder. The ```docker_rasa_chatbot``` was our attempt to dockerize the application. However, this was not successfull. The ```Chatbot-Widget``` folder contains the files for the frontend of the chatbot.

## Screencast

https://user-images.githubusercontent.com/77493377/150161105-5233421c-d4e4-45ea-b6e3-c74d02b8a443.mp4


## Possible questions for Carl 

- Whats the incidence in Germany?

- Whats the incidence in Mannheim?

- Whats the incidence in Cottbus?

- Give me the incidence map of Germany?

- What are Covid-19 symptoms?

- How many died last week?

- I think i have corona

> In case Carl doesnt recognize your request, he will give tips to rephrase your question.


## Installation Instructions:

1. *Rasa is required for the execution. If you don't have Rasa installed yet then you can do this e.g. in a Conda environment. For this you should use the command:*

```
pip3 install -U --user pip && pip3 install rasa
```

 *For more information, please follow the instruction of the official Rasa documentation: https://rasa.com/docs/rasa/installation*

2. *Start rasa*

```
rasa run -m models --enable-api --cors "*" --debug
```

3. *Start actionserver*

```
rasa run actions
```

4. *Start Imageserver*

```
python3 picture_server.py
```

5. *Open index.html*
Click on the [index.html](Chatbot-Widget/Chatbot-Widget-main/index.html) file to see the frontend with our mascot Carl Corona 🤖.

## Team members:

Andreas Edte  
Canberk Alkan  
Dominic Viola  
Jendrik Hülsmeyer  
Johannes Damke  
Killian Ebi  


## Some evaluations 

Evaluation metrics for the rasa_chatbot.


<table border="0" columns=2 align="center">
    <tr>
    <col>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163110-d96783e9-4ffc-4537-acaa-847050161655.png" alt="" width=50%></img></th>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163119-e4829812-0448-4d34-8474-b95094213a58.png" alt="" width=100%></img></th>
    </col>
    </tr>
    <tr>
    <col>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163122-2203c17d-6f21-47e4-886b-44b192e2ba3b.png" alt="" width=50%></img></th>
        <td><img src="https://user-images.githubusercontent.com/77493377/150163142-b965cedb-ae13-4e7f-80c3-239bc81df46b.png" alt=""  width=100%></img></th>
    </col>
    </tr>
</table>


