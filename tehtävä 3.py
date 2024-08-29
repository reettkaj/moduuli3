sukupuoli = input("Oletko nainen vai mies?:")

hemoglobiini = float(input("Mikä on hemoglobiiniarvosi?"))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiinisi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiinisi on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")









