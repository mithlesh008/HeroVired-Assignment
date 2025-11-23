# As a DevOps engineer, it is crucial to monitor the health and performance of servers. 
# Write a Python program to monitor the health of the CPU.

import psutil
import time
Threshold = 80

def monitor():
    print("Monitoring CPU usage...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > Threshold:
                print(f'Alert! CPU usage exceeds threshold: {cpu_usage}%')
    except KeyboardInterrupt:
        print("Monitoring Stopped by User by pressing CTRL+C")
    except Exception as e:
        print(f"Here is the error: {e}")

monitor()

