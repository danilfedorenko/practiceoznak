import json

def load_tasks():
    # Загружаем список задач из файла tasks.json
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не найден или содержит некорректный JSON, возвращаем пустой список
        tasks = []
    return tasks

def save_tasks(tasks):
    # Сохраняем список задач в файл tasks.json в формате JSON
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def show_tasks(tasks):
    # Отображаем список задач с их статусом
    if not tasks:
        print("Список задач пуст.")
        return
    # Сортируем задачи: невыполненные (done=False) идут первыми
    tasks.sort(key=lambda t: t['done'])
    print("Список задач:")
    for idx, task in enumerate(tasks, 1):
        status = "[x]" if task['done'] else "[ ]"
        print(f"{idx}. {status} {task['task']}")

def add_task(tasks):
    # Добавляем новую задачу
    task_text = input("Введите описание задачи: ")
    if task_text:
        tasks.append({"task": task_text, "done": False})
        save_tasks(tasks)
        print("Задача добавлена.")

def mark_task_done(tasks):
    # Отмечаем задачу как выполненную
    if not tasks:
        print("Нет задач для отметки.")
        return
    show_tasks(tasks)
    try:
        num = int(input("Введите номер выполненной задачи: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['done'] = True
            save_tasks(tasks)
            print(f"Задача \"{tasks[num-1]['task']}\" отмечена выполненной.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Введите корректный номер.")

def delete_task(tasks):
    # Удаляем задачу из списка
    if not tasks:
        print("Нет задач для удаления.")
        return
    show_tasks(tasks)
    try:
        num = int(input("Введите номер задачи для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"Задача \"{removed['task']}\" удалена.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Введите корректный номер.")

def main():
    # Загрузка существующих задач (если файл tasks.json существует)
    tasks = load_tasks()
    while True:
        print("\nTodoList CLI")
        print("1) Добавить задачу")
        print("2) Показать список задач")
        print("3) Отметить задачу как выполненную")
        print("4) Удалить задачу")
        print("5) Выход")
        choice = input("Выберите действие (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите цифру 1-5.")

if __name__ == "__main__":
    main()