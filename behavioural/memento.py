class TextEditor:
    def __init__(self):
        self.text = ""
        self.text_history = []
        self.history_index = -1

    def set_text(self, text: str):
        self.text = text
        self.text_history.append(text)
        self.history_index = len(self.text_history) - 1

    def undo(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.text = self.text_history[self.history_index]

    def redo(self):
        if self.history_index < len(self.text_history) - 1:
            self.history_index += 1
            self.text = self.text_history[self.history_index]


if __name__ == "__main__":
    text_editor = TextEditor()
    text_editor.set_text("Hello")
    text_editor.set_text("Hello World")
    text_editor.undo()
    print(text_editor.text)
    text_editor.redo()
    print(text_editor.text)
