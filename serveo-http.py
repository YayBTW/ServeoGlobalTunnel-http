import subprocess
import time

print("*****************************")
print("OPENING SERVEO-HTTP TO GLOBAL")
print("-----------BY YAY------------")
print("*****************************")

link=subprocess.run('ssh -R 80:localhost:80 serveo.net', shell=True, text=True, encoding='utf-8', errors='replace')
time.sleep(3)

print(link)