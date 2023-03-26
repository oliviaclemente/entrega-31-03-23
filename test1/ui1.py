class UI:
    def __init__(self):
        pass
    
    def mostrar_mensaje(self, mensaje):
        print(mensaje)
    
    def mostrar_error(self, error):
        print(f"Error: {error}")
    
    def obtener_input(self, mensaje):
        return input(mensaje)
    
    def limpiar_pantalla(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
