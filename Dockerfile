FROM python:3

WORKDIR /usr/src/projeto-estatistica

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8050

CMD [ "python", "./app.py" ]