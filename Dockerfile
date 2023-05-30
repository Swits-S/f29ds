FROM python:3.9
ADD routes.py .
COPY templates /templates
RUN pip install requests flask mysql-connector-python yagmail jinja2
EXPOSE 8080
CMD ["python", "./routes.py"]