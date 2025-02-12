from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Hello, World! -- nuevo</h1>" # siempre se debe de regresar algo
    titulo = 'IDGS801'
    lista = ['joel', 'briones', 'hola']
    
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

@app.route('/hola')
def hola():
    return "<h1>Hola, mundo_2!</h1>"

@app.route('/user/<string:usuario>') # tipodato/ variable
def user(usuario):
    return f"Hola, {usuario}!"

app.route('/numero/<int:n>')
def numero(n):
    return f"El número es: {n}"

@app.route('/user/<int:id>/<string:username>')
def userName(id, usename):
    return f"El id es: {id} y el username es: {usename}"

@app.route('/suma/<float:n1>/<float:n2>')
@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route('/default')
@app.route('/default/<string:parm>')
def default(parm = 'joel'):
    return f"El parámetro es: {parm}"

@app.route('/operas')
def operas():
    return '''
     <form action="">
        <label for="txtNombre">Nombre</label>
        <input type="text" id="txtNombre">b
        <label for="txtPass">Pass</label>
        <input type="text" id="txtPass">
    </form>
    '''


if __name__ == '__main__':
        app.run(debug=True, port=8080)
