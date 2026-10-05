name = "Анна"
price = 125000

text = "125000"
number = 125000
print(type(text), type(number))

is_ready = True
print("Готово?", is_ready)

files = ["a.pdf", "b.pdf", "c.pdf"]
files.append("d.pdf")
print(files)

ticket = {"номер": 5412, "статус": "в работе"}
print(ticket["статус"])

if price > 100000:
    print("Дорого")
else:
    print("Недорого")

for f in files:
    print("Обрабатываю", f)


def percent(value, p):
    return value * p / 100


print(percent(125000, 17))
