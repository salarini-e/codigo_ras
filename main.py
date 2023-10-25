# Aqui depois da funcionalidades estiverem prontas, iremos montar as rotinas do robô
import time
import network
import BlynkLib
from ras import CarrinhoDeDuasRodas

# Instancia o carrinho escolhendo os pinos que serão utilizados
meu_carrinho = CarrinhoDeDuasRodas(
                                        motor1_pwm_pin=17, 
                                        motor1_in1_pin=18, 
                                        motor1_in2_pin=23,
                                        
                                        motor2_pwm_pin=22, 
                                        motor2_in1_pin=24,
                                        motor2_in2_pin=25
                                    )

# Necessário inserir um arquivo envvars com as variáveis de ambientew.
# Por enquanto coloquei isso só pra ilustrar onde elas vão ficar
BLYNK_AUTH = "YOUR BLYNK-AUTH-TOKEN"
SSID = "SSID"
PASSWORD = "PASSWORD"

# Configura o Wi-Fi (Pensei em abstractar isso em uma função ou objeto para o código ficar mais limp)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('Aguardando conexão...')
    time.sleep(1)
 
# Habilita o Wi-Fi
if wlan.status() != 3:
    raise RuntimeError('Falha na conexão')
else:
    print('Conectado')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)

# Initializa o Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Aqui preciso analisar como fazer a comunicação com o Blynk e o retorno que o Joystick vai dar
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
   print(value)