from flask import Flask, render_template, url_for, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    print(np.version.version)
    print(pickle.format_version)
    features = [[x] for x in request.form.values()]
    # final_features = [np.array(features)]
    col_names =  ['movement_reactions', 'mentality_composure', 'passing', 
      'potential', 'dribbling', 'wage_eur', 'power_shot_power', 'value_eur', 'lcm', 'rcm', 'cm', 'release_clause_eur', 
      'mentality_vision', 'attacking_short_passing']
    ##col_names = np.array(['movement_reactions', 'mentality_composure', 'passing', 'potential', 'dribbling', 'wage_eur', 'power_shot_power', 'value_eur'])
    mapping = dict(zip(col_names, features))
    print(mapping)
    df_X = pd.DataFrame(data=mapping)
    print(df_X)
    prediction = model.predict(df_X)
    predicted_value = round(prediction[0], 2)
    return render_template("index.html", prediction_text="Player rating is {}".format(predicted_value))

if __name__ == "main":
    app.run(debug=True)