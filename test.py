import subprocess

files = ["test_1.py", "test_2.py", "test_3.py", "test_4.py", "test_5.py"]

# for file in files:
#     subprocess.run(["pytest", file])

for file in files:
    subprocess.run(["black", file])