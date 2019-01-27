import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle
import model as md

app = Flask(__name__)
model = pickle.load(open('billboards_model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(data['inputs'])
    prediction = md.predict(np.array(data['inputs']))
    num = prediction
    print(num)

    csv_data = pd.read_csv("Data-Part1.csv")
    # csv_data = data.dropna()

    data_labels = pd.DataFrame(model.labels_)

    data_total = pd.concat([data_labels, csv_data], axis=1)

    is_val = data_total[0]==num
    data_total_fin = data_total[is_val]
    return jsonify({'result':data_total_fin['Intersection'].values[0]})
    # return jsonify({'result':'BLOOR ST E and TED ROGERS WAY'})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
