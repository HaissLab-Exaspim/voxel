from oxxius_laser import LCX
from serial import Serial

from voxel.descriptors.deliminated_property import DeliminatedProperty
from voxel.devices.laser.base import BaseLaser


class OxxiusLCXLaser(BaseLaser):
    """
    OxxiusLCXLaser class for handling Oxxius LCX laser devices.
    """

    def __init__(self, id: str, wavelength: int, port: Serial or str, prefix: str):
        """
        Initialize the OxxiusLCXLaser object.

        :param id: Laser ID
        :type id: str
        :param wavelength: Wavelength in nanometers
        :type wavelength: int
        :param port: Serial port for the laser
        :type port: Serial or str
        :param prefix: Command prefix for the laser
        :type prefix: str
        """
        super().__init__(id)
        self._prefix = prefix
        self._inst = LCX(port, self._prefix)
        self._wavelength = wavelength

    def enable(self):
        """
        Enable the laser.
        """
        self._inst.enable()

    def disable(self):
        """
        Disable the laser.
        """
        self._inst.disable()

    @property
    def wavelength(self) -> int:
        """
        Get the wavelength of the laser.

        :return: Wavelength in nanometers
        :rtype: int
        """
        return self._wavelength

    @DeliminatedProperty(minimum=0, maximum=lambda self: self._inst.max_power)
    def power_setpoint_mw(self):
        """
        Get the power setpoint in milliwatts.

        :return: Power setpoint in milliwatts
        :rtype: float
        """
        return float(self._inst.power_setpoint)

    @power_setpoint_mw.setter
    def power_setpoint_mw(self, value: float | int):
        """
        Set the power setpoint in milliwatts.

        :param value: Power setpoint in milliwatts
        :type value: float | int
        """
        self._inst.power_setpoint = value

    @property
    def power_mw(self) -> float:
        """
        Get the current power in milliwatts.

        :return: Current power in milliwatts
        :rtype: float
        """
        return self._inst.power

    @property
    def temperature_c(self) -> float:
        """
        Get the temperature of the laser in Celsius.

        :return: Temperature in Celsius
        :rtype: float
        """
        return self._inst.temperature

    def status(self):
        """
        Get the status of the laser.

        :return: Status of the laser
        :rtype: dict
        """
        return self._inst.get_system_status()

    def close(self):
        """
        Close the laser connection.
        """
        self.disable()
        if self._inst.ser.is_open:
            self._inst.ser.close()
