def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Некоректний рядок: {line}")
                    continue

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)