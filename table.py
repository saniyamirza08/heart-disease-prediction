import mysql.connector as mc

conn = mc.connect(user='root', password='SaniyaMirza@23', host='localhost', database='heart')

if conn.is_connected():
    print("You are connected.")
else:
    print('Unable to connect.')

mycursor = conn.cursor()


query =""" CREATE TABLE heartdata(
    sex VARCHAR(50),
    cp VARCHAR(50),
    trestbps INT,
    chol INT,
    fbs VARCHAR(50),
    restecg VARCHAR(50),
    thalach INT,
    exang VARCHAR(50),
    oldpeak FLOAT,
    slope VARCHAR(50),
    ca VARCHAR(50),
    thal VARCHAR(50),
    age INT,
    predicted INT
)"""


mycursor.execute(query)
print('Your table is created.')

mycursor.close()
conn.close()
