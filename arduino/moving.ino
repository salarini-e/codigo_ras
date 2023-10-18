// Define os pinos
#define ENA 12
#define IN1 8
#define IN2 7
#define ENB 1
#define IN3 4
#define IN4 2

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void loop() {
  // Move os motores para frente
  moveForward();
  delay(2000);

  // Move os motores para trás
  moveBackward();
  delay(2000);

  // Para os motores
  stopMotors();
  delay(2000);

  // Gira os motores para a esquerda
  turnLeft();
  delay(2000);

  // Gira os motores para a direita
  turnRight();
  delay(2000);

  // Para os motores
  stopMotors();
  delay(2000);
}

// Função para mover os motores para frente
void moveForward() {
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

// Função para mover os motores para trás
void moveBackward() {
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

// Função para parar os motores
void stopMotors() {
  digitalWrite(ENA, LOW);
  digitalWrite(ENB, LOW);
}

// Função para girar os motores para a esquerda
void turnLeft() {
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

// Função para girar os motores para a direita
void turnRight() {
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}
