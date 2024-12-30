from abc import abstractmethod

from ..base import VoxelDevice


class BaseFilter(VoxelDevice):
    """
    Base class for filter devices.
    """
    @abstractmethod
    def enable(self):
        """
        Enable the filter device.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close the filter device.
        """
        pass