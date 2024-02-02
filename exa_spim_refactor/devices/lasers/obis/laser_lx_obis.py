from obis_laser import ObisLX, OperationalQuery, OperationalCmd
from devices.lasers.laser_base import Laser
import logging
from serial import Serial

MODULATION_MODES = {
    'off': 'CWP',
    'analog': 'ANALOG',
    'digital': 'DIGITAL',
    'mixed': 'MIXED'
}


class LaserLXObis(ObisLX, Laser):

    def __init__(self, port: Serial or str, prefix: str = None):
        """Communicate with specific LBX laser in L6CC Combiner box.

                :param port: comm port for lasers.
                :param prefix: prefix specic to laser.
                """
        self.log = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.prefix = prefix
        super(ObisLX, self).__init__(port, self.prefix)
        # inherit from laser device_widgets class

    @property
    def power_setpoint_mw(self):
        return self.power_setpoint

    @power_setpoint_mw.setter
    def power_setpoint_mw(self, value: float or int):
        self.power_setpoint = value

    @property
    def max_power_mw(self):
        return self.max_power

    @property
    def modulation_mode(self):
        mode = self._readcmd(OperationalQuery.OPERATING_MODE)
        for key, value in MODULATION_MODES.items():
            if mode == value:
                return key
        return self.log.error(f'Returned {mode}')

    @modulation_mode.setter
    def modulation_mode(self, mode: str):
        if mode not in MODULATION_MODES.keys():
            raise ValueError("mode must be one of %r." % MODULATION_MODES.keys())
        if MODULATION_MODES[mode] == 'CWP':
            self._writecmd(OperationalCmd.MODE_INTERNAL_CW, MODULATION_MODES[mode])
        else:
            self._writecmd(OperationalCmd.MODE_EXTERNAL, MODULATION_MODES[mode])

    def status(self):
        return self.get_system_status()