from oxxius_laser import LBX, BoolVal
from serial import Serial
from sympy import Expr, solve, symbols
from typing import Union, Dict

from voxel.descriptors.deliminated_property import DeliminatedProperty
from voxel.devices.laser.base import BaseLaser

MODULATION_MODES = {
    "off": {"external_control_mode": BoolVal.OFF, "digital_modulation": BoolVal.OFF},
    "analog": {"external_control_mode": BoolVal.ON, "digital_modulation": BoolVal.OFF},
    "digital": {"external_control_mode": BoolVal.OFF, "digital_modulation": BoolVal.ON},
}


class OxxiusLBXLaser(BaseLaser):
    """
    OxxiusLBXLaser class for handling Oxxius LBX laser devices.
    """

    def __init__(
        self, id: str, port: Union[Serial, str], wavelength: int, prefix: str, coefficients: Dict[str, float]
    ) -> None:
        """
        Initialize the OxxiusLBXLaser object.

        :param id: Laser ID
        :type id: str
        :param port: Serial port for the laser
        :type port: Serial or str
        :param wavelength: Wavelength in nanometers
        :type wavelength: int
        :param prefix: Command prefix for the laser
        :type prefix: str
        :param coefficients: Coefficients for the power-current curve
        :type coefficients: dict
        """
        super().__init__(id)
        self._prefix = prefix
        self._inst = LBX(port, self._prefix)
        self._coefficients = coefficients
        self._wavelength = wavelength

    @property
    def wavelength(self) -> int:
        """
        Get the wavelength of the laser.

        :return: Wavelength in nanometers
        :rtype: int
        """
        return self._wavelength

    def enable(self) -> None:
        """
        Enable the laser.
        """
        self._inst.enable()

    def disable(self) -> None:
        """
        Disable the laser.
        """
        self._inst.disable()

    @property
    @DeliminatedProperty(minimum=0, maximum=lambda self: self.max_power)
    def power_setpoint_mw(self) -> float:
        """
        Get the power setpoint in milliwatts.

        :return: Power setpoint in milliwatts
        :rtype: float
        """
        if self._inst.constant_current == "ON":
            return int(round(self._coefficients_curve().subs(symbols("x"), self._inst.current_setpoint)))
        else:
            return int(self._inst.power_setpoint)

    @power_setpoint_mw.setter
    def power_setpoint_mw(self, value: Union[float, int]) -> None:
        """
        Set the power setpoint in milliwatts.

        :param value: Power setpoint in milliwatts
        :type value: float or int
        """
        if self._inst.constant_current == "ON":
            solutions = solve(self._coefficients_curve() - value)  # solutions for laser value
            for sol in solutions:
                if round(sol) in range(0, 101):
                    self._inst.current_setpoint = int(round(sol))  # setpoint must be integer
                    return
            # If no value exists, alert user
            self.log.error(f"Cannot set laser to {value}mW because no current percent correlates to {value} mW")
        else:
            self._inst.power_setpoint = value

    @property
    def modulation_mode(self) -> str:
        """
        Get the modulation mode.

        :return: Modulation mode
        :rtype: str
        """
        if self._inst.external_control_mode == "ON":
            return "analog"
        elif self._inst.digital_modulation == "ON":
            return "digital"
        else:
            return "off"

    @modulation_mode.setter
    def modulation_mode(self, value: str) -> None:
        """
        Set the modulation mode.

        :param value: Modulation mode
        :type value: str
        :raises ValueError: If the modulation mode is not valid
        """
        if value not in MODULATION_MODES.keys():
            raise ValueError("mode must be one of %r." % MODULATION_MODES.keys())
        for attribute, state in MODULATION_MODES[value].items():
            setattr(self._inst, attribute, state)
        self._set_max_power()

    def status(self) -> Dict[str, Union[str, float]]:
        """
        Get the status of the laser.

        :return: Status of the laser
        :rtype: dict
        """
        return self._inst.faults()

    def close(self) -> None:
        """
        Close the laser connection.
        """
        self._inst.close()

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

    def _coefficients_curve(self) -> Expr:
        """
        Get the power-current curve as a symbolic expression.

        :return: Power-current curve
        :rtype: Expr
        """
        x = symbols("x")
        func: Expr = x
        for order, co in self._coefficients.items():
            func = func + float(co) * x ** int(order)
        return func

    @property
    def max_power(self) -> float:
        """
        Get the maximum power in milliwatts.

        :return: Maximum power in milliwatts
        :rtype: float
        """
        if self._inst.constant_current == "ON":
            return int((round(self._coefficients_curve().subs(symbols("x"), 100), 1)))
        else:
            return self._inst.max_power

    def _set_max_power(self) -> None:
        """
        Set the maximum power.
        """
        type(self.power_setpoint_mw).maximum = self.max_power
