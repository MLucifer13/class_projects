import re
name = input("Whats your name?").strip()
if match := re.search(r"^(.+), *(.+)$", name):
    name = match.group(1) + " " + match.group(2)

print(f"Hello, {name}")
    