# base python Image (base linux Image)
FROM python:3.9

# work directory
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

#  
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# error 
# COPY ./.env /code/

## ENV DATABASE_USERNAME="neo4j"
## ENV DATABASE_PASSWORD="awt2022"
## ENV DATABASE_URL="bolt://localhost:7687"
## ENV DATABASE_URL="neo4j://localhost:7687"

# we copy all the code to COPY ./app /code/app 
COPY ./main.py /code/
## main.py

# Set the command to run the uvicorn server.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
## docker build -t myimage .
## docker run -d --name mycontainer -p 80:80 myimage
# docker run --name mycontainer -p 80:80 myimage