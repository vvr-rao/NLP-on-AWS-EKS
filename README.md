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

The modeling needs a bit more work(ref: NLPonEKS-ModelTraining.ipynb). I used a simple BOW model using Linear SVM. Planning to do more work to tune the model later but wanted a framework in place to host an ML model

One approach I am exploring to improve the model is to create Word2Vec vectors and training a model using that (ref: NLPonEKS-EDA-Word2Vec.ipynb). Unfortunately, the corpus might not be large enough for sufficient W2V training and my accuracy is proving to be lower than a simple BOW with CountVectorization and SVM (I could always download a pretained one from Google, Stanford etc.). Below is the 2D representation of my trained Word2Vec model using the corpus:
![Word2Vec](https://github.com/vvr-rao/NLP-on-AWS-EKS/blob/main/Notebooks/W2V.png?raw=true)

In any case, with the trained model, the steps to deploy are as follows;
1) Save the model in a .pkl, 
2) Create a Docker container holding the .pkl and a simple flask app to accept incoming text in a JSON and return the Sentiment
3) Publish on AWS EKS. For detail on how to publish a Flask App of EKS, take a look at my other repo here: https://github.com/vvr-rao/Flask-on-AWS-EKS

Model can be called from Postman by passing a POST message with a JSON body.
The expected input is of the form {"mytext":"<TEXT FOR WHICH SENTIMENT IS NEEDED>"}
  

