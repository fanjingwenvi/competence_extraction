## 1. Intro 

### nlp service:
extracts Competencies from Course-description
output Relationship(Path) between the Course-description and each of the extracted Competency

### graph database local setup 
Setup a graph database on local desktop 

### graph database driver service 
import Course-descriptions and Competencies in the graph database
import Relationship(Path) in the graph database

### graph database cloud setup 
push the local graph database with data to cloud 

### rest api service: 
get all Competencies covered by a Course, the list of competencies will be either in ESCO or W3C Verifiable Credentials (VC) dataformat.
query/filter Course (Course-descriptions) by Competenc(y/ies)


## 2. Folder Structure 
bash 
```
competency_extraction
│
└───rest_api 
│   │───main.py
│   │───.env 
│   │───requirements.txt
│───nlp_service.ipynb
│───graph_database_driver.ipynb 
└───data 
│   │───connector.txt
│   │───skills_de.csv
│   │───course_description_FOKUS.xml 
│   │───ccourse_description_testset.xml
│───requirements.txt
│───LICENSE
│───README.md
```

## 3. MAIN PROGRAM: Run rest api service with cloud graph databse 

run the following command to open the rest_api service sub folder, create the virtual environment, install dependencies, start FastAPI webserver.<br>
```bash
cd competency_extraction/rest_api

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

hypercorn main:app
```

click the folloing link to see documentation of the FastAPI<br>
<http://127.0.0.1:8000/docs><br>

For security resaon, the neo4j databae environment variables are stored in the .env file. They are connected to the neo4j cloud neo4j databae by default. They can be changed as following to connect to local desktop neo4j databae. <br>

```
DATABASE_USERNAME="neo4j"
DATABASE_PASSWORD="awt2022"
DATABASE_URL="bolt://localhost:7687"
```

## 4. Run nlp service 

run the following command to open the main folder, create the virtual environment, install dependencies, create ipykernel with name=awt2022, 
start jupyter notebook.<br>
```bash
cd competency_extraction

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 -m ipykernel install --user --name=awt2022

jupyter notebook

```
<br>

open nlp_service.ipynb file, choose the kernel awt2022 on jupyter notebook, and run <br>

## 5. Setup graph database local desktop 

open neo4j desktop, add new Project, add local Graph DBMS, set Password = awt2022, start local Graph DBMS, install APOC plugin<br>

put the following variables on the end of the neo4j Graph DBMS seetings file to unrestricte APOC plugin, enable file import function, and expand dbms memory<br>
```
dbms.security.procedures.unrestricted=apoc.*
apoc.import.file.enabled=true

dbms.memory.heap.initial_size=2G
dbms.memory.heap.max_size=4G
dbms.memory.pagecache.size=2G
```
<br>

put the the output relations folder, skills_de.csv file, course_description_FOKUS.xml file on the neo4j desktop Open folder - Import to prepare for importing <br>

## 6. Run graph database driver service 

same venv as 4. Run nlp service<br>

open  graph_database_driver.ipynb , choose the kernel awt2022 on jupyter notebook, and run <br>


## 7. Setup graph database cloud service  

get the dump file from neo4j local Graph DBMS<br>

install neo4j on local machine, for mac, it is<br>
```bash
brew install neo4j
```

push the neo4j dump file to the neo4j cloud<br>
```bash
/usr/local/opt/neo4j/bin/neo4j-admin push-to-cloud  --bolt-uri=bolt-uri  --dump=dump-file-path --username=neo4j  --password=password --overwrite=true 
```

