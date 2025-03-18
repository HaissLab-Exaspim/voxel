import logging

from coherent_lasers.genesis_mx.commands import OperationMode
from coherent_lasers.genesis_mx.driver import GenesisMX

from voxel.descriptors.deliminated_property import DeliminatedProperty
from voxel.devices.laser.base import BaseLaser


class GenesisMXLaser(BaseLaser):
    """Genesis MX Laser device class."""

    def __init__(self, id: str, wavelength: int, maximum_power_mw: int) -> None:
        """Initialize the Genesis MX Laser.

        :param id: The serial ID of the laser.
        :type id: str
        :param wavelength: The wavelength of the laser in nanometers.
        :type wavelength: int
        :param maximum_power_mw: The maximum power of the laser in milliwatts.
        :type maximum_power_mw: int
        :raises ValueError: If the serial number does not match.
        """
        self.log = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        super().__init__(id)
        self._conn = id
        self._wavelength = wavelength
        type(self).power_setpoint_mw.maximum = maximum_power_mw
        self.enable()

    @property
    def _instance(self):
        _inst = getattr(self, "_inst", None)
        if _inst is None :
            try:
                self._inst = GenesisMX(serial=self._conn)
                assert self._inst.serial == self._conn
                assert self._inst.serial in self._inst._manager._serials.keys() # serial is in existing serial handles
                self._inst.mode = OperationMode.PHOTO
            except AssertionError:
                raise ValueError(f"Error initializing laser {self._conn}, serial number mismatch. Available ids are : {self._inst._manager._serials.keys()}")
        return self._inst

    @property
    def wavelength(self) -> int:
        """Get the wavelength of the laser.

        :return: The wavelength of the laser in nanometers.
        :rtype: int
        """
        return self._wavelength

    def enable(self) -> None:
        """Enable the laser."""
        self._instance.enable()

    def disable(self) -> None:
        """Disable the laser."""
        self._instance.disable()

    def close(self) -> None:
        """Close the connection to the laser."""
        self.disable()

    @property
    def power_mw(self) -> float:
        """Get the current power of the laser.

        :return: The current power of the laser in milliwatts.
        :rtype: float
        """
        return self._instance.power_mw

    @DeliminatedProperty(minimum=0, maximum=float("inf"))
    def power_setpoint_mw(self) -> float:
        """Get the power setpoint of the laser.

        :return: The power setpoint of the laser in milliwatts.
        :rtype: float
        """
        return self._instance.power_setpoint_mw

    @power_setpoint_mw.setter
    def power_setpoint_mw(self, value: float) -> None:
        """Set the power setpoint of the laser.

        :param value: The desired power setpoint in milliwatts.
        :type value: float
        """
        self.log.info(f"setting power to {value} mW")
        self._instance.power_mw = value

    @property
    def temperature_c(self) -> float:
        """Get the temperature of the laser.

        :return: The temperature of the laser in degrees Celsius.
        :rtype: float
        """
        return self._instance.temperature_c
