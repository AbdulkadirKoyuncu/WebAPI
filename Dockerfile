FROM python:latest
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]