def presenteer(dictionary, totaal):
    for sleutel, waarde in dictionary.items():
        print(f"{sleutel} : {waarde} euro")
    print("=" * 26)
    print(f"Totaal : {totaal} euro")