import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return []

    def save_notes(self):
        with open(self.filename, "w") as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, body):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = {"id": len(self.notes) + 1, "title": title, "body": body, "timestamp": timestamp}
        self.notes.append(note)
        self.save_notes()
        print("Заметка добавлена.")

    def display_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")
            print(f"Тело: {note['body']}")
            print("-" * 30)

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = new_title
                note["body"] = new_body
                note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print(f"Заметка с ID {note_id} изменена.")
                return
        print(f"Заметка с ID {note_id} не найдена.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self.save_notes()
        print(f"Заметка с ID {note_id} удалена.")

def main():
    app = NotesApp()

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            app.display_notes()
        elif choice == "2":
            title = input("Введите заголовок: ")
            body = input("Введите тело заметки: ")
            app.add_note(title, body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новое тело заметки: ")
            app.edit_note(note_id, new_title, new_body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            app.delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
