import time
import os

def start():
  test_env = os.environ.get("test_variable")
  if test_env is None:
    test_env = "no"
  print("is environ loaded: " + test_env)
  print("service is started.")
  while True:
    print("service is running...")
    time.sleep(10)


if __name__ == "__main__":
  start()
