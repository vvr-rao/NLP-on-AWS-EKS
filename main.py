from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
  json = request.get_json()
  model = open('model/SVM_cv_model.pkl','rb')
  clf = joblib.load(model)
  data = ["plenty of funny quotes but ultimately fell flat"]
  new_data = []
  for string in data:
    string1 = string.replace('\d+', '') # remove digits
    string1 = string1.replace('[^\w\s]', '') # remove punctuation
    new_data.append(string1)
  my_prediction = clf.predict(data)
  return jsonify(my_prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
