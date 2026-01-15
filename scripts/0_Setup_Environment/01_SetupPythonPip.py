import subprocess

subprocess.run(["python", "--version"])
subprocess.run(["pip", "--version"])
subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"])

print("Update Python and Pip Completed")