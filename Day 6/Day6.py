with open("input.txt", "r") as file:
  data = file.read()
  data = data.split("\n")

time = None
distance_record = None

for i, line in enumerate(data):
  line = int("".join(line.split()[1:]))
  if i == 0:
    time = line
  else:
    distance_record = line

record_breakers = 0

left = 1
right = time - 1

for speed in range(left, right):
  distance = (time - speed) * speed
  if distance > distance_record:
    left = speed
    break

for speed in range(right, 0, -1):
  distance = (time - speed) * speed
  if distance > distance_record:
    right = speed
    break

print(right - left + 1)
