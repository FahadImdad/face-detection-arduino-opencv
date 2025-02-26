#include <cvzone.h>

SerialData serialData(2, 1); // Array of 2 values received

int valsRec[2]; // Store received values

void setup() {
    pinMode(13, OUTPUT); // Yellow LED (Face Detected)
    pinMode(12, OUTPUT); // Red LED (No Face)
    serialData.begin(9600);
}

void loop() {
    serialData.Get(valsRec);

    digitalWrite(13, valsRec[0]); // Turn ON/OFF Yellow LED
    digitalWrite(12, valsRec[1]); // Turn ON/OFF Red LED

    delay(10);
}
