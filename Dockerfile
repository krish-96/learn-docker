FROM python:3.6
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
RUN mkdir gopi
RUN cd gopi
RUN echo "code cloned successfully" > message.txt
