# Python image
FROM python:3.8.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# setup dependencies
RUN apt-get update
RUN apt-get install xz-utils
RUN apt-get -y install curl

# Download latest nodejs binary
RUN curl https://nodejs.org/dist/v14.15.4/node-v14.15.4-linux-x64.tar.xz -O

# Extract & install
RUN tar -xf node-v14.15.4-linux-x64.tar.xz
RUN ln -s /node-v14.15.4-linux-x64/bin/node /usr/local/bin/node
RUN ln -s /node-v14.15.4-linux-x64/bin/npm /usr/local/bin/npm
RUN ln -s /node-v14.15.4-linux-x64/bin/npx /usr/local/bin/npx

# create root directory for our project in the container
RUN mkdir /project

# Set the working directory to /project
WORKDIR /project

# Copy the current directory contents into the container at /project
ADD . /project/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt