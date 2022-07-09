from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

from dotenv import load_dotenv, find_dotenv
import os 
import ast

from neo4j import GraphDatabase

load_dotenv(find_dotenv())

def env(key, default=None, required=True):
    """
    Retrieves environment variables and returns Python natives. The (optional)
    default will be returned if the environment variable does not exist.
    """
    try:
        value = os.environ.get(key)
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value
    except KeyError:
        if default or not required:
            return default
        raise RuntimeError("Missing required environment variable '%s'" % key)

DATABASE_USERNAME = env('DATABASE_USERNAME')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_URL = env('DATABASE_URL')


driver = GraphDatabase.driver(uri=DATABASE_URL, auth=(DATABASE_USERNAME, DATABASE_PASSWORD))
session = driver.session()

app = FastAPI()

@app.get("/related_competences/{course_name}") 
def search(course_name):
    q1=f"""
    MATCH (Course WHERE Course.name CONTAINS '{course_name}')-[:Annotate]—(Competence)
RETURN Course.name, Competence.name, Competence.uri 
    """
    results=session.run(q1)
    data=results.data()
    return(jsonable_encoder(data))

@app.get("/related_courses/{competence_name}") 
def search(competence_name):
    q1=f"""
    MATCH (Competence WHERE Competence.name CONTAINS '{competence_name}')-[:Annotate]—(Course)
RETURN Competence.name, Course.name, Course.descr
    """
    results=session.run(q1)
    data=results.data()
    return(jsonable_encoder(data))
     



