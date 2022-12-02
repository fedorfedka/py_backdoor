import subprocess
import os

args = ['cd']

try:
    result = subprocess.run(args, shell=True, capture_output=True)
    print(result.stdout)
except Exception as e:
    result = e

print(len(b'\a\a'))
