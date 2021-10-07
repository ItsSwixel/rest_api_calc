FROM python:3
ADD /app /app
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN ls -la
CMD ["python", "app/main.py"]