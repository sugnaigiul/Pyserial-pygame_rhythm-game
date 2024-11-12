void setup() {
  Serial.begin(9600);  // Initialise la communication série à 9600 bauds
}

void loop() {
  int potValue = analogRead(A0);      // Lit la valeur du potentiomètre
  Serial.println(potValue);           // Envoie la valeur lue par la liaison série
  delay(50);                          // Petit délai pour éviter la surcharge
}
