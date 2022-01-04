a = "I'm" + " good"

print(a)
print(type(a))

print(len(a))

print(a[-1])  # última letra
print(a[::-1])  # inverte a ordem das letras

letter = "-#-"

print(letter * 10)

print(a.upper())

print("{} tem {} anos".format('Marcos Túlio', '11'))

result = 1890098/9

print("The result is {r:1.2f}".format(r=result))

print(f"The result is {result:1.2f}")

d = {
    'key1': [1, 2, 3, 4, 5]
}

print(d['key1'])

d['key1'] = ["a", "b", "c", "d"]

print(d['key1'])