// config
## plugin: apoc 
## go to setting 
## dbms.security.procedures.unrestricted=apoc.*
## call apoc.help(‘meta’)

// apoc.import.file.enabled=true
// apoc.import.file.use_neo4j_config=true

// neo4j awt2022 bolt://localhost:7687

MATCH (n) DELETE n

LOAD CSV WITH HEADERS from "file:/toy_competence.csv" AS row 
MERGE (c:Competence {uri:row.conceptUri})
SET c.name = row.preferredLabel ;

CALL apoc.load.xml("toy_course.xml","/DEFTISCAT/COURSETRANSACTIONS/INSERTCOURSES/*") YIELD value AS cs
WITH cs,
[x IN cs._children WHERE x._type="CS_NAME" | x._text] as name,
[x IN cs._children WHERE x._type="CS_DESC_LONG" | x._text] as descr,
[x IN cs._children WHERE x._type="CS_ID" | x._text] as cid
MERGE (c:Course{cid:cid[0]})
SET c.name=name[0],
c.descr = descr[0] ;

// MATCH (n) RETURN n
