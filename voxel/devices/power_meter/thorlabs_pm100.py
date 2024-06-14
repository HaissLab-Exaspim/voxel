from typing import Optional
import pyvisa as visa

from . import BasePowerMeter

class ThorlabsPowerMeter(BasePowerMeter):
    def __init__(self, id: str, conn: str) -> None:
        super().__init__(id)
        self.conn = conn
        self.inst: Optional[visa.resources.Resource] = None
        self.connect()

    def connect(self):
        rm = visa.ResourceManager()
        try:
            self.inst = rm.open_resource(self.conn)
            self.log.info(f"Connection to {self.conn} successful")
        except visa.VisaIOError as e:
            self.log.error(f"Could not connect to {self.conn}: {e}")
            raise
        except Exception as e:
            self.log.error(f"Unknown error: {e}")
            raise

    def disconnect(self) -> None:
        if self.inst is not None:
            self.inst.close()
            self.inst = None
            self.log.info(f"Disconnected from {self.conn}")
        else:
            self.log.warning(f"Already disconnected from {self.conn}")

    def _check_connection(self):
        if self.inst is None:
            raise Exception(f"Device {self.id} is not connected")

    @property
    def power_mw(self) -> float:
        self._check_connection()
        return float(self.inst.query("MEAS:POW?"))  * 1e3 # type: ignore

    @property
    def wavelength_nm(self) -> float:
        self._check_connection()
        return float(self.inst.query('SENS:CORR:WAV?')) # type: ignore

    @wavelength_nm.setter
    def wavelength_nm(self, wavelength: float) -> None:
        self._check_connection()
        self.inst.write(f"SENS:CORR:WAV {wavelength}") # type: ignore
        self.log.info(f"{self.id} - Set wavelength to {wavelength} nm")
