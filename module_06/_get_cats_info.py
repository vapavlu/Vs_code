def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_info = line.strip().split(',')
                cat_dict = {"id": cat_info[0], "name": cat_info[1], "age": cat_info[2]}
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats_list

cats_info = get_cats_info("cats_info.py")
print(cats_info)

# не можу написати шлях до файлу, щоб програма його бачила (cats_info.py)