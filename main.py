import os
# Two-line entry (222 chars): the lines below are the whole submission.
# Writes to /output/entry.txt.
LINE = "I am sorry I watered your laptop instead of the fern; they were both sitting on the desk and only one of them looked thirsty.\nI have learned to check for keyboards before watering, and from now on I will ask before I pour."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
