from flask import Flask, render_template, request, jsonify
from validation import validform
from views import groupby_maker, sales_per_month, sales_per_hour, member_vs_no_member, sales_per_hour_per_product_line
import pandas as pd
from random import randint



#chargement du dataset
df =  pd.read_csv('ss.csv')



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard',methods = ['POST', 'GET'])
def dashboard():
    data =  request.form
    
    #get admin email
    email =  data.get('email')

    #get password
    pwd =  data.get('pwd')

    #views
    data_un = groupby_maker("Branch", "Total",df)
    data_deux =  groupby_maker("Gender", "Total", df)
    data_trois =  sales_per_month(df)
    data_quatre = member_vs_no_member(df)
    data_cinq =  sales_per_hour(df)
    if validform(email = email, pwd_on_form= pwd):
        return render_template('chart.html', data_un=data_un, 
                               data_deux = data_deux, data_trois = data_trois, 
                               data_quatre =  data_quatre,
                               data_cinq = data_cinq)
    else:
        return 'No dashboard !'




### route pour les donnees du multiplelineChart -- qui seront recupere par une methode fetch json
@app.route('/mulChart_data')
def mulChart_data():
    data =  sales_per_hour_per_product_line(df)

    return jsonify(data)


### route pour les donnees concernant le radar -- qui seront recuperere par une methode fetch java script !
@app.route('/radar_data')
def radar_data():
    data =  member_vs_no_member(df)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug = True)
