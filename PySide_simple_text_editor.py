"""
Simple app created with use of PySide6 (Qt).

App structure (simplified):

- QMainWindow
   - QWidget
      - QVBoxLayout
         - QTextArea
         - QPushButton

Created by @aleksejalex
"""

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QPushButton, QFileDialog, QVBoxLayout
import sys


class MyOwnWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("My Own Text Editor")
        self.setMinimumSize(640, 480)

        # Create a central widget for the MyOwnWindow
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QTextEdit widget for the user to input text
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Enter text here... And when you'll be done, hit save button to save it as .txt!")

        # Create a QPushButton to save the contents of the text area
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_text)

        # Add the text area and save button to the central widget
        layout = QVBoxLayout()  # = vertical boxed layout
        layout.addWidget(self.text_area)
        layout.addWidget(self.save_button)
        central_widget.setLayout(layout)

    def save_text(self):
        """
        Simple function to save inputted text in 'text_area' to the '.txt' file.
        :return: None
        """
        # Open a file dialog to get the filename and path to save the file
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")

        # If a filename was selected, write the contents of the text area to the file
        if filename:
            with open(filename, "w") as f:
                f.write(self.text_area.toPlainText())


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    main_window = MyOwnWindow()
    main_window.show()

    # Running the event loop
    sys.exit(app.exec())
