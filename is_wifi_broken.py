# is_wifi_broken.py
"""
Python Challenge:
	Check your wifi is broken by someone
"""
import socket
import time

def is_wifi_broken():
  """Checks if the WiFi is broken by someone."""
  try:
    # Try to connect to a public DNS server.
    socket.create_connection(("8.8.8.8", 53), 2)
    return False
  except socket.error:
    return True

def main():
  """Checks the WiFi status and prints a message."""
  wifi_broken = is_wifi_broken()
  if wifi_broken:
    print("Your WiFi may be broken by someone.")
  else:
    print("Your WiFi is working fine.")

if __name__ == "__main__":
  main()
