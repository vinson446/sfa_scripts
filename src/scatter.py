from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds


def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class ScatterUI(QtWidgets.QDialog):
    """Scatter UI Class"""

    def __init__(self):
        super(ScatterUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Scatter Tool")
        self.setMinimumWidth(500)
        self.setMaximumWidth(750)
        self.setMaximumHeight(200)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_ui()
        self.create_connections()

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font: bold 20px")
        self.header_lay = self._create_header_ui()
        self.button_lay = self._create_polygon_ui()
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.main_lay.addStretch()
        self.main_lay.addLayout(self.header_lay)
        self.main_lay.addLayout(self.button_lay)
        self.setLayout(self.main_lay)

    def _create_polygon_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.sphere_btn = QtWidgets.QPushButton("Sphere")
        self.cube_btn = QtWidgets.QPushButton("Cube")
        self.cylinder_btn = QtWidgets.QPushButton("Cylinder")
        self.cone_btn = QtWidgets.QPushButton("Cone")
        self.descriptor_le = QtWidgets.QLineEdit()
        layout.addWidget(self.sphere_btn)
        layout.addWidget(self.cube_btn)
        layout.addWidget(self.cylinder_btn)
        layout.addWidget(self.cone_btn)
        layout.addWidget(self.descriptor_le)
        return layout

    def _create_header_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.descriptor_header_lbl = QtWidgets.QLabel("Polygon Object")
        self.descriptor_header_lbl.setStyleSheet("font: bold")
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.descriptor_header_lbl, 0, 0)
        return layout

    def create_connections(self):
        """Connect Signals and Slots"""
        self.sphere_btn.clicked.connect(self._save_polygon_as_sphere)
        self.cube_btn.clicked.connect(self._save_polygon_as_cube)
        self.cylinder_btn.clicked.connect(self._save_polygon_as_cylinder)
        self.cone_btn.clicked.connect(self._save_polygon_as_cone)

    @QtCore.Slot()
    def _save_polygon_as_sphere(self):
        self.descriptor_le.setText("Sphere")

    @QtCore.Slot()
    def _save_polygon_as_cube(self):
        self.descriptor_le.setText("Cube")

    @QtCore.Slot()
    def _save_polygon_as_cylinder(self):
        self.descriptor_le.setText("Cylinder")

    @QtCore.Slot()
    def _save_polygon_as_cone(self):
        self.descriptor_le.setText("Cone")
