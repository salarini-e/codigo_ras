import RPi.GPIO as GPIO
import time

class CarrinhoDeDuasRodas:

    # Python não tem construtor, mas tem um método especial chamado __init__ que é chamado quando a classe é instanciada
    def __init__(self, motor1_pwm_pin, motor1_in1_pin, motor1_in2_pin,
                       motor2_pwm_pin, motor2_in1_pin, motor2_in2_pin):
        
        # Configuração dos pinos GPIO
        self.motor1_pwm_pin = motor1_pwm_pin
        self.motor1_in1_pin = motor1_in1_pin
        self.motor1_in2_pin = motor1_in2_pin
        self.motor2_pwm_pin = motor2_pwm_pin
        self.motor2_in1_pin = motor2_in1_pin
        self.motor2_in2_pin = motor2_in2_pin
 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor1_pwm_pin, GPIO.OUT)
        GPIO.setup(self.motor1_in1_pin, GPIO.OUT)
        GPIO.setup(self.motor1_in2_pin, GPIO.OUT)
        GPIO.setup(self.motor2_pwm_pin, GPIO.OUT)
        GPIO.setup(self.motor2_in1_pin, GPIO.OUT)
        GPIO.setup(self.motor2_in2_pin, GPIO.OUT)

        # Criação dos objetos PWM para os motores
        self.motor1_pwm = GPIO.PWM(self.motor1_pwm_pin, 100)  # Frequência de PWM: 100 Hz
        self.motor2_pwm = GPIO.PWM(self.motor2_pwm_pin, 100)  # Frequência de PWM: 100 Hz

        # Inicialização do PWM com velocidade zero
        self.motor1_pwm.start(0)
        self.motor2_pwm.start(0)

    # Comandos
    def frente(self, velocidade=50):
        GPIO.output(self.motor1_in1_pin, GPIO.HIGH)
        GPIO.output(self.motor1_in2_pin, GPIO.LOW)
        GPIO.output(self.motor2_in1_pin, GPIO.HIGH)
        GPIO.output(self.motor2_in2_pin, GPIO.LOW)
        self.motor1_pwm.ChangeDutyCycle(velocidade)
        self.motor2_pwm.ChangeDutyCycle(velocidade)

    def tras(self, velocidade=50):
        GPIO.output(self.motor1_in1_pin, GPIO.LOW)
        GPIO.output(self.motor1_in2_pin, GPIO.HIGH)
        GPIO.output(self.motor2_in1_pin, GPIO.LOW)
        GPIO.output(self.motor2_in2_pin, GPIO.HIGH)
        self.motor1_pwm.ChangeDutyCycle(velocidade)
        self.motor2_pwm.ChangeDutyCycle(velocidade)

    def esquerda(self, velocidade=50):
        GPIO.output(self.motor1_in1_pin, GPIO.HIGH)
        GPIO.output(self.motor1_in2_pin, GPIO.LOW)
        GPIO.output(self.motor2_in1_pin, GPIO.LOW)
        GPIO.output(self.motor2_in2_pin, GPIO.HIGH)
        self.motor1_pwm.ChangeDutyCycle(velocidade)
        self.motor2_pwm.ChangeDutyCycle(velocidade)

    def direita(self, velocidade=50):
        GPIO.output(self.motor1_in1_pin, GPIO.LOW)
        GPIO.output(self.motor1_in2_pin, GPIO.HIGH)
        GPIO.output(self.motor2_in1_pin, GPIO.HIGH)
        GPIO.output(self.motor2_in2_pin, GPIO.LOW)
        self.motor1_pwm.ChangeDutyCycle(velocidade)
        self.motor2_pwm.ChangeDutyCycle(velocidade)
    
    def parar(self):
        GPIO.output(self.motor1_in1_pin, GPIO.LOW)
        GPIO.output(self.motor1_in2_pin, GPIO.LOW)
        GPIO.output(self.motor2_in1_pin, GPIO.LOW)
        GPIO.output(self.motor2_in2_pin, GPIO.LOW)
        self.motor1_pwm.ChangeDutyCycle(0)
        self.motor2_pwm.ChangeDutyCycle(0)

    def cleanup(self):
        GPIO.cleanup()

#Teste do carrinho 
if __name__ == "__main__":

    meu_carrinho = CarrinhoDeDuasRodas(motor1_pwm_pin=17, motor1_in1_pin=18, motor1_in2_pin=23,
                                    motor2_pwm_pin=22, motor2_in1_pin=24, motor2_in2_pin=25)

    try:
        while True:
            comando = input("Digite o comando (f = frente, t = tras, e = esquerda, d = direita, p = parar ou s = sair): ")
            if comando == "f":
                meu_carrinho.frente()
            elif comando == "t":
                meu_carrinho.tras()
            elif comando == "e":
                meu_carrinho.esquerda()
            elif comando == "d":
                meu_carrinho.direita()
            elif comando == "p":
                meu_carrinho.parar()
            elif comando == "s":
                break
            else:
                print("Comando inválido!")

    except KeyboardInterrupt:
        pass 

    finally:
        meu_carrinho.cleanup()