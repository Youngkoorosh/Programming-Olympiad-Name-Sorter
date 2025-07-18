HMTime = int(input("How many people we have: "))

inf = {"f": [], "m": []}  

for i in range(HMTime):
    x = input("Enter gender(m, f) and Enter name and programming language: ").split(".")
    if len(x) >= 3:  
        person_gender = x[0].lower()
        person_name = x[1].capitalize()
        person_language = x[2]
        inf[person_gender].append((person_name, person_language))


inf["f"].sort()
inf["m"].sort()


for name, language in inf["f"]:
    print(f"f {name} {language}")

for name, language in inf["m"]:
    print(f"m {name} {language}")
