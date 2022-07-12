# Competence Extraction With Machine Learning / Natural Language Processing 

### Situation 
In the field of Technology Enhanced Learning (TEL) Data-models / metadata exist for several types like Courses (Course-descriptions, Course-structures), User-profiles and Competencies, just to name some of them. In this project we'll have our scope on Course-descriptions, and you'll focus on Specifications / data-models for Course-description which don't have the properties for Competencies covered by this Course - but it is necessary to know which competencies are covered by which course and vice versa. The goal is to extract competencies from these textual descriptions / Data-models. For the Competencies you'll work with the Framework EU-ESCO (European Skills, Competencies and Occupation) and for the Course-description you'll get Samples following the Specifications DIN PAS1045 (including DEfTIS), the WDBB (Weiterbildungsdatenbank Berlin Brandenburg) fork of DEfTIS and its extensions, and also KursNet (based on open-Qcat). For the Extraction of Competencies you'll need expertise or passion towards working with Machine Learning approaches in the field of Natural Language Processing (NLP)<br>

### Task and Reaction 
Create a Service which extracts Competencies from Course-descriptions<br>
Spacy, Tensorflow<br> 
demo: preprocessing_with_mathing.ipynb<br> 
demo: named_entity_recognition.ipynb<br> 
solution: similarity_analysis.ipynb<br>
<br>
Setup a Graph database storing Course-descriptions and Competencies, Create the Relation (Path) in the Graph database between the Course-description and each of the extracted Competency<br>
Neo4j<br> 
<br>
Create a RESTful API to get all Competencies covered by a Course (Course-description ID) or query/filter Course (Course-descriptions) by Competenc(y/ies)<br>
Fast API<br> 

### Result 
Evaluation of the Model<br> 
Docker Deployment<br> 




