#tehtävä 1
kuha= float(input("Minkä pituinen kuha on?: "))
if kuha>=37:
    print("Hieno kuha!")
else:
    print(f"Kuha on alamittainen. Siitä puuttuu {37 - kuha:.1f} senttimetriä.")

