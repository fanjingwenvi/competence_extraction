from flask import Flask,request,render_template,redirect
# from flask_restful import Resource, Api

from neo4j import GraphDatabase

from dotenv import load_dotenv, find_dotenv
import os 
import ast

app = Flask(__name__)
## api = Api(app)

## find the environment variable 
load_dotenv(find_dotenv())

def env(key, default=None, required=True):
    """
    Retrieves environment variables and returns Python natives. The (optional)
    default will be returned if the environment variable does not exist.
    """
    try:
        value = os.environ[key]
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value
    except KeyError:
        if default or not required:
            return default
        raise RuntimeError("Missing required environment variable '%s'" % key)

## app.config['SECRET_KEY'] = env('SECRET_KEY')

DATABASE_USERNAME = env('DATABASE_USERNAME')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_URL = env('DATABASE_URL')

print(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_URL)

driver = GraphDatabase.driver(uri=DATABASE_URL, auth=(DATABASE_USERNAME, DATABASE_PASSWORD))
session = driver.session()

@app.route("/display",methods=["GET","POST"])
def display_node():
    q1="""
    match (n) return n
    """
    results=session.run(q1)
    data=results.data()
    return(jsonify(data))

if __name__=='__main__':
    app.run(port=5000)