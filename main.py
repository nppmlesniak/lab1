
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def classify_bmi(bmi):
    if bmi < 16:
        return "wyglodzenie"
    elif bmi < 17:
        return "wychudzenie"
    elif bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidlowa"
    elif bmi < 30:
        return "nadwaga"
    elif bmi < 35:
        return "otylosc I stopnia"
    elif bmi < 40:
        return "otylosc II stopnia"
    else:
        return "otylosc III stopnia"

def read_positive_float(prompt, min_value, max_value):
    while True:
        try:
            value = input(prompt).strip()
            if value == "":
                raise ValueError
            value = float(value.replace(",", ".")) # pozwala na wpisanie liczby z przecinkiem

            if value < min_value or value > max_value:
                print(
                    f"podaj wartosc z zakresu "
                    f"{min_value}-{max_value}."
                )
                continue
            return value
        except ValueError:
            print("podaj poprawna liczbe.")

def read_name():
    while True:
        name = input("Podaj imie: ").strip()
        if name:
            return name
        print("imie nie moze byc puste")

def add_person(results):
    name = read_name()
    height = read_positive_float("Podaj wzrost w cm: ",80,250)

    weight = read_positive_float("Podaj mase ciała w kg: ",20,300)

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    person = {
        "name": name,
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "category": category
    }

    results.append(person)

    print("\nWynik:")
    print(f"Imie: {name}")
    print(f"BMI: {bmi:.2f}")
    print(f"Kategoria: {category}")

def show_history(results):
    if not results:
        print("Historia jest pusta.")
        return

    for number, person in enumerate(results, start=1):
        print(
            f"{number}. {person['name']} | "
            f"Wzrost: {person['height']} cm | "
            f"Masa: {person['weight']} kg | "
            f"BMI: {person['bmi']:.2f} | "
            f"{person['category']}"
        )

def show_summary(results):
    print("\n--- Podsumowanie ---")

    if not results:
        print("Brak wynikow do podsumowania.")
        return

    bmi_values = [person["bmi"] for person in results]

    average_bmi = sum(bmi_values) / len(bmi_values)
    minimum_bmi = min(bmi_values)
    maximum_bmi = max(bmi_values)

    categories = {
        "wyglodzenie": 0,
        "wychudzenie": 0,
        "niedowaga": 0,
        "waga prawidlowa": 0,
        "nadwaga": 0,
        "otylosc I stopnia": 0,
        "otylosc II stopnia": 0,
        "otylosc III stopnia": 0
    }

    for person in results:
        categories[person["category"]] += 1

    print(f"Liczba osób: {len(results)}")
    print(f"Średnie BMI: {average_bmi:.2f}")
    print(f"Min: {minimum_bmi:.2f}")
    print(f"Max: {maximum_bmi:.2f}")

    print("\nKategorie:")
    print(f"Wyglodzenie: {categories['wyglodzenie']}")
    print(f"Wychudzenie: {categories['wychudzenie']}")
    print(f"Niedowaga: {categories['niedowaga']}")
    print(f"Waga prawidlowa: {categories['waga prawidlowa']}")
    print(f"Nadwaga: {categories['nadwaga']}")
    print(f"Otylosc I stopnia: {categories['otylosc I stopnia']}")
    print(f"Otylosc II stopnia: {categories['otylosc II stopnia']}")
    print(f"Otylosc III stopnia: {categories['otylosc III stopnia']}")

def show_menu():
    print("\n======= KALKULATOR BMI =======")
    print("1. Dodaj wynik do bazy tymczasowej")
    print("2. Wyswietl historie")
    print("3. Pokaz podsumowanie biezacych wynikow")
    print("0. Zakoncz")

def main():
    results = []
    while True:
        show_menu()
        choice = input("Wybierz opcje: ").strip()
        if choice == "1":
            add_person(results)
        elif choice == "2":
            show_history(results)
        elif choice == "3":
            show_summary(results)
        elif choice == "0":
            break
        else:
            print("Nieprawidlowa opcja. Wybierz 0, 1, 2 lub 3.")


if __name__ == "__main__":
    main()