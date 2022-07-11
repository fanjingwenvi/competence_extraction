plugin: apoc
call apoc.help("meta")

dbms.security.procedures.unrestricted=apoc.*
apoc.import.file.enabled=true

CALL dbms.listPools()
dbms.memory.heap.initial_size=2G
dbms.memory.heap.max_size=4G
dbms.memory.pagecache.size=2G

// neo4j awt2022 bolt://localhost:7687
// MATCH (n) RETURN n

MATCH (n) DELETE n

LOAD CSV WITH HEADERS from "file:/toy_competence.csv" AS row 
MERGE (c:Competence {uri:row.conceptUri})
SET c.name = row.preferredLabel ;

CALL apoc.load.xml("CompetencyExtraction_utf.xml","/DEFTISCAT/COURSETRANSACTIONS/INSERTCOURSES/*") YIELD value AS cs
// WITH cs LIMIT 10
WITH cs,
[x IN cs._children WHERE x._type="CS_NAME" | x._text] as name,
[x IN cs._children WHERE x._type="CS_DESC_LONG" | x._text] as descr,
[x IN cs._children WHERE x._type="CS_ID" | x._text] as cid
MERGE (c:Course{cid:cid[0]})
SET c.name=name[0],
c.descr = descr[0];








