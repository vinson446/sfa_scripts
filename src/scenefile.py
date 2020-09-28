from pymel.core.system import Path
import re


class SceneFile(object):
    """An abstract representation of a Scene file."""
    def __init__(self, path):
        self.folder_path = Path()
        self.descriptor = 'main'
        self.task = None
        self.ver = 1
        self.ext = '.ma'
        self._init_from_path(path)

    @property
    def filename(self):
        pattern = "{descriptor}_{task}_v{ver:03d}{ext}"
        return pattern.format(descriptor=self.descriptor,
                              task=self.task,
                              ver=self.ver,
                              ext=self.ext)

    @property
    def path(self):
        return self.folder_path / self.filename

    def _init_from_path(self, path):
        descriptor, self.task, ver = re.split(r"\_", path)
        self.descriptor = descriptor[descriptor.rfind("/") + 1:]
        ver, ext = re.split(r"\.", ver)
        self.ver = int(ver.split("v")[-1])
        self.ext = "." + ext
        path = Path(path)
        self.folder_path = path.parent


scene_file = SceneFile("D:/sandbox/tank_model_v001.ma")
print(scene_file.folder_path)
print(scene_file.descriptor)
print(scene_file.task)
print(scene_file.ver)
print(scene_file.ext)
print(scene_file.filename)
print(scene_file.path)
