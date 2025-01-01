import logging
import time
from typing import Tuple

from voxel.devices.stage.base import BaseStage


class Stage(BaseStage):
    """
    Simulated stage class for handling simulated stage devices.
    """

    def __init__(self, hardware_axis: str, instrument_axis: str) -> None:
        """
        Initialize the Stage object.

        :param hardware_axis: Hardware axis
        :type hardware_axis: str
        :param instrument_axis: Instrument axis
        :type instrument_axis: str
        """
        self.log = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self._hardware_axis = hardware_axis.upper()
        self._instrument_axis = instrument_axis.lower()
        self.id = self.instrument_axis
        self._position_mm = 0
        self._speed = 1.0
        self._limits = [-10000, 10000]

    def move_relative_mm(self, position: float, wait: bool = False) -> None:
        """
        Move the stage relative to its current position.

        :param position: Position to move to in millimeters
        :type position: float
        :param wait: Whether to wait for the move to complete, defaults to False
        :type wait: bool, optional
        """
        w_text = "" if wait else "NOT "
        self.log.info(f"relative move by: {self.hardware_axis}={position} mm and {w_text}waiting.")
        move_time_s = position / self._speed
        self.move_end_time_s = time.time() + move_time_s
        self._position_mm += position
        if wait:
            while time.time() < self.move_end_time_s:
                time.sleep(0.01)

    def move_absolute_mm(self, position: float, wait: bool = False) -> None:
        """
        Move the stage to an absolute position.

        :param position: Position to move to in millimeters
        :type position: float
        :param wait: Whether to wait for the move to complete, defaults to False
        :type wait: bool, optional
        """
        w_text = "" if wait else "NOT "
        self.log.info(f"absolute move to: {self.hardware_axis}={position} mm and {w_text}waiting.")
        move_time_s = abs(self._position_mm - position) / self._speed
        self.move_end_time_s = time.time() + move_time_s
        self._position_mm = position
        if wait:
            while time.time() < self.move_end_time_s:
                time.sleep(0.01)

    def setup_stage_scan(
        self,
        fast_axis_start_position: float,
        slow_axis_start_position: float,
        slow_axis_stop_position: float,
        frame_count: int,
        frame_interval_um: float,
        strip_count: int,
        pattern: str,
        retrace_speed_percent: int,
    ) -> None:
        """
        Setup a stage scan.

        :param fast_axis_start_position: Fast axis start position
        :type fast_axis_start_position: float
        :param slow_axis_start_position: Slow axis start position
        :type slow_axis_start_position: float
        :param slow_axis_stop_position: Slow axis stop position
        :type slow_axis_stop_position: float
        :param frame_count: Frame count
        :type frame_count: int
        :param frame_interval_um: Frame interval in micrometers
        :type frame_interval_um: float
        :param strip_count: Strip count
        :type strip_count: int
        :param pattern: Scan pattern
        :type pattern: str
        :param retrace_speed_percent: Retrace speed percent
        :type retrace_speed_percent: int
        """
        self._position_mm = fast_axis_start_position

    def halts(self) -> None:
        """
        Halt the stage.
        """
        pass

    @property
    def limits_mm(self) -> Tuple[int, int]:
        """
        Get the limits of the stage in millimeters.

        :return: Limits in millimeters
        :rtype: tuple
        """
        return self._limits

    @property
    def position_mm(self) -> float:
        """
        Get the current position of the stage in millimeters.

        :return: Current position in millimeters
        :rtype: float
        """
        return self._position_mm

    @position_mm.setter
    def position_mm(self, value: float) -> None:
        """
        Set the current position of the stage in millimeters.

        :param value: Position in millimeters
        :type value: float
        """
        self._position_mm = value

    @property
    def speed_mm_s(self) -> float:
        """
        Get the speed of the stage in millimeters per second.

        :return: Speed in millimeters per second
        :rtype: float
        """
        return self._speed

    @speed_mm_s.setter
    def speed_mm_s(self, speed_mm_s: float) -> None:
        """
        Set the speed of the stage in millimeters per second.

        :param speed_mm_s: Speed in millimeters per second
        :type speed_mm_s: float
        """
        self._speed = speed_mm_s

    @property
    def hardware_axis(self) -> str:
        """
        Get the hardware axis.

        :return: Hardware axis
        :rtype: str
        """
        return self._hardware_axis

    @property
    def instrument_axis(self) -> str:
        """
        Get the instrument axis.

        :return: Instrument axis
        :rtype: str
        """
        return self._instrument_axis

    def is_axis_moving(self) -> bool:
        """
        Check if the axis is moving.

        :return: True if the axis is moving, False otherwise
        :rtype: bool
        """
        if time.time() < self.move_end_time_s:
            return True
        else:
            return False

    def zero_in_place(self) -> None:
        """
        Zero the stage in place.
        """
        self._position_mm = 0

    def close(self) -> None:
        """
        Close the stage.
        """
        pass
