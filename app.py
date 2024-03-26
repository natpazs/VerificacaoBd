from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import mysql.connector 

# email: usuario1@email
#senha: 1234

app = Flask(__name__)

conexao = mysql.connector.connect(
    host = "127.0.0.1", 
    user = "root",
    password ="",
    database = "usuarios"
)
       
@app.route("/")
def login():  
    return render_template("login.html")

@app.route("/pag2")
def pag2():  
    return render_template("pag.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form["inputEmail"]
        senha = request.form["inputPassword"]

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email = %s and senha = %s",(email, senha))
        user = cursor.fetchall()

        if user:
            cursor.close()
            conexao.close()
            return redirect(url_for('pag2'))
        else:
            return render_template('login.html', show_alert=True, alert="Usuário ou senha incorretos!")
    else:
        return render_template('login.html', show_alert=True, alert="Usuário ou senha incorretos!")



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")