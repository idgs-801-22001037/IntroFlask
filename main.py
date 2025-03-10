from flask import Flask, render_template, request
import os
import datetime
from model.Persona import Persona
from flask import g
from flask import flash
import forms
from flask_wtf.csrf import CSRFProtect
import forms_zodiaco


app = Flask(__name__)
app.secret_key='esta es una clave secreta'
csrf  = CSRFProtect()

@app.route('/')
def index():
    #return "<h1>Hello, World! -- nuevo</h1>" # siempre se debe de regresar algo
    titulo = 'IDGS801'
    lista = ['joel', f'{g.user}', 'hola']
    print(f'{g.user}')
    return render_template('index.html', titulo=titulo, lista=lista)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.before_request
def before_request():
    g.user = 'mario'
    print('before request')

@app.after_request
def after_request(response):
    print('after request')
    return response

@app.route('/operacion')
def operacion():
    
    return render_template('OperasBas.html')

@app.route('/resultado', methods=['POST'])
@csrf.exempt
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    n1 = int(n1)
    n2 = int(n2)
    opcion = request.form.get('operacion')
    resultado = int
    if opcion == 'suma':
        resultado = n1 + n2
    if opcion == 'resta':
        resultado = n1 - n2
    if opcion == 'multi':
        resultado = n1 * n2
    if opcion == 'divi':
        resultado = n1 / n2
    os.system('cls')
    print(operacion)
    return render_template('OperasBas.html', operacion=opcion, resultado=resultado)


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
    
# ---------------------------------------------------------------------------------------
    
@app.route('/cineView')
def cineView():
    return render_template('CineView.html')


@app.route('/cineControl', methods=['POST'])
@csrf.exempt
def cineControl():
    os.system('cls')  

    boton = request.form.get('accion')
    nombre = request.form.get('txtNombre')
    personas = request.form.get('txtCantidadPersonas')
    personas = int(personas)
    personas = int(personas)
    boletos = request.form.get('txtCantidad')
    boletos = int(boletos)
    persona = Persona()
    persona.crearPersona(nombre,personas, boletos)
    if boton == 'procesar':

        tarjeta = request.form.get('txtTarjeta')
        if persona.verificarDatos():
            if persona.verificar():
                
                mensaje = persona.calcularPrecio(personas,boletos)
                totalLocal = persona.descuento()
                if tarjeta == '1':
                    salida = persona.tarjetaDescuento(totalLocal)
                else:
                    salida = totalLocal
                
                return render_template('CineView.html', nombre=nombre,personas=0, boletos=0, mensaje=salida )
            else:
                mensaje = 'Solo 7 por persona'
                return render_template('CineView.html', nombre=nombre,personas=personas, boletos=boletos, mensaje=mensaje)
        else:
            mensaje = 'valores incorrectos'
            return render_template('CineView.html', nombre=nombre,personas=personas, boletos=boletos, mensaje=mensaje)
        
    

@app.route('/zodiaco', methods=['GET', 'POST'])
def zodiaco():
    form = forms_zodiaco.zodiacoForm(request.form)
    
    if form.validate_on_submit():  # Esta función valida el CSRF token también
        nombre = form.nombre.data
        apellido = form.apellido.data
        apellidoM = form.apellidoM.data
        anio = form.anio.data
        dia = form.dia.data
        mes = form.mes.data

        fecha_actual = datetime.datetime.now()
        anio_actual = fecha_actual.year
        edad = anio_actual - anio

        lista_zodiaco = [
            "rata", "buey", "tigre", "conejo", "dragon", "serpiente",
            "caballo", "cabra", "mono", "gallo", "perro", "cerdo"
        ]
        signo = lista_zodiaco[(anio - 4) % 12]

        return render_template('zodiaco.html',form=form, nombre=nombre, apellido=apellido, apellidoM=apellidoM, edad=edad, signo=signo)
    
    return render_template('zodiaco.html', form=form)

    
    """boton = request.form.get('accion')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    appelidoM = request.form.get('apellidoM')
    anio = request.form.get('anio')
    anio = int(anio)
    dia = request.form.get('dia')
    dia = int(dia)
    mes = request.form.get('mes')
    mes = int(mes)
    
    fecha_actual = datetime.datetime.now()
    anioActual = fecha_actual.year
    anioActual = int(anioActual)
    
    edad = anioActual - anio
        
    
    if boton == 'accionar':
        os.system('cls')
        print('correcto')
        signo = (anio - 4) % 12
    return render_template('zodiaco.html', nombre=nombre, apellido=apellido, appelidoM=appelidoM, edad=edad, signo=listaZignos[signo])"""




"""_________________________"""
@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    
    mat=''
    nom=''
    ape=''
    correo=''
    
    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        correo = alumno_clas.correo.data
        
        mensaje = 'Bienvenido {}'.format(nom)
        flash(message=mensaje)
        
    return render_template('Alumnos.html', form=alumno_clas,mat=mat, nom=nom, ape=ape, correo=correo)




if __name__ == '__main__':
        csrf .init_app(app)
        app.run(debug=True, port=8080)
