"""Base class for all voxel devices."""

import logging
from abc import ABC, abstractmethod


class VoxelDevice(ABC):
    """Base class for all voxel devices."""

    def __init__(self, id: str):
        """
        Initialize the VoxelDevice object.

        :param id: Device ID
        :type id: str
        """
        self.id = id
        self.log = logging.getLogger(f"{self.__class__.__name__}[{self.id}]")

    @abstractmethod
    def close(self):
        """
        Close the device.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the device.

        :return: String representation of the device
        :rtype: str
        """
        return f"{self.__class__.__name__}[{self.id}]"

    def __del__(self):
        """
        Close the device when the object is deleted.
        """
        self.close()
