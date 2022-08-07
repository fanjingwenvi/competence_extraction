# !pip3 install neo4j==4.4.5

import time
from neo4j import GraphDatabase
import csv

### create nodes

%%time
with open("data/connector.txt") as con:
    data = csv.reader(con, delimiter = ",")
    for i in data:
        user = i[0]
        pwd = i[1]
        uri = i[2]


driver = GraphDatabase.driver(uri=uri, auth=(user,pwd))


session = driver.session()



clear_all_nodes = """
MATCH (n) DELETE n;
"""

clear_all = """
MATCH (n) DETACH DELETE n;
"""

# WITH cs LIMIT 10
import_descriptions = """
CALL apoc.load.xml("course_description_FOKUS.xml","/DEFTISCAT/COURSETRANSACTIONS/INSERTCOURSES/*") YIELD value AS cs
WITH cs,
[x IN cs._children WHERE x._type="CS_NAME" | x._text] as name,
[x IN cs._children WHERE x._type="CS_DESC_LONG" | x._text] as desc,
[x IN cs._children WHERE x._type="CS_ID" | x._text] as cid
MERGE (c:Course{cid:cid[0]})
SET c.name=name[0],
c.description = desc[0];
"""


import_competency = """
USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS from "file:/skills_de.csv" AS row 
MERGE (c:Competency {uri:row.conceptUri})
SET c.name = row.preferredLabel;
"""


session.run(clear_all)
session.run(import_competency)
session.run(import_descriptions)


### create relationships

clear_all_relations = """
MATCH ()-[r]-() DELETE r;
"""

session.run(clear_all_relations)

for i in range(1,29): # with all relation-data in 28 csv-files
    import_relation = """
    USING PERIODIC COMMIT 500
    LOAD CSV WITH HEADERS from "file:/relations/relations_part_""" + str(i) + """.csv" AS row
    MATCH (course:Course {cid:row.course_id})
    MERGE (competency:Competency {uri: row.conceptUri})
    MERGE (course)-[r:RELATED_TO]-(competency);
    """
    session.run(import_relation)




