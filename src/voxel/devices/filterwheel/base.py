from abc import abstractmethod

from ..base import VoxelDevice


class BaseFilterWheel(VoxelDevice):
    """
    Base class for filter wheel devices.
    """

    def __init__(self):
        """
        Initialize the BaseFilterWheel object.
        """
        self.filter_list = list()

    @property
    @abstractmethod
    def filter(self):
        """
        Get the current filter.

        :return: Current filter name
        :rtype: str
        """
        pass

    @abstractmethod
    @filter.setter
    def filter(self, filter_name: str):
        """
        Set the current filter.

        :param filter_name: Filter name
        :type filter_name: str
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close the filter wheel device.
        """
        pass
