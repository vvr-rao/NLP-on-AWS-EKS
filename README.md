# Training an NLP model and Deploying onto AWS Elastic Kubernetes Service

Trained a model locally and deploying on to Elastic Kubernetes Service on AWS

The Notebooks folder has the EDA and Model training. For EDA, I primarily focussed on using the **en_core_web_lg model** of Spacy to extract Named Entities, Adjectives and Verbs. Was looking for any trends

The modeliing needs a bit more work. I used a simple BOW model using Linear SVM. Planning to do more work to tune the model later but wanted a framework in place to host an ML model

From there, saved the model, created a Docker container and published on AWS EKS. 

Model can be called from Postman by passing a POST message with a JSON body.
The expected input is of the form {"mytext":"<TEXT FOR WHICH SENTIMENT IS NEEDED>"}
