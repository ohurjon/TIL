spaces = "    "
stars = "*********"

# 0~4 까지 반복
for i in range(0, 5):
    print(spaces[:4 - i] + stars[:(1 + i * 2)])
