#include <Adafruit_PWMServoDriver.h>

#define NOTEOFF_DELAY 50
#define PAUSA_ENTRE_LOOPS 1000
#define N_NOTAS 8

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40 /*default*/);

const int notas[N_NOTAS] = const int notas[] = {76, 71, 76, 69, 76, 71, 67, 74, };
const long note_on[N_NOTAS] = const int note_on[] = {0, 500, 1000, 1500, 2000, 2500, 3000, 3500, };

long notas_onoff[N_NOTAS * 2];
long tempos[N_NOTAS * 2];
long onoff[N_NOTAS * 2];
int i;

void setup() {
  for (int m = 0, n = 0, k = 0; k < N_NOTAS * 2; k++) {
    if (n >= N_NOTAS || note_on[m] < note_on[n] + NOTEOFF_DELAY) {
      tempos[k] = note_on[m];
      onoff[k] = 1;
      notas_onoff[k] = notas[m];
      m++;
    }
    else {
      tempos[k] = note_on[n] + NOTEOFF_DELAY;
      onoff[k] = 0;
      n++;
    }
  }


  i = 0;
  //initialize PWM board
  pwm.begin();
  pwm.setPWMFreq(1000);
}

void loop()
{
  if (onoff[i])
    pwm.setPWM(notas_onoff[i], 4096, 0);
  else
    pwm.setPWM(notas_onoff[i], 0, 4096);

  i++;
  if (i >= N_NOTAS) {
    i = 0;
    delay(PAUSA_ENTRE_LOOPS);
  }
  else {
    delay(tempos[i] - tempos[i - 1]);
  }
}
