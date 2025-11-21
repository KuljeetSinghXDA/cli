import os
from datetime import datetime

OUTPUT_DIR = "/data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

now = datetime.now()
filename = os.path.join(
    OUTPUT_DIR,
    f"output-{now.strftime('%Y%m%d-%H%M%S')}.txt"
)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Generated at: {now.isoformat()}\n")
    f.write("This file was created by the CLI inside the container.\n")

print("Wrote file:", filename)
