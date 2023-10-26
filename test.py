import time
import BlynkLib

BLYNK_AUTH = "teste123"

# Initializa o Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Aqui preciso analisar como fazer a comunicação com o Blynk e o retorno que o Joystick vai dar
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
   print(value)