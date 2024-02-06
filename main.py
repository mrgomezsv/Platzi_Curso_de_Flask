from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    #return 'Mario Roberto, tu IP es {}'.format(user_ip)
    return render_template('hello.html', **context)


# Comentario general:
# Este programa utiliza Flask, un marco de desarrollo web para Python, para crear una aplicación web simple.
# La ruta principal ('/') redirige al usuario a la ruta '/hello' y almacena su IP en una cookie llamada 'user_ip'.
# La ruta '/hello' recupera la IP almacenada en la cookie y muestra un saludo personalizado.
# El programa utiliza las bibliotecas request, make_response y redirect de Flask para manejar la solicitud y respuesta HTTP.
