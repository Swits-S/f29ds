FROM python:3.9
ADD routes.py .
COPY templates /templates
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "./routes.py"]