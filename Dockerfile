   FROM python:3.11-slim
    WORKDIR  /app
    COPY requirements.txt /app
    COPY . .
    RUN pip install -r requirements.txt
    EXPOSE 8080
    ENTRYPOINT [ "python" , "app.py" ]
    
