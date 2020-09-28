import logging

import pymel.core as pmc
from pymel.core.system import Path

log = logging.getLogger(__name__)


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

    def save(self):
        """Saves the scene file.

        Returns:
            Path: The path to the scene file if successful
        """
        try:
            return pmc.system.saveAs(self.path)
        except RuntimeError as err:
            log.warning("Missing directories in path. Creating directories...")
            self.folder_path.makedirs_p()
            return pmc.system.saveAs(self.path)
