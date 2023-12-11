FROM python:3.9
WORKDIR app
COPY . .
RUN pip install plyer
EXPOSE 8000
CMD ["python","reminder.py"]