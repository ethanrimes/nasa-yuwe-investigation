"""Run the three remaining Nasa configs in sequence."""
import os, sys, json, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
py = os.path.join(".venv", "Scripts", "python.exe")
LABELS = [
    "Nasa All 1.3B",
    "Nasa Without Letters 600M",
    "Nasa Without Letters 1.3B",
]
for label in LABELS:
    print(f"\n##### LAUNCHING: {label}", flush=True)
    rc = subprocess.call([py, "-u", "eval_strict.py", "--only", label])
    print(f"##### EXIT {rc} for {label}", flush=True)
