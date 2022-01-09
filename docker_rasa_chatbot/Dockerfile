#Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.0.2

#Use subdirectory as working directory
WORKDIR /app

#Copy any additional custom requirements, if necessary (uncomment next line)
COPY aa_rki_api_v1.py ./
COPY requirements.txt ./


#Change back to root user to install dependencies
USER root

#Copy actions folder to working directory
#COPY actions /app/actions
ADD actions/* /app/


#Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip3 install -r ./requirements.txt

RUN /opt/venv/bin/python -m pip install --upgrade pip
#By best practices, don't run the code with root user
USER 1000

WORKDIR /
docker run -v $(pwd):/app rasa/rasa:3.0.4-full init --no-prompt