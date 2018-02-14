# Docker Container Example Running NewsApi Python Client 

####

This is a simple example of how to utilize NewsApi Python client within a Docker container.

### Requirements

- Docker

### Setup 

##### Docker

Build the container from the Dockerfile
```commandline
docker build -t newsapi .
```

Run the container. Define the environment variables.
Replace the api_key with your credentials.

```commandline
docker run -e api_key='XXXXXXXX' -t newsapi
```


## Usage

Check the container output and you will see a simple printout of the top headlines
for BBC News
