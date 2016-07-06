import subprocess
import glob

# Get all files in this repo with prefix `hello_`
files = glob.glob("hello_*")

# Run all files.
for f in files:
    subprocess.call(["python", f])
