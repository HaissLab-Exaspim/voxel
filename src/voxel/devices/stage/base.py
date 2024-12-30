from abc import abstractmethod

from ..base import VoxelDevice


class BaseStage(VoxelDevice):
    """
    Base class for stage devices.
    """

    @property
    @abstractmethod
    def hardware_axis(self):
        """
        Get the hardware axis.

        :raises ValueError: If the hardware axis is not set
        :return: Hardware axis
        :rtype: str
        """
        pass

    @property
    @abstractmethod
    def instrument_axis(self):
        """
        Get the instrument axis.

        :raises ValueError: If the instrument axis is not set
        :return: Instrument axis
        :rtype: str
        """
        pass

    @abstractmethod
    def move_relative_mm(self, position: float, wait: bool = True):
        """
        Move the stage relative to its current position.

        :param position: Position to move to in millimeters
        :type position: float
        :param wait: Whether to wait for the move to complete, defaults to True
        :type wait: bool, optional
        """
        pass

    @abstractmethod
    def move_absolute_mm(self, position: float, wait: bool = True):
        """
        Move the stage to an absolute position.

        :param position: Position to move to in millimeters
        :type position: float
        :param wait: Whether to wait for the move to complete, defaults to True
        :type wait: bool, optional
        """
        pass

    @abstractmethod
    def setup_step_shoot_scan(self, step_size_um: float):
        """
        Setup a step shoot scan.

        :param step_size_um: Step size in micrometers
        :type step_size_um: float
        """
        pass

    @abstractmethod
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
    ):
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
        pass

    @abstractmethod
    def start(self):
        """
        Start the stage.
        """
        pass

    @property
    @abstractmethod
    def position_mm(self) -> float:
        """
        Get the current position of the stage in millimeters.

        :return: Current position in millimeters
        :rtype: float
        """
        pass

    @property
    @abstractmethod
    def limits_mm(self):
        """
        Get the limits of the stage in millimeters.

        :return: Limits in millimeters
        :rtype: tuple
        """
        pass

    @property
    @abstractmethod
    def backlash_mm(self):
        """
        Get the backlash of the stage in millimeters.

        :return: Backlash in millimeters
        :rtype: float
        """
        pass

    @abstractmethod
    @backlash_mm.setter
    def backlash_mm(self, backlash: float):
        """
        Set the backlash of the stage in millimeters.

        :param backlash: Backlash in millimeters
        :type backlash: float
        """
        pass

    @property
    @abstractmethod
    def speed_mm_s(self):
        """
        Get the speed of the stage in millimeters per second.

        :return: Speed in millimeters per second
        :rtype: float
        """
        pass

    @abstractmethod
    @speed_mm_s.setter
    def speed_mm_s(self, speed: float):
        """
        Set the speed of the stage in millimeters per second.

        :param speed: Speed in millimeters per second
        :type speed: float
        """
        pass

    @abstractmethod
    @property
    def acceleration_ms(self):
        """
        Get the acceleration of the stage in millimeters per second squared.

        :return: Acceleration in millimeters per second squared
        :rtype: float
        """
        pass

    @abstractmethod
    @acceleration_ms.setter
    def acceleration_ms(self, acceleration: float):
        """
        Set the acceleration of the stage in millimeters per second squared.

        :param acceleration: Acceleration in millimeters per second squared
        :type acceleration: float
        """
        pass

    @property
    @abstractmethod
    def mode(self):
        """
        Get the mode of the stage.

        :return: Mode of the stage
        :rtype: int
        """
        pass

    @abstractmethod
    @mode.setter
    def mode(self, mode: int):
        """
        Set the mode of the stage.

        :param mode: Mode of the stage
        :type mode: int
        """
        pass

    @property
    @abstractmethod
    def joystick_mapping(self):
        """
        Get the joystick mapping.

        :return: Joystick mapping
        :rtype: str
        """
        pass

    @abstractmethod
    @joystick_mapping.setter
    def joystick_mapping(self, mapping: str):
        """
        Set the joystick mapping.

        :param mapping: Joystick mapping
        :type mapping: str
        """
        pass

    @property
    @abstractmethod
    def joystick_polarity(self):
        """
        Get the joystick polarity.

        :return: Joystick polarity
        :rtype: str
        """
        pass

    @abstractmethod
    @joystick_polarity.setter
    def joystick_polarity(self, polarity: str):
        """
        Set the joystick polarity.

        :param polarity: Joystick polarity
        :type polarity: str
        """
        pass

    @abstractmethod
    def lock_external_user_input(self):
        """
        Lock external user input.
        """
        pass

    @abstractmethod
    def unlock_external_user_input(self):
        """
        Unlock external user input.
        """
        pass

    @abstractmethod
    def is_axis_moving(self):
        """
        Check if the axis is moving.

        :return: True if the axis is moving, False otherwise
        :rtype: bool
        """
        pass

    @abstractmethod
    def zero_in_place(self):
        """
        Zero the stage in place.
        """
        pass

    @abstractmethod
    def log_metadata(self):
        """
        Log metadata.
        """
        pass

    @abstractmethod
    def halts(self):
        """
        Halt the stage.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close the stage.
        """
        pass
