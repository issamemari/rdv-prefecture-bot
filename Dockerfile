FROM selenium/standalone-chrome:latest

USER root

# Install python3.11
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.11 python3.11-dev python3.11-distutils
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

# Install pipenv
RUN pip install pipenv==2022.9.24

COPY . /bot
WORKDIR /bot

# Install dependencies
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "src/main.py"]
