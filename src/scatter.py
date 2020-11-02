from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import random


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
        self.setMaximumWidth(600)
        self.setMaximumHeight(200)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_ui()
        self.create_connections()

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font: bold 20px")
        self.header_rand_density_lay = self._create_header_rand_density_ui()
        self.rand_density_lay = self._create_rand_density_ui()
        self.header_rand_scale_lay = self._create_header_rand_scale_ui()
        self.rand_scale_lay = self._create_rand_scale_ui()
        self.header_rand_rot_lay = self._create_header_rand_rot_ui()
        self.rand_rot_lay = self._create_rand_rot_ui()
        self.scatter_lay = self._create_scatter_ui()
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.main_lay.addLayout(self.scatter_lay)
        self.main_lay.addLayout(self.header_rand_density_lay)
        self.main_lay.addLayout(self.rand_density_lay)
        self.main_lay.addLayout(self.header_rand_scale_lay)
        self.main_lay.addLayout(self.rand_scale_lay)
        self.main_lay.addLayout(self.header_rand_rot_lay)
        self.main_lay.addLayout(self.rand_rot_lay)
        self.main_lay.addStretch()
        self.setLayout(self.main_lay)

    def _create_scatter_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        layout.addWidget(self.scatter_btn)
        return layout

    def _create_header_rand_density_ui(self):
        layout = QtWidgets.QGridLayout()
        self.header_density_lbl = QtWidgets.QLabel("Random Density Scatter")
        self.header_density_lbl.setStyleSheet("font: bold")
        layout.addWidget(self.header_density_lbl, 0, 0)
        return layout

    def _create_rand_density_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.rand_density_lbl = QtWidgets.QLabel("Density Percentage")
        self.rand_density_le = QtWidgets.QLineEdit()
        self.rand_density_btn = QtWidgets.QPushButton("Scatter")
        layout.addWidget(self.rand_density_lbl)
        layout.addWidget(self.rand_density_le)
        layout.addWidget(self.rand_density_btn)
        return layout

    def _create_header_rand_scale_ui(self):
        layout = QtWidgets.QGridLayout()
        self.header_scale_lbl = QtWidgets.QLabel("Random Scale")
        self.header_scale_lbl.setStyleSheet("font: bold")
        layout.addWidget(self.header_scale_lbl, 0, 0)
        return layout

    def _create_rand_scale_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.rand_min_scale_x_lbl = QtWidgets.QLabel("X Min")
        self.rand_min_scale_x_le = QtWidgets.QLineEdit()
        self.rand_max_scale_x_lbl = QtWidgets.QLabel("X Max")
        self.rand_max_scale_x_le = QtWidgets.QLineEdit()
        self.rand_min_scale_y_lbl = QtWidgets.QLabel("Y Min")
        self.rand_min_scale_y_le = QtWidgets.QLineEdit()
        self.rand_max_scale_y_lbl = QtWidgets.QLabel("Y Max")
        self.rand_max_scale_y_le = QtWidgets.QLineEdit()
        self.rand_min_scale_z_lbl = QtWidgets.QLabel("Z Min")
        self.rand_min_scale_z_le = QtWidgets.QLineEdit()
        self.rand_max_scale_z_lbl = QtWidgets.QLabel("Z Max")
        self.rand_max_scale_z_le = QtWidgets.QLineEdit()
        self.rand_scale_btn = QtWidgets.QPushButton("Scale")
        layout.addWidget(self.rand_min_scale_x_lbl)
        layout.addWidget(self.rand_min_scale_x_le)
        layout.addWidget(self.rand_max_scale_x_lbl)
        layout.addWidget(self.rand_max_scale_x_le)
        layout.addWidget(self.rand_min_scale_y_lbl)
        layout.addWidget(self.rand_min_scale_y_le)
        layout.addWidget(self.rand_max_scale_y_lbl)
        layout.addWidget(self.rand_max_scale_y_le)
        layout.addWidget(self.rand_min_scale_z_lbl)
        layout.addWidget(self.rand_min_scale_z_le)
        layout.addWidget(self.rand_max_scale_z_lbl)
        layout.addWidget(self.rand_max_scale_z_le)
        layout.addWidget(self.rand_scale_btn)
        return layout

    def _create_header_rand_rot_ui(self):
        layout = QtWidgets.QGridLayout()
        self.header_rot_lbl = QtWidgets.QLabel("Random Rotation")
        self.header_rot_lbl.setStyleSheet("font: bold")
        layout.addWidget(self.header_rot_lbl, 0, 0)
        return layout

    def _create_rand_rot_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.rand_rot_min_x_lbl = QtWidgets.QLabel("X Min")
        self.rand_rot_min_x_le = QtWidgets.QLineEdit()
        self.rand_rot_max_x_lbl = QtWidgets.QLabel("X Max")
        self.rand_rot_max_x_le = QtWidgets.QLineEdit()
        self.rand_rot_min_y_lbl = QtWidgets.QLabel("Y Min")
        self.rand_rot_min_y_le = QtWidgets.QLineEdit()
        self.rand_rot_max_y_lbl = QtWidgets.QLabel("Y Max")
        self.rand_rot_max_y_le = QtWidgets.QLineEdit()
        self.rand_rot_min_z_lbl = QtWidgets.QLabel("Z Min")
        self.rand_rot_min_z_le = QtWidgets.QLineEdit()
        self.rand_rot_max_z_lbl = QtWidgets.QLabel("Z Max")
        self.rand_rot_max_z_le = QtWidgets.QLineEdit()
        self.rand_rot_btn = QtWidgets.QPushButton("Rotate")
        layout.addWidget(self.rand_rot_min_x_lbl)
        layout.addWidget(self.rand_rot_min_x_le)
        layout.addWidget(self.rand_rot_max_x_lbl)
        layout.addWidget(self.rand_rot_max_x_le)
        layout.addWidget(self.rand_rot_min_y_lbl)
        layout.addWidget(self.rand_rot_min_y_le)
        layout.addWidget(self.rand_rot_max_y_lbl)
        layout.addWidget(self.rand_rot_max_y_le)
        layout.addWidget(self.rand_rot_min_z_lbl)
        layout.addWidget(self.rand_rot_min_z_le)
        layout.addWidget(self.rand_rot_max_z_lbl)
        layout.addWidget(self.rand_rot_max_z_le)
        layout.addWidget(self.rand_rot_btn)
        return layout

    def create_connections(self):
        """Connect Signals and Slots"""
        self.scatter_btn.clicked.connect(self.get_polygon_vert_list)
        self.rand_density_btn.clicked.connect(self.get_rand_density)
        self.rand_scale_btn.clicked.connect(self.rand_polygon_scale)
        self.rand_rot_btn.clicked.connect(self.rand_polygon_rot_offset)

    @QtCore.Slot()
    def get_polygon_vert_list(self):
        polygon_vert_list = cmds.ls(selection=True, fl=True)
        self.polygon_inst = polygon_vert_list[0]
        self.scatter_polygon_inst_on_vert(polygon_vert_list)

    def scatter_polygon_inst_on_vert(self, polygon_list):
        """Scatter polygon instances on another object's vertices"""
        for inst in polygon_list:
            vert_pos = cmds.xform(inst, q=True, ws=True, t=True)

            new_instance = cmds.instance(polygon_list, n="polygon_inst")
            cmds.move(vert_pos[0], vert_pos[1], vert_pos[2],
                      new_instance)

        #cmds.delete(self.polygon_inst, "polygon_inst")

    @QtCore.Slot()
    def get_rand_density(self):
        polygon_vert_list = cmds.ls(selection=True, fl=True)
        self.polygon_inst = polygon_vert_list[0]
        random.shuffle(polygon_vert_list)

        try:
            density_percentage = float(self.rand_density_le.text())
            self.density_number = int(density_percentage *
                                      len(polygon_vert_list))
        except ValueError:
            self.density_number = 0

        density_polygon_inst_list = polygon_vert_list[:self.density_number]
        self.scatter_polygon_inst_on_vert(density_polygon_inst_list)

    @QtCore.Slot()
    def rand_polygon_scale(self):
        polygon_inst_list = cmds.ls("polygon_inst*")
        for inst in polygon_inst_list:
            try:
                min_scale_x = int(self.rand_min_scale_x_le.text())
                self.polygon_min_scale_x = min_scale_x
                max_scale_x = int(self.rand_max_scale_x_le.text())
                self.polygon_max_scale_x = max_scale_x
            except ValueError:
                self.polygon_min_scale_x = 0
                self.polygon_max_scale_x = 0

            try:
                min_scale_y = int(self.rand_min_scale_y_le.text())
                self.polygon_min_scale_y = min_scale_y
                max_scale_y = int(self.rand_max_scale_y_le.text())
                self.polygon_max_scale_y = max_scale_y
            except ValueError:
                self.polygon_min_scale_y = 0
                self.polygon_max_scale_y = 0

            try:
                min_scale_z = int(self.rand_min_scale_z_le.text())
                self.polygon_min_scale_z = min_scale_z
                max_scale_z = int(self.rand_max_scale_z_le.text())
                self.polygon_max_scale_z = max_scale_z
            except ValueError:
                self.polygon_min_scale_z = 0
                self.polygon_max_scale_z = 0

            rand_scale_x = random.uniform(self.polygon_min_scale_x,
                                          self.polygon_max_scale_x)
            rand_scale_y = random.uniform(self.polygon_min_scale_y,
                                          self.polygon_max_scale_y)
            rand_scale_z = random.uniform(self.polygon_min_scale_z,
                                          self.polygon_max_scale_z)
            cmds.scale(rand_scale_x,
                       rand_scale_y,
                       rand_scale_z,
                       inst, a=True)

    @QtCore.Slot()
    def rand_polygon_rot_offset(self):
        polygon_inst_list = cmds.ls("polygon_inst*")
        for inst in polygon_inst_list:
            try:
                min_x_rot = int(self.rand_rot_min_x_le.text())
                self.polygon_min_x_rot = min_x_rot
                max_x_rot = int(self.rand_rot_max_x_le.text())
                self.polygon_max_x_rot = max_x_rot
            except ValueError:
                self.polygon_min_x_rot = 0
                self.polygon_max_x_rot = 0

            try:
                min_y_rot = int(self.rand_rot_min_y_le.text())
                self.polygon_min_y_rot = min_y_rot
                max_y_rot = int(self.rand_rot_max_y_le.text())
                self.polygon_max_y_rot = max_y_rot
            except ValueError:
                self.polygon_min_y_rot = 0
                self.polygon_max_y_rot = 0

            try:
                min_z_rot = int(self.rand_rot_min_z_le.text())
                self.polygon_min_z_rot = min_z_rot
                max_z_rot = int(self.rand_rot_max_z_le.text())
                self.polygon_max_z_rot = max_z_rot
            except ValueError:
                self.polygon_min_z_rot = 0
                self.polygon_max_z_rot = 0

            current_rot = cmds.xform(inst, q=True, ro=True)

            rand_polygon_rot_x_offset = random.uniform(
                self.polygon_min_x_rot, self.polygon_max_x_rot)
            rand_polygon_rot_y_offset = random.uniform(
                self.polygon_min_y_rot, self.polygon_max_y_rot)
            rand_polygon_rot_z_offset = random.uniform(
                self.polygon_min_z_rot, self.polygon_max_z_rot)

            cmds.rotate(current_rot[0] + rand_polygon_rot_x_offset,
                        current_rot[1] + rand_polygon_rot_y_offset,
                        current_rot[2] + rand_polygon_rot_z_offset,
                        inst, a=True)
