import tkinter as tk
import socket

HOST = 'localhost'  # O servidor estará executando na mesma máquina
PORT = 65432  # A mesma porta do servidor
TOKEN = "meu_token_secreto"  # Substitua isso pelo seu token válido

s = None  # Inicialmente, nenhuma conexão está aberta
autonomous = True


def send_message(command):
    global s
    if not autonomous and s:
        s.sendall(f"{command}".encode())  # Envia a mensagem para o servidor


def send_message_pressed(command):
    global s
    if not autonomous and s:
        s.sendall(f"{command}".encode())  # Envia a mensagem para o servidor


def send_message_released(command):
    global s
    if autonomous and s:
        s.sendall(f"{command}-desativado".encode())  # Envia a mensagem para o servidor


def toggle_autonomous():
    global autonomous, s
    # print(autonomous)
    if not autonomous:
        send_message("quit")
        print('Desconectado do servidor.')
        s = None
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(f"TOKEN {TOKEN}".encode())  # Envia o token para o servidor
        response = s.recv(1024).decode()  # Recebe a resposta do servidor
        if response == "VALID":
            print("Token válido. Conexão estabelecida.")
            status_conexao = 'Conexão estabelecida.'
            status_fg = 'green'
        else:
            print("Token inválido. Conexão não estabelecida.")
            status_conexao = 'Conexão não estabelecida.'
            status_fg = 'red'
            s = None

    autonomous = not autonomous
    if autonomous:
        button_autonomous.config(text="Autônomo", bg="#ffa0a0")
        label_status.grid_remove()
    else:
        button_autonomous.config(text="Manual", bg="#a0ffa0")
        update_label_status(status_conexao, status_fg)
        label_status.grid()
        
        
        


root = tk.Tk()
root.title("Controle Virtual")

# Estilos
button_style = {'font': ('Arial', 12), 'width': 10, 'height': 2, 'bg': '#f0f0f0', 'activebackground': '#c0c0c0'}

# Frame principal
frame = tk.Frame(root, bg="#d9d9d9")
frame.pack(pady=20)

# Etiqueta de status da conexão
label_status = tk.Label(frame, text='', fg="red")
label_status.grid(row=0, column=1, pady=10)
label_status.grid_remove()

def update_label_status(new_text, color):
    label_status.config(text=new_text, fg=color)

# Botões de controle
button_up = tk.Button(frame, text="▲", command=lambda: (send_message_pressed("up")), **button_style)
button_up.grid(row=1, column=1)

button_left = tk.Button(frame, text="◀", command=lambda: (send_message_pressed("left")), **button_style)
button_left.grid(row=2, column=0)

button_stop = tk.Button(frame, text="⏸", command=lambda: (send_message_pressed("stop")), **button_style)
button_stop.grid(row=2, column=1)

button_right = tk.Button(frame, text="▶ ", command=lambda: (send_message_pressed("right")), **button_style)
button_right.grid(row=2, column=2)

button_down = tk.Button(frame, text="▼", command=lambda: (send_message_pressed("down")), **button_style)
button_down.grid(row=3, column=1)

# Botão de alternância entre autônomo e manual
button_autonomous = tk.Button(root, text="Autônomo", command=toggle_autonomous, **button_style)
button_autonomous.config(bg="#ffa0a0")
button_autonomous.pack(pady=10)

root.mainloop()

if s:
    send_message("quit")
    print('Desconectado do servidor.')
