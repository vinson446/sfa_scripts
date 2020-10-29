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

    def _init_polygon_rot(self):
        self.polygon_min_x_rot = 0
        self.polygon_max_x_rot = 0
        self.polygon_min_y_rot = 0
        self.polygon_max_y_rot = 0
        self.polygon_min_z_rot = 0
        self.polygon_max_z_rot = 0

    def create_ui(self):
        self.title_lbl = QtWidgets.QLabel("Scatter Tool")
        self.title_lbl.setStyleSheet("font: bold 20px")
        self.header_rand_rot_lay = self._create_header_rand_rot_ui()
        self.rand_rot_lay = self._create_rand_rot_ui()
        self.scatter_lay = self._create_scatter_ui()
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.main_lay.addLayout(self.header_rand_rot_lay)
        self.main_lay.addLayout(self.rand_rot_lay)
        self.main_lay.addLayout(self.scatter_lay)
        self.main_lay.addStretch()
        self.setLayout(self.main_lay)

    def _create_header_rand_rot_ui(self):
        layout = QtWidgets.QGridLayout()
        self.descriptor_header_lbl = QtWidgets.QLabel("Rotation")
        self.descriptor_header_lbl.setStyleSheet("font: bold")
        layout.addWidget(self.descriptor_header_lbl, 0, 0)
        return layout

    def _create_rand_rot_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.random_rot_min_x_lbl = QtWidgets.QLabel("X Min")
        self.random_rot_min_x_le = QtWidgets.QLineEdit()
        self.random_rot_max_x_lbl = QtWidgets.QLabel("X Max")
        self.random_rot_max_x_le = QtWidgets.QLineEdit()
        self.random_rot_min_y_lbl = QtWidgets.QLabel("Y Min")
        self.random_rot_min_y_le = QtWidgets.QLineEdit()
        self.random_rot_max_y_lbl = QtWidgets.QLabel("Y Max")
        self.random_rot_max_y_le = QtWidgets.QLineEdit()
        self.random_rot_min_z_lbl = QtWidgets.QLabel("Z Min")
        self.random_rot_min_z_le = QtWidgets.QLineEdit()
        self.random_rot_max_z_lbl = QtWidgets.QLabel("Z Max")
        self.random_rot_max_z_le = QtWidgets.QLineEdit()
        self.random_rot_btn = QtWidgets.QPushButton("Rotate")
        layout.addWidget(self.random_rot_min_x_lbl)
        layout.addWidget(self.random_rot_min_x_le)
        layout.addWidget(self.random_rot_max_x_lbl)
        layout.addWidget(self.random_rot_max_x_le)
        layout.addWidget(self.random_rot_min_y_lbl)
        layout.addWidget(self.random_rot_min_y_le)
        layout.addWidget(self.random_rot_max_y_lbl)
        layout.addWidget(self.random_rot_max_y_le)
        layout.addWidget(self.random_rot_min_z_lbl)
        layout.addWidget(self.random_rot_min_z_le)
        layout.addWidget(self.random_rot_max_z_lbl)
        layout.addWidget(self.random_rot_max_z_le)
        layout.addWidget(self.random_rot_btn)
        return layout

    def _create_scatter_ui(self):
        layout = QtWidgets.QHBoxLayout()
        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        layout.addWidget(self.scatter_btn)
        return layout

    def create_connections(self):
        """Connect Signals and Slots"""
        self.random_rot_btn.clicked.connect(self.rand_polygon_rot)
        self.scatter_btn.clicked.connect(self.scatter_polygon_inst_on_vert)

    @QtCore.Slot()
    def scatter_polygon_inst_on_vert(self):
        """Scatter polygon instances on another object's vertices"""
        polygon_vert_list = cmds.ls(selection=True, fl=True)
        polygon_inst = polygon_vert_list[0]
        if cmds.objectType(polygon_inst) == 'transform':
            for inst in polygon_vert_list:
                vert_pos = cmds.xform(inst, q=True, ws=True, t=True)

                new_instance = cmds.instance(polygon_inst, n="polygon_inst")
                cmds.move(vert_pos[0], vert_pos[1], vert_pos[2],
                          new_instance)

        cmds.delete(polygon_vert_list[0], "polygon_inst")

    @QtCore.Slot()
    def rand_polygon_rot(self):
        polygon_inst_list = cmds.ls("polygon_inst*")
        for inst in polygon_inst_list:
            try:
                min_x_rot = int(self.random_rot_min_x_le.text())
                self.polygon_min_x_rot = min_x_rot
                max_x_rot = int(self.random_rot_max_x_le.text())
                self.polygon_max_x_rot = max_x_rot
            except ValueError:
                self.polygon_min_x_rot = 0
                self.polygon_max_x_rot = 0

            try:
                min_y_rot = int(self.random_rot_min_y_le.text())
                self.polygon_min_y_rot = min_y_rot
                max_y_rot = int(self.random_rot_max_y_le.text())
                self.polygon_max_y_rot = max_y_rot
            except ValueError:
                self.polygon_min_y_rot = 0
                self.polygon_max_y_rot = 0

            try:
                min_z_rot = int(self.random_rot_min_z_le.text())
                self.polygon_min_z_rot = min_z_rot
                max_z_rot = int(self.random_rot_max_z_le.text())
                self.polygon_max_z_rot = max_z_rot
            except ValueError:
                self.polygon_min_z_rot = 0
                self.polygon_max_z_rot = 0

            rand_polygon_rot_x = random.uniform(self.polygon_min_x_rot,
                                                self.polygon_max_x_rot)
            rand_polygon_rot_y = random.uniform(self.polygon_min_y_rot,
                                                self.polygon_max_y_rot)
            rand_polygon_rot_z = random.uniform(self.polygon_min_z_rot,
                                                self.polygon_max_z_rot)

            cmds.rotate(rand_polygon_rot_x, rand_polygon_rot_y,
                        rand_polygon_rot_z, inst, a=True, os=True)
