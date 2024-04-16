#тип данных dict Словарь

a = {
    "car":"Toyota",
    "Model":"Camry",
    "images":["https://som-image/","https://some-im"],
    "price":25000000,
    "is-published":True
}

a = {"name":"Erbol","surname":"Askarov"}
b = a["name"] #Резултать Erbol
b = a.get("name") #Резултать Erbol
b = None
a["middle_name"]="Erzhanuly"
print(a)

person_data = {}
person_data = dict
person_data["name"] = "Kanat"
last_name = "Dauletbay"
person_data["last_name"] = last_name
print(person_data)

a = {"name":"Askar","lastname":"Erlanov"}
for k,v in a.items():
    print("key",k)
    print("value",v)

list_1 = [
    {
        "name": "Kanat",
        "last_name": "Erbolov",
        "age": 20
    },
    {
        "name": "Askar",
        "last_name": "Erzhanov",
        "age": 15
    },
    {
        "name": "Kairat",
        "last_name": "Zhandosov",
        "age": 45
    }
]

summ = 0
for i in list_1:
    age1 = i["age"]
    summ += age1

total_people = len(list_1)
average_age = summ / total_people
print(average_age)




