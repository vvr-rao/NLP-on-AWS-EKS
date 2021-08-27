from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

@app.route("/", methods=['POST'])
def do_prediction():
  content = request.get_json()
  model = open('model/SVM_cv_model.pkl','rb')
  clf = joblib.load(model)
  data = [content['mytext']]
  new_data = []
  for string in data:
    string1 = string.replace('\d+', '') # remove digits
    string1 = string1.replace('[^\w\s]', '') # remove punctuation
    new_data.append(string1)
  my_prediction = clf.predict(data)
  my_prediction_str = ""
  if my_prediction[0] == 0:
    my_prediction_str = "Negative"
  elif my_prediction[0] == 1:
    my_prediction_str = "Somewhat Negative"
  elif my_prediction[0] == 2:
    my_prediction_str = "Neutral"
  elif my_prediction[0] == 3:
    my_prediction_str = "Somewhat Positive"
  elif my_prediction[0] == 4:
    my_prediction_str = "Positive"
  return (jsonify(my_prediction_str))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
