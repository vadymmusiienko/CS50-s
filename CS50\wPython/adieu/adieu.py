import inflect

p = inflect.engine()
names = []
while True:
    try:
        names.append(input(": "))
    except EOFError:
        break

sentence = p.join(names)
print("Adieu, adieu, to", p.join(names))
