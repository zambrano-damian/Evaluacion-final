from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para el ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Recibiendo datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        # Configuración de precios
        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        # Lógica para determinar el descuento
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15  # 15% de descuento
        elif edad > 30:
            descuento = total_sin_descuento * 0.25  # 25% de descuento
        else:
            descuento = 0  # Sin descuento

        # Total con el descuento aplicado
        total_con_descuento = total_sin_descuento - descuento

        # Renderizar plantilla con las variables
        return render_template(
            'resultado1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento
        )
    return render_template('ejercicio1.html')

# Ruta para el ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # Diccionario de usuarios y contraseñas
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if request.method == 'POST':
        # Recibiendo datos del formulario
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # Lógica de validación
        if nombre in usuarios and usuarios[nombre] == contrasena:
            if nombre == 'juan':
                mensaje = f"Bienvenido administrador {nombre}"
            else:
                mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        # Renderizar plantilla con el mensaje
        return render_template('resultado2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)