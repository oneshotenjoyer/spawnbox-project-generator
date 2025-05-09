import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

'''
  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SBPG v0.0.1 by ModGuy07")

        self.setFixedSize(QSize(800, 600))

        self.btn = QPushButton(
            text="Generate",
            parent=self
        )

        self.btn.setFixedSize(80, 40)
        self.btn.move(360, 280)
        self.btn.clicked.connect(self.generateBaseProject)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def generateBaseProject(self):
        HOME = None
        if sys.platform in ["linux", "darwin"]:
            HOME = os.getenv("HOME")
        elif sys.platform == "win32":
            HOME = os.getenv("userprofile")
        dir_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select directory",
            directory=HOME,
            options=QFileDialog.Option.ShowDirsOnly,
        )   
        with open(dir_path + "/main.py", "w") as File:
            File.write("'''\n\n--- CREATED WITH SpawnBoxProjectGenerator ---\n\n'''\n\nimport spawnbox\
\n\nsbox = spawnbox.SpawnBox(\"My Title\", 800, 600, (0, 0, 0, 255))\n\n@sbox.addUpdater\ndef update(delta):\
\n\tpass\n\n@sbox.addDrawer\ndef draw():\n\tpass\n\nsbox.mainloop()")
        

window = MainWindow()
window.show()

app.exec()