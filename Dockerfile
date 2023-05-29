FROM python:3.9
ADD main.py .
RUN pip install requests flask
EXPOSE 8080
CMD ["python", "./main.py"]