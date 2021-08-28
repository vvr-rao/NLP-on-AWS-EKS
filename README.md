# Training an NLP model and Deploying onto AWS Elastic Kubernetes Service

Trained a model locally and deployed  to the Elastic Kubernetes Service on AWS. The data was from Kaggle: https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/overview.
This is a Sentiment Dataset for Movie reviews. Five Sentiment Labels as follows:
0 - negative
1 - somewhat negative
2 - neutral
3 - somewhat positive
4 - positive

The Notebooks folder has the EDA and Model training. For EDA, I primarily focussed on using the **en_core_web_lg model** of Spacy to extract Named Entities, Adjectives and Verbs. Was looking for any trends. Below is an Example of the Persons in the corpus arranged by Sentiment Label
![Persons by Sentiment](https://github.com/vvr-rao/NLP-on-AWS-EKS/blob/main/Notebooks/Persons.png?raw=true)

The modeliing needs a bit more work. I used a simple BOW model using Linear SVM. Planning to do more work to tune the model later but wanted a framework in place to host an ML model

From there I;
1) Saved the model in a .pkl, 
2) Created a Docker container holding the .pkl and a simple flask app to accept incoming text in a JSON and return the Sentiment
3) Published on AWS EKS. For detail on how to publish a Flask App of EKS, take a look at my other repo here: https://github.com/vvr-rao/Flask-on-AWS-EKS

Model can be called from Postman by passing a POST message with a JSON body.
The expected input is of the form {"mytext":"<TEXT FOR WHICH SENTIMENT IS NEEDED>"}
  

