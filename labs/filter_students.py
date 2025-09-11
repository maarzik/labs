students = {
    "Анна": [5, 4, 5, 5],
    "Борис": [3, 4, 4, 3],
    "Вика": [4, 5, 5, 4],
    "Глеб": [2, 3, 3, 4],
    "Рита": [5, 5, 5, 5],
}

threshold = float(input("Введите минимальный средний балл: "))

print("Студенты с баллом выше", threshold, ":")
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    if avg > threshold:
        print(f"{name} (средний = {avg:.2f})")