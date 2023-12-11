FROM python:3.9
WORKDIR app
COPY . .
RUN pip install plyer
CMD ["python","reminder.py"]