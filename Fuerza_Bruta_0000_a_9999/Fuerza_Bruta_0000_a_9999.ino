#include "DigiKeyboard.h"

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  int d = 100;
  for(int i=0;i<=9;i=i+1){
    for(int j=0;j<=9;j=j+1){
      for(int k=0;k<=9;k=k+1){
        for(int h=0;h<=9;h=h+1){
          DigiKeyboard.print(i);
          DigiKeyboard.print(j);
          DigiKeyboard.print(k);
          DigiKeyboard.println(h);
          DigiKeyboard.sendKeyStroke(KEY_ENTER);
          delay(1000);
        }
      }
    }
  }

}
