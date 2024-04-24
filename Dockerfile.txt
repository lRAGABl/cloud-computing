FROM python

RUN apt update

RUN apt install python3 -y

RUN pip install nltk

WORKDIR  /Users/alisoliman/visual studio projects /clod

COPY  paragraphs.txt ./

COPY  app.py ./

CMD [ "python3","./app.py" ]

