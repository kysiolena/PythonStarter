import json
import os

PATH = os.path.abspath(__file__ + '/..')

default_subjects = {
    "Математика": [],
    "Укр. Мова": [],
    "Хімія": [],
    "Фізика": [],
    "Англ. Мова": [],
    "Фізкультура": [],
}

students = []

menu_choices = [
    "Додати учня",
    "Видали учня",
    "Переглянути учнів",
    "Переглянути оцінки учня",
    "Поставити оцінку учню",
    "Вихід",
]

while True:
    for idx, text in enumerate(menu_choices):
        print(f"{idx+1}. {text}")

    user_choice = int(input())

    match user_choice:
        case 1:
            student_name = input("Введіть ім'я учня: ")
            student_surname = input("Введіть прізвище учня: ")
            new_student = {
                "name": student_name,
                "surname": student_surname,
                "marks": default_subjects.copy(),
            }
            students.append(new_student)
        case 2:
            if students:
                print()
                for idx, student in enumerate(students):
                    student_name = student["name"]
                    student_surname = student["surname"]
                    print(f"{idx+1}. {student_name} {student_surname}")
                print()

                index_for_remove = int(input("Введіть номер учня для видалення: "))
                index_for_remove -= 1
                if 0 <= index_for_remove < len(students):
                    removed_student = students.pop(index_for_remove)
                    print(
                        f"Учня {removed_student['name']} {removed_student['surname']} було видалено"
                    )

        case 3:
            print()
            for idx, student in enumerate(students):
                student_name = student["name"]
                student_surname = student["surname"]
                print(f"{idx+1}. {student_name} {student_surname}")
            print()
        case 4:
             if students:
                print()
                for idx, student in enumerate(students):
                    student_name = student["name"]
                    student_surname = student["surname"]
                    print(f"{idx+1}. {student_name} {student_surname}")
                print()

                index_for_mark = int(input("Введіть номер учня оцінки якого треба переглянути: "))
                index_for_mark -= 1
                if 0 <= index_for_mark < len(students):
                    student = students[index_for_mark]
                    for subject_name, marks in student['marks'].items():
                        print(subject_name)
                        print("|".join(list(map(str, marks))))
                        print("=" * 10)
        case 5:
            if students:
                print()
                for idx, student in enumerate(students):
                    student_name = student["name"]
                    student_surname = student["surname"]
                    print(f"{idx+1}. {student_name} {student_surname}")
                print()

                index_for_mark = int(input("Введіть номер учня для оцінки: "))
                index_for_mark -= 1
                if 0 <= index_for_mark < len(students):
                    student = students[index_for_mark]
                    subjects_list = list(student["marks"].keys())
                    for idx, subject in enumerate(subjects_list):
                        print(f"{idx+1} - {subject}")
                    subject_index = int(
                        input("Введіть номер предмата по якому треба поставити оцінку: ")
                    )
                    subject_index -= 1
                    subject_key = subjects_list[subject_index]
                    if 0 <= subject_index < len(subjects_list):
                        mark = int(input("Введіть оцінку яку треба поставити: "))
                        if 1 <= mark <= 12:
                            student['marks'][subject_key].append(mark)
        case 6:
            break

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)