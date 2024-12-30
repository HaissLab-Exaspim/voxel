from abc import abstractmethod

from ..base import VoxelDevice


class BaseAOTF(VoxelDevice):
    """
    Base class for Acousto-Optic Tunable Filter (AOTF) devices.
    """

    @abstractmethod
    def enable_all(self):
        """
        Enable all channels of the AOTF.
        """
        pass

    @abstractmethod
    def disable_all(self):
        """
        Disable all channels of the AOTF.
        """
        pass

    @property
    @abstractmethod
    def frequency_hz(self):
        """
        Get the frequency in Hz for the AOTF.

        :return: The frequency in Hz.
        :rtype: dict
        """
        pass

    @frequency_hz.setter
    @abstractmethod
    def frequency_hz(self, channel: int, frequency_hz: dict):
        """
        Set the frequency in Hz for a specific channel of the AOTF.

        :param channel: The channel number.
        :type channel: int
        :param frequency_hz: The frequency in Hz.
        :type frequency_hz: dict
        """
        pass

    @property
    @abstractmethod
    def power_dbm(self):
        """
        Get the power in dBm for the AOTF.

        :return: The power in dBm.
        :rtype: dict
        """
        pass

    @power_dbm.setter
    @abstractmethod
    def power_dbm(self, channel: int, power_dbm: dict):
        """
        Set the power in dBm for a specific channel of the AOTF.

        :param channel: The channel number.
        :type channel: int
        :param power_dbm: The power in dBm.
        :type power_dbm: dict
        """
        pass

    @property
    @abstractmethod
    def blanking_mode(self):
        """
        Get the blanking mode of the AOTF.

        :return: The blanking mode.
        :rtype: str
        """
        pass

    @blanking_mode.setter
    @abstractmethod
    def blanking_mode(self, mode: str):
        """
        Set the blanking mode of the AOTF.

        :param mode: The blanking mode.
        :type mode: str
        """
        pass

    @property
    @abstractmethod
    def input_mode(self):
        """
        Get the input mode of the AOTF.

        :return: The input mode.
        :rtype: dict
        """
        pass

    @input_mode.setter
    @abstractmethod
    def input_mode(self, modes: dict):
        """
        Set the input mode of the AOTF.

        :param modes: The input modes.
        :type modes: dict
        """
        pass
