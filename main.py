from flask import request, make_response, redirect, render_template, session, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms.fields import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()
# app = Flask(__name__)
# bootstrap = Bootstrap(app) #Inicializamos bootstrap

# app.config['SECRET_KEY'] = 'SUPER SECRET' #Estos nos ayuda a generar una sesion en flask

todos = ['Comprar Café', 'Enviar Solicitudes de Comrpa', 'Entregar video al productor']

# class LoginForm(FlaskForm):
#     username = StringField('Nombre de Usuario', validators=())
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Enviar')
    
@app.cli.command()
def test():
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(test)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)
    
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect(url_for('hello')))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    Login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': Login_form,
        'username': username
    }

    if Login_form.validate_on_submit():
        username = Login_form.username.data
        session['username'] = username
        
        flash('Nombre de usuario registrado con éxito!!!')

        return redirect(url_for('index'))

    #return 'Mario Roberto, tu IP es {}'.format(user_ip)
    return render_template('hello.html', **context)


# Comentario general:
# Este programa utiliza Flask, un marco de desarrollo web para Python, para crear una aplicación web simple.
# La ruta principal ('/') redirige al usuario a la ruta '/hello' y almacena su IP en una cookie llamada 'user_ip'.
# La ruta '/hello' recupera la IP almacenada en la cookie y muestra un saludo personalizado.
# El programa utiliza las bibliotecas request, make_response y redirect de Flask para manejar la solicitud y respuesta HTTP.
