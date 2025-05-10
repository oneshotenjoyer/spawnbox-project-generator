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

        # Flags

        self.fontsFolder = False
        self.animFolder = False
        self.addBasicCode = False

        self.setFixedSize(QSize(800, 600))

        self.btn = QPushButton(
            text="Generate",
            parent=self
        )

        self.btn.setFixedSize(80, 40)
        self.btn.move(360, 280)
        self.btn.clicked.connect(self.generateBaseProject)

        self.errorLabel = QLabel(
            self,
            text=" " # temp
        )

        self.errorLabel.setFixedSize(780, 20)
        self.errorLabel.move(0, 350)
        self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.animFolderCheck = QCheckBox('Add /animations folder', self)
        self.animFolderCheck.setFixedSize(400, 20)
        self.animFolderCheck.move(300, 180)

        self.fontFolderCheck = QCheckBox('Add /fonts folder', self)
        self.fontFolderCheck.setFixedSize(400, 20)
        self.fontFolderCheck.move(300, 210)

        self.codeCheck = QCheckBox('Add basic code (will be boilerplate if unchecked)', self)
        self.codeCheck.setFixedSize(400, 20)
        self.codeCheck.move(300, 240)

        layout = QVBoxLayout()

        layout.addWidget(self.btn)
        layout.addWidget(self.errorLabel)
        layout.addWidget(self.animFolderCheck)
        layout.addWidget(self.fontFolderCheck)
        layout.addWidget(self.codeCheck)

        self.setLayout(layout)

    def generateBaseProject(self):
        self.animFolder = self.animFolderCheck.isChecked()
        self.fontsFolder = self.fontFolderCheck.isChecked()
        self.addBasicCode = self.codeCheck.isChecked()
        try:
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
                os.mkdir(dir_path + "/resources")
                if self.animFolder:
                    os.mkdir(dir_path + "/resources/animations")
                if self.fontsFolder:
                    os.mkdir(dir_path + "/resources/fonts")
                os.mkdir(dir_path + "/resources/sprites")
                if self.addBasicCode:
                    File.write("'''\n\n--- CREATED WITH SpawnBoxProjectGenerator. ---\n--- SBPG is under the Mozilla Public License v2.0. For more information, see https://mozilla.org/MPL/2.0/ ---\n\n'''\n\nimport spawnbox\
\n\nsbox = spawnbox.SpawnBox(\"My Title\", 800, 600, (0, 0, 0, 255))\nentity = spawnbox.Entity(sbox) # You don't have to specify all parameters!\nentity.center()\n\n@sbox.addUpdater\n\
def update(delta):\n\tif sbox.input.pressed[sbox.input.keys[\"W\"]]:\n\t\tentity.y -= 180 * delta\n\tif sbox.input.pressed[sbox.input.keys[\"A\"]]:\n\t\tentity.x -= 180 * delta\n\tif \
sbox.input.pressed[sbox.input.keys[\"S\"]]:\n\t\tentity.y += 180 * delta\n\tif sbox.input.pressed[sbox.input.keys[\"D\"]]:\n\t\tentity.x += 180 * delta\n\n@sbox.addDrawer\ndef draw():\n\t\
entity.draw()\n\nsbox.mainloop()")
                else:
                    File.write("'''\n\n--- CREATED WITH SpawnBoxProjectGenerator. ---\n--- SBPG is under the Mozilla Public License v2.0. For more information, see https://mozilla.org/MPL/2.0/ ---\n\n'''\n\nimport spawnbox\
\n\nsbox = spawnbox.SpawnBox(\"My Title\", 800, 600, (0, 0, 0, 255))\n\n@sbox.addUpdater\ndef update(delta):\
\n\tpass\n\n@sbox.addDrawer\ndef draw():\n\tpass\n\nsbox.mainloop()")
        except:
            self.errorLabel.setText(f"Please empty folder {dir_path} before using SBPG.")

        

window = MainWindow()
window.show()

app.exec()