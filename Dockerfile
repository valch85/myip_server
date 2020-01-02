FROM python:3

WORKDIR /usr/src/app

COPY run.py run.py

CMD [ "python", "run.py" ]