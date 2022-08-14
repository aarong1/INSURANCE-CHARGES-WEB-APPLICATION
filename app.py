import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'registry': 'Registry'}, {'registry': 'vcs'}, {'registry': 'gsr'}],
        data1=[{'vintage': 'Vintage'}, {'vintage': 0}, {'vintage': 1}, {'vintage': 2}, {'vintage': 3}, {'vintage': 4}, {'vintage': 5}],
        data2=[{'sector': 'Sector'}, {'sector': 'Forestry'}, {'sector': 'Household'}],
        data3=[{'country': "Brazil"}, {'country': "Peru"}, {'country': "Indonesia"},
               {'country': 'United States'}, {'country': "China"}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    if int(input_data[0]) & int(input_data[3]) & input_data[2].isdigit() == True:
        pass
    else:
        print(ValueError)

    if input_data[1] == 'vcs':
        input_data[1] = 0
    elif input_data[1] == 'gsr':
        input_data[1] = 1
    else:
        print(ValueError)

    if input_data[4] == 'no':
        input_data[4] = 0
    elif input_data[4] == 'yes':
        input_data[4] = 1
    else:
        print(ValueError)

    if input_data[5] == 'Brazil':
        input_data[5] = 0
    elif input_data[5] == 'Peru':
        input_data[5] = 1
    elif input_data[5] == 'United States':
        input_data[5] = 2
    elif input_data[5] == 'China':
        input_data[5] = 3
    else:
        print(ValueError)



    output = input_data[5]
    return render_template('index.html', prediction_text=" The predicted insurance charges is {}".format(output),
                           data=[{'registry': 'Registry'}, {'registry': 'vcs'}, {'registry': 'gsr'}],
        data1=[{'vintage': 'Vintage'}, {'vintage': 0}, {'vintage': 1}, {'vintage': 2}, {'vintage': 3}, {'vintage': 4}, {'vintage': 5}],
        data2=[{'sector': 'Sector'}, {'sector': 'Forestry'}, {'sector': 'Household'}],
        data3=[{'country': "Brazil"}, {'country': "Peru"}, {'country': "Indonesia"},
               {'country': 'United States'}, {'country': "China"}])

if __name__ == '__main__':
    app.run(debug=True)
