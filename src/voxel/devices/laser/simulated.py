import logging
import random

from serial import Serial

from voxel.descriptors.deliminated_property import DeliminatedProperty
from voxel.devices.laser.base import BaseLaser

MODULATION_MODES = {
    "off": {"external_control_mode": "OFF", "digital_modulation": "OFF"},
    "analog": {"external_control_mode": "ON", "digital_modulation": "OFF"},
    "digital": {"external_control_mode": "OFF", "digital_modulation": "ON"},
}

MAX_POWER_MW = 100


class SimulatedLaser(BaseLaser):
    """
    SimulatedLaser class for handling simulated laser devices.
    """

    def __init__(self, id: str, wavelength: int, prefix: str = "", coefficients: dict = {}):
        """
        Initialize the SimulatedLaser object.

        :param id: Laser ID
        :type id: str
        :param wavelength: Wavelength in nanometers
        :type wavelength: int
        :param prefix: Prefix for the laser
        :type prefix: str, optional
        :param coefficients: Coefficients for the laser
        :type coefficients: dict, optional
        """
        super().__init__(id)
        self.log = logging.getLogger(__name__ + "." + self.__class__.__name__)

        self.prefix = prefix
        self.ser = Serial
        self._wavelength = wavelength
        self._simulated_power_setpoint_mw = 10.0
        self._max_power_mw = 100.0
        self._modulation_mode = "digital"
        self._temperature = 20.0
        self._cdrh = "ON"
        self._status = []

    def enable(self):
        """
        Enable the laser.
        """
        pass

    def disable(self):
        """
        Disable the laser.
        """
        pass

    @DeliminatedProperty(minimum=0, maximum=MAX_POWER_MW)
    def power_setpoint_mw(self):
        """
        Get the power setpoint in milliwatts.

        :return: Power setpoint in milliwatts
        :rtype: float
        """
        return self._simulated_power_setpoint_mw

    @power_setpoint_mw.setter
    def power_setpoint_mw(self, value: float):
        """
        Set the power setpoint in milliwatts.

        :param value: Power setpoint in milliwatts
        :type value: float
        """
        self._simulated_power_setpoint_mw = value

    @property
    def power_mw(self):
        """
        Get the current power in milliwatts.

        :return: Current power in milliwatts
        :rtype: float
        """
        return random.gauss(self._simulated_power_setpoint_mw, 0.1)

    @property
    def modulation_mode(self):
        """
        Get the modulation mode.

        :return: Modulation mode
        :rtype: str
        """
        return self._modulation_mode

    @modulation_mode.setter
    def modulation_mode(self, value: str):
        """
        Set the modulation mode.

        :param value: Modulation mode
        :type value: str
        :raises ValueError: If the modulation mode is not valid
        """
        if value not in MODULATION_MODES.keys():
            raise ValueError("mode must be one of %r." % MODULATION_MODES.keys())
        for attribute, state in MODULATION_MODES[value].items():
            setattr(self, attribute, state)
            self._modulation_mode = value

    @property
    def temperature_c(self):
        """
        Get the temperature of the laser in Celsius.

        :return: Temperature in Celsius
        :rtype: float
        """
        return self._temperature

    def status(self):
        """
        Get the status of the laser.

        :return: Status of the laser
        :rtype: list
        """
        return self._status

    @property
    def cdrh(self):
        """
        Get the CDRH status.

        :return: CDRH status
        :rtype: str
        """
        return self._cdrh

    @cdrh.setter
    def cdrh(self, value: str):
        """
        Set the CDRH status.

        :param value: CDRH status
        :type value: str
        """
        self._cdrh = value

    @property
    def wavelength(self) -> int:
        """
        Get the wavelength of the laser.

        :return: Wavelength in nanometers
        :rtype: int
        """
        return self._wavelength

    def close(self):
        """
        Close the laser connection.
        """
        pass
