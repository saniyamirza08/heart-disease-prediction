from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import mysql.connector as mc
conn = mc.connect(user='root', password='SaniyaMirza@23', host='localhost', database='heart')
import joblib
model = joblib.load("decisiontreeclassifier.lb")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('userdata.html') 

@app.route('/userdata', methods=['GET', 'POST'])
def userdata():
    if request.method == 'POST':
        
        age = int(request.form['age'])  
        sex = request.form['sex']  
        cp = request.form['cp']  
        trestbps = int(request.form['trestbps'])  
        chol = int(request.form['chol'])  
        fbs = request.form['fbs']  
        restecg = request.form['restecg']  
        thalach = int(request.form['thalach'])  
        exang = request.form['exang']  
        oldpeak = float(request.form['oldpeak'])  
        slope = request.form['slope']  
        ca = request.form['ca']  
        thal = request.form['thal']  

        unseen_data = [[sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, age]]

        output = model.predict(unseen_data)[0]

        
        query = """INSERT INTO heartdata(sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, age, predicted)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        mycursor = conn.cursor()
        details = (sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, age, int(output))

        mycursor.execute(query, details)
        conn.commit()

        mycursor.close()

        if output == 0:
            return f"Patient doesn't have heart disease."
        else:
            return f"Patient has heart disease."

@app.route('/history')
def history():
    
    conn = mc.connect(user="root", host="localhost", password="SaniyaMirza@23", database='heart')
    mycursor = conn.cursor()
    query = "SELECT * FROM heartdata"  
    mycursor.execute(query)
    data = mycursor.fetchall()

    mycursor.close()
    conn.close()

    return render_template('history.html', userdetails=data)

if __name__ == "__main__":
    app.run(debug=True)
