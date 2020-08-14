from flask import Flask, request, render_template
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect("localhost", "root", "", "oanda-service")

@app.route('/')
def getFibonacciValueData():
    # cur = db.cursor()
    cur2 = db.cursor()
    # cur.execute('SELECT * FROM fibonaccivalue')
    cur2.execute('SELECT r.robotorderid, r.orderid, r.apiTime, a.instrument FROM robotorder AS r INNER JOIN  activity AS a ON r.activityid = a.activityid')

    # fibonacciValueData = cur.fetchall()
    robotOrderData = cur2.fetchall()


    return render_template('index.html', robotorder=robotOrderData)



if __name__ == "__main__":
    app.run(debug=True)

    