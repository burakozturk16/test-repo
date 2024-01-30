import time

def start():
  print("service is started.")
  while True:
    print("service is running...")
    time.sleep(10)


if __name__ == "__main__":
  start()
