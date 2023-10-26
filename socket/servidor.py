import socket

HOST = 'localhost'  # Define o host como localhost
PORT = 65432        # Define a porta para conexão
VALID_TOKEN = "meu_token_secreto"  # Substitua isso pelo seu próprio token válido

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Cria um socket TCP
    s.bind((HOST, PORT))  # Associa o socket ao host e à porta especificados
    while True:
        s.listen()  # Habilita o socket para aceitar conexões
        conn, addr = s.accept()  # Aceita a conexão e obtém o objeto de conexão e o endereço do cliente
        with conn:
            print('Conectado por', addr)  # Imprime o endereço do cliente conectado
            authenticated = False
            while True:
                try:
                    data = conn.recv(1024)  # Recebe dados do cliente
                    if not data:  # Se não houver mais dados, sai do loop interno
                        break
                    message = data.decode()  # Decodifica os dados recebidos
                    if not authenticated:
                        if message.strip().startswith("TOKEN"):  # Verifica se a mensagem é um token
                            token = message.strip().split()[1]  # Extrai o token da mensagem recebida
                            if token == VALID_TOKEN:  # Verifica se o token é válido
                                conn.sendall(b'VALID')  # Envia uma confirmação de token válido para o cliente
                                authenticated = True
                                print('Token válido. Conexão estabelecida.')
                            else:
                                conn.sendall(b'INVALID')  # Envia uma notificação de token inválido para o cliente
                                print('Token inválido. Conexão não estabelecida.')
                                break  # Encerra a conexão se o token for inválido
                    else:
                        print(f"Mensagem recebida: {message}")  # Imprime a mensagem recebida do cliente
                        if message.strip().lower() == 'quit':  # Verifica se a mensagem recebida é 'quit'
                            print(addr, 'desconectado do servidor.')  # Imprime o endereço do cliente que se desconectou
                            conn.sendall(b'Desconectado do servidor.')  # Envia uma mensagem de desconexão para o cliente
                            break  # Encerra o loop interno, mas mantém o loop externo para aceitar novas conexões
                        # Adicione aqui a lógica para controlar o carrinho de acordo com a mensagem recebida
                except ConnectionResetError:
                    print("Conexão foi redefinida pelo peer.")
                    break
                except ConnectionAbortedError:
                    print("Conexão foi anulada pelo software no computador host.")
                    break
