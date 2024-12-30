from abc import abstractmethod

from ..base import VoxelDevice


class BaseJoystick(VoxelDevice):
    """
    Base class for joystick devices.
    """

    @abstractmethod
    def stage_axes(self):
        """
        Get the stage axes controlled by the joystick.

        :return: List of stage axes
        :rtype: list
        """
        pass
    
    @abstractmethod
    def joystick_mapping(self):
        """
        Get the joystick mapping.

        :return: Joystick mapping
        :rtype: dict
        """
        pass
    
    @abstractmethod
    def close(self):
        """
        Close the joystick device.
        """
        pass