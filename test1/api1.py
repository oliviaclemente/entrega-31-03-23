from flask import Flask, jsonify, request

app = Flask(__name__)

# Función para resolver el problema de la Torre de Hanoi
def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de la torre {origen} a la torre {destino}")
        return
    torre_hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} de la torre {origen} a la torre {destino}")
    torre_hanoi(n-1, auxiliar, destino, origen)

# Definición de la ruta /hanoi para la API
@app.route('/hanoi')
def hanoi():
    n = int(request.args.get('n', 3))  # Número de discos (por defecto: 3)
    origen = request.args.get('origen', 'A')  # Torre de origen (por defecto: A)
    destino = request.args.get('destino', 'C')  # Torre de destino (por defecto: C)
    auxiliar = request.args.get('auxiliar', 'B')  # Torre auxiliar (por defecto: B)
    resultado = []
    # Resolver el problema de la Torre de Hanoi y agregar cada movimiento al resultado
    def resolver_hanoi(n, origen, destino, auxiliar):
        if n == 1:
            resultado.append(f"Mover disco 1 de la torre {origen} a la torre {destino}")
            return
        resolver_hanoi(n-1, origen, auxiliar, destino)
        resultado.append(f"Mover disco {n} de la torre {origen} a la torre {destino}")
        resolver_hanoi(n-1, auxiliar, destino, origen)
    resolver_hanoi(n, origen, destino, auxiliar)
    return jsonify(resultado)  # Devolver el resultado como JSON

if __name__ == '__main__':
    app.run()
