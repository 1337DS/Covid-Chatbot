<!-- docker rasa powershell-based commands

docker run -v ${pwd}:/app rasa/rasa:3.0.4-full train --domain domain.yml --data data --out models #train


network for seperate host of actions

#########

docker run -d -v ${pwd}/actions:/app/actions --net rasa_project --name action-server rasa/rasa-sdk:3.0.2

docker run -v ${pwd}:/app rasa/rasa:3.0.4-full train --domain domain.yml --data data --out models


docker run -it -v ${pwd}:/app -p 5005:5005 --net rasa_project rasa/rasa:3.0.4-full shell

########## -->