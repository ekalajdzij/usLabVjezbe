import network
import time
import simple
from simple import MQTTClient
import machine
from machine import Pin, unique_id, PWM, ADC
import ubinascii
TEMASUBLED1 = 'USLABEMIR/led1'
TEMASUBLED2 = 'USLABEMIR/led2'
TEMASUBLED3 = 'USLABEMIR/led3'
TEMAPUBPOT = 'USLABEMIR/potenciometar'
TEMAPUBTAST = 'USLABEMIR/taster'
TEMATEST = 'USLABEMIR/test'
TEMAG = 'USLABEMIR/ledG'
TEMAB = 'USLABEMIR/ledB'
TEMAR = 'USLABEMIR/ledR'


taster = Pin(0, Pin.IN)
led1 = Pin(4, Pin.OUT)
led2 = Pin(5, Pin.OUT)
led3 = PWM(Pin(6))
pot = ADC(Pin(27))
G = PWM(Pin(12))
B = PWM(Pin(13))
R = PWM(Pin(14))

mqtt_server = 'broker.hivemq.com'
unique_id = ubinascii.hexlify(unique_id())
state = 0

potentiometar_value = 0.
taster_state = -1

def function(topic, message):
  print("PRIMLJENA PORUKA: ",topic, " value: ", message)
  if topic==b'USLABEMIR/led1':
    led1.value(int(message))
  elif topic==b'USLABEMIR/led2':
    led2.value(int(message))
  elif topic==b'USLABEMIR/led3':
    led3.duty_u16(int(65535*float(message)))
  elif topic==b'USLABEMIR/ledG':
    G.duty_u16(int(65535*float(message)))
  elif topic==b'USLABEMIR/ledB':
    B.duty_u16(int(65535*float(message)))
  elif topic==b'USLABEMIR/ledR':
    R.duty_u16(int(65535*float(message)))
 

print("Connecting to WiFi", end="")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Ugradbeni", "USlaboratorija220")
while not wlan.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected to WiFi!")
print(wlan.ifconfig())

mqtt_conn = MQTTClient(client_id=unique_id, server=mqtt_server, user='', password='', port=1883)

mqtt_conn.set_callback(function)
mqtt_conn.connect()
mqtt_conn.subscribe(TEMASUBLED1)
mqtt_conn.subscribe(TEMASUBLED2)
mqtt_conn.subscribe(TEMASUBLED3)
mqtt_conn.subscribe(TEMAG)
mqtt_conn.subscribe(TEMAB)
mqtt_conn.subscribe(TEMAR)


print('Connected to {0} MQTT broker'.format(mqtt_server))

while 1:
  mqtt_conn.check_msg()
  if(pot.read_u16()!=potentiometar_value):
    potentiometar_value = pot.read_u16()
    time.sleep(0.1)
    potString = "{\n \"Potenciometar\" : " + str(potentiometar_value/65535) + "\n}"
    mqtt_conn.publish(TEMAPUBPOT, potString)
  if taster_state!=taster.value():
    taster_state = taster.value()
    tasterString = "{\n \"Taster\" : " + str(taster_state) + "\n}"
    mqtt_conn.publish(TEMAPUBTAST, tasterString)
