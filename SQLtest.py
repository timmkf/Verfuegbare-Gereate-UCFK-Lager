from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'User'
app.config['MYSQL_PASSWORD'] = '47114711'
app.config['MYSQL_DB'] = 'belegarbeit'
mysql = MySQL(app)


@app.route('/')
def index():
    # Render the HTML page
    return render_template('index.html')



@app.route('/verfügbareGeräte', methods=['GET'])
def verfügbare_Geräte():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT Bezeichnung, Produktgruppe FROM geraet WHERE G_id NOT IN( SELECT mietvertrag.G_id FROM mietvertrag LEFT JOIN geraet ON mietvertrag.G_id = geraet.G_id WHERE mietvertrag.Status = 0 OR geraet.Zustand != "Gut");''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


    