from abc import abstractmethod

from ..base import VoxelDevice


class BaseFlipMount(VoxelDevice):
    """
    Base class for flip mount devices.
    """

    def __init__(self, id: str):
        """
        Initialize the BaseFlipMount object.

        :param id: Flip mount ID
        :type id: str
        """
        super().__init__(id)

    @property
    @abstractmethod
    def position(self) -> str | None:
        """
        Get the position of the flip mount.

        :return: Position of the flip mount
        :rtype: str | None
        """
        pass

    @position.setter
    @abstractmethod
    def position(self, position_name: str, wait=False):
        """
        Set the flip mount to a specific position.

        :param position_name: Position name
        :type position_name: str
        :param wait: Whether to wait for the flip mount to finish moving, defaults to False
        :type wait: bool, optional
        """
        pass

    @abstractmethod
    def toggle(self):
        """
        Toggle the flip mount position.
        """
        pass

    @abstractmethod
    def wait(self):
        """
        Wait for the flip mount to finish flipping.
        """
        pass

    @property
    @abstractmethod
    def flip_time_ms(self) -> int:
        """
        Get the time it takes to flip the mount in milliseconds.

        :return: Flip time in milliseconds
        :rtype: int
        """
        pass

    @flip_time_ms.setter
    @abstractmethod
    def flip_time_ms(self, time_ms: int):
        """
        Set the time it takes to flip the mount in milliseconds.

        :param time_ms: Flip time in milliseconds
        :type time_ms: int
        """
        pass
