import logging
from abc import abstractmethod

import numpy


class BaseDownSample:
    """
    Base class for image downsampling.
    """

    def __init__(self, binning: int) -> None:
        """
        Module for handling downsampling processes.

        :param binning: The binning factor for downsampling.
        :type binning: int
        """

        self._binning = binning
        self.log = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    @abstractmethod
    def run(self, method, image: numpy.array):
        """
        Run function for image downsampling.

        :param image: Input image
        :type image: numpy.array
        """
        pass
