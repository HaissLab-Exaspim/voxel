import logging

from voxel.devices.filter.base import BaseFilter
from voxel.devices.filterwheel.asi import FilterWheel


class Filter(BaseFilter):
    """
    Filter class for handling ASI filter devices.
    """
    def __init__(self, wheel: FilterWheel, id: str):
        """
        Initialize the Filter object.

        :param wheel: Filter wheel object
        :type wheel: FilterWheel
        :param id: Filter ID
        :type id: str
        """
        self.log = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.id = id
        self.wheel = wheel

    def enable(self):
        """
        Enable the filter device.
        """
        self.wheel.filter = self.id

    def close(self):
        """
        Close the filter device.
        """
        self.wheel.close()