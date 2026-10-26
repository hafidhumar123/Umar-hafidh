light = "pink"
status = ""
"""
red = stop
yellow = stop
green = go
"""
if light == "red":
    status = "Stop"
elif light == "yellow":
    status = "ready"
elif light == "green":
    status = "move"
else:
    status = "invalid light" 
print(status)      