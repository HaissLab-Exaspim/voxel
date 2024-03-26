from oxxius_laser import LCX
from voxel.devices.lasers.base import BaseLaser
import logging
from serial import Serial

class LaserLCXOxxius(LCX, BaseLaser):

    def __init__(self,  port: Serial or str, prefix:str):
        """Communicate with specific LBX laser in L6CC Combiner box.

                :param port: comm port for lasers.
                :param prefix: prefix specic to laser.
                """
        self.log = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.port = port
        self.prefix = prefix
        super(LCX, self).__init__(port, self.prefix)
        # inherit from laser device_widgets class

    @property
    def power_setpoint_mw(self):
        return float(self.power_setpoint)

    @power_setpoint_mw.setter
    def power_setpoint_mw(self, value: float or int):
        print('power setting to ', value)
        self.power_setpoint = value
        print('power set to ', self.power_setpoint)

    @property
    def max_power_mw(self):
        return float(self.max_power)

    @property
    def modulation_mode(self):
        raise AttributeError

    def status(self):
        return self.status()

    def cdrh(self):
        raise AttributeError

    def close(self):
        self.disable()
        if self.port.is_open:
            self.port.close()


