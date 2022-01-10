#Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.0.1
#Use subdirectory as working directory
WORKDIR /app

#Copy any additional custom requirements, if necessary (uncomment next line)
COPY rki_api_v1.py ./
COPY requirements.txt ./

#Change back to root user to install dependencies
USER root

# To install system dependencies
# RUN apt-get update -qq && \
#     apt-get install -y ngrok && \
#     apt-get clean

#Copy actions folder to working directory
COPY actions /app/
#ADD actions/* /app/

#Install extra requirements for actions code, if necessary (uncomment next line)
RUN /opt/venv/bin/python -m pip install --upgrade pip
RUN pip3 install -r ./requirements.txt
#By best practices, don't run the code with root user


#WORKDIR /
ENTRYPOINT ["./entrypoint.sh"]
USER 1000
EXPOSE 5005
CMD ["start" "actions" "--actions"]