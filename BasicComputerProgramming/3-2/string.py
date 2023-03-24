chars = "534183552676"

for c in chars:
    if c > "5":
        print("first", c)
        break
for c in reversed(chars):
    if c < "5":
        print("two", c)
        break
