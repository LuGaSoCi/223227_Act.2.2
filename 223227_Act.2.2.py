import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape):
        self.tape = tape

    def parse_and_sum(self):
        results = []  # Lista para almacenar los resultados de cada suma
        tapes = self.tape.split(';')  # Dividir las entradas por el delimitador ';'

        for tape in tapes:
            tape = tape.strip()  # Eliminar espacios en blanco alrededor
            # Validar que la cadena comienza con '10'
            if not tape.startswith('10'):
                results.append(f"Error: La cadena '{tape}' debe comenzar con '10'.")
                continue
            
            # Validar que la cadena termina con '='
            if not tape.endswith('='):
                results.append(f"Error: La cadena '{tape}' debe terminar con '='.")
                continue
            
            base_binary = '10' 
            base_value = int(base_binary, 2)

            # Obtener la parte de la cadena después de '10' y quitar el '='
            rest_of_tape = tape[2:-1]  # eliminar '=' al final
            binary_numbers = rest_of_tape.split('=')

            # Validar que haya al menos un número binario después de '10'
            if not rest_of_tape or len(binary_numbers) == 0:
                results.append(f"Error: La cadena '{tape}' debe contener al menos un número binario después del '10'.")
                continue

            total_sum = base_value
            for num in binary_numbers:
                if num: 
                    total_sum += int(num, 2)

            binary_result = bin(total_sum)[2:]
            results.append(f"Resultado para '{tape}': {binary_result}")

        return results

def check_string():
    input_string = entry.get()

    tm = TuringMachine(input_string)

    results = tm.parse_and_sum()

    # Mostrar resultados en un único mensaje
    messagebox.showinfo("Resultados", "\n".join(results))

def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f'{width}x{height}+{x}+{y}')

# Crear ventana principal
root = tk.Tk()
root.title("Máquina de Turing - Suma de Binarios")

# Definir el tamaño de la ventana
window_width = 400
window_height = 300
center_window(window_width, window_height)

# Etiqueta
label = tk.Label(root, text="Introduce cadenas binarias (separadas por ';'):\n(debe comenzar con '10' y terminar con '='):")
label.pack(pady=10)

# Campo de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Botón de verificación
check_button = tk.Button(root, text="Calcular Sumas", command=check_string)
check_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
