# Hat aktuell keine Verwendung. Siehe README.md für docker based Ausführungen

FROM python:3.7


RUN pip install rasa

WORKDIR /app
# Takes all files and copies them into the docker  cintainer
COPY . .

# RUN rasa train nlu

# Set user: best practise for security
USER 1001

# For Shells etc.
ENTRYPOINT ["rasa"]

# If Container starts, this will be executed
CMD ["run" , "--enable-api", "--port", "8080"]