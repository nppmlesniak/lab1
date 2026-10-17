
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidlowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otylosc"

def read_positive_float(prompt, min_value, max_value):
    while True:
        try:
            value = input(prompt).strip()

            if value == "":
                raise ValueError

            # Pozwala wpisać np. 70,5 zamiast 70.5
            value = float(value.replace(",", "."))

            if value < min_value or value > max_value:
                print(
                    f"Błąd: podaj wartość z zakresu "
                    f"{min_value}-{max_value}."
                )
                continue

            return value

        except ValueError:
            print("Błąd: podaj poprawną liczbę.")

def read_name():
    while True:
        name = input("Podaj imię: ").strip()

        if name:
            return name

        print("Błąd: imię nie może być puste.")


def add_person(results):
    print("\n--- Dodawanie wyniku ---")

    name = read_name()

    height = read_positive_float(
        "Podaj wzrost w cm: ",
        80,
        250
    )

    weight = read_positive_float(
        "Podaj masę ciała w kg: ",
        20,
        300
    )

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
    print(f"Imię: {name}")
    print(f"BMI: {bmi:.2f}")
    print(f"Kategoria: {category}")

def show_history(results):
    print("\n--- Historia wyników ---")

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
        print("Brak wyników do podsumowania.")
        return

    bmi_values = [person["bmi"] for person in results]

    average_bmi = sum(bmi_values) / len(bmi_values)
    minimum_bmi = min(bmi_values)
    maximum_bmi = max(bmi_values)

    categories = {
        "niedowaga": 0,
        "waga prawidłowa": 0,
        "nadwaga": 0,
        "otyłość": 0
    }

    for person in results:
        categories[person["category"]] += 1

    print(f"Liczba osób: {len(results)}")
    print(f"Średnie BMI: {average_bmi:.2f}")
    print(f"Min: {minimum_bmi:.2f}")
    print(f"Max: {maximum_bmi:.2f}")

    print("\nKategorie:")
    print(f"Niedowaga: {categories['niedowaga']}")
    print(f"Waga prawidłowa: {categories['waga prawidłowa']}")
    print(f"Nadwaga: {categories['nadwaga']}")
    print(f"Otyłość: {categories['otyłość']}")

def show_menu():
    print("\n=== KALKULATOR BMI ===")
    print("1. Dodaj wynik")
    print("2. Wyświetl historię")
    print("3. Pokaż podsumowanie")
    print("0. Zakończ")

def main():
    results = []

    while True:
        show_menu()

        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            add_person(results)

        elif choice == "2":
            show_history(results)

        elif choice == "3":
            show_summary(results)

        elif choice == "0":
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja. Wybierz 0, 1, 2 lub 3.")


if __name__ == "__main__":
    main()