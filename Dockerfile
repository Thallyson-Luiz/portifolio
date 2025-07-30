FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN cd portifolio && pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "portifolio/manage.py", "runserver" , "0.0.0.0:8000" ]

