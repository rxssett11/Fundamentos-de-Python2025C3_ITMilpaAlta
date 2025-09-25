"""
ROSETE ZEPEDA ISMAEL 

CALCULADORA POO

"""



import sys

class Calculadora:
    def __init__(self):
        
        #Inicializa la calculadora con un historial de operaciones vacío.
        
        self.historial = []

    def _validar_expresion(self, expresion):
        
        #Método privado para validar si una expresión es válida.
        #Devuelve un mensaje de error o None si es válida.
        
        elementos = expresion.split()
        if len(elementos) != 3:
            return "Error: La expresión debe tener el formato 'numero operador numero' (ej. '5 + 3')."
        
        try:
            float(elementos[0])
            float(elementos[2])
            if elementos[1] not in ['+', '-', '*', '/']:
                return "Error: Operador no válido. Los operadores permitidos son '+', '-', '*', '/'."
        except ValueError:
            return "Error: Los operandos deben ser números."
            
        return None

    def _realizar_operacion(self, num1, operador, num2):
        """
        Método privado para realizar la operación matemática.
        """
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return "Error: División por cero."
            return num1 / num2
    
    def procesar_comando(self, comando):
        """
        Procesa comandos especiales como 'salir' o 'historial'.
        """
        comando = comando.lower()
        if comando == 'salir':
            print("Saliendo de la calculadora. ¡Hasta la próxima!")
            sys.exit(0)
        elif comando == 'historial':
            self.mostrar_historial()
            return True
        elif comando == 'ayuda':
            print("Comandos disponibles:")
            print("  - Escribe una expresión matemática (ej. '5 + 3')")
            print("  - 'historial' para ver las operaciones anteriores")
            print("  - 'salir' para cerrar la calculadora")
            return True
        return False

    def procesar_expresion(self, expresion):
        """
        Procesa una expresión matemática, realiza el cálculo y lo guarda en el historial.
        """
        error = self._validar_expresion(expresion)
        if error:
            print(error)
            return
            
        elementos = expresion.split()
        num1 = float(elementos[0])
        operador = elementos[1]
        num2 = float(elementos[2])

        resultado = self._realizar_operacion(num1, operador, num2)

        if isinstance(resultado, (float, int)):
            operacion_str = f"{num1} {operador} {num2} = {resultado}"
            print(f"Resultado: {resultado}")
            self.historial.append(operacion_str)
        else:
            print(resultado) # Muestra el error de división por cero

    def mostrar_historial(self):
        """
        Muestra todas las operaciones guardadas en el historial.
        """
        if not self.historial:
            print("El historial está vacío.")
        else:
            print("--- Historial de Operaciones ---")
            for i, operacion in enumerate(self.historial, 1):
                print(f"{i}. {operacion}")
            print("-------------------------------")

def main():
    """
    Función principal que ejecuta el bucle de la calculadora.
    """
    calculadora = Calculadora()
    print("¡Bienvenido a la Calculadora Básica!")
    print("Escribe una expresión (ej. '5 + 3') o 'ayuda' para ver los comandos.")

    while True:
        try:
            entrada = input("\n> ")
            if not entrada:
                continue

            if not calculadora.procesar_comando(entrada):
                calculadora.procesar_expresion(entrada)
        
        except KeyboardInterrupt:
            print("\nSaliendo de la calculadora.")
            sys.exit(0)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
