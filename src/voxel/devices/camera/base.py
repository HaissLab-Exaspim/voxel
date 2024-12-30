from abc import abstractmethod

from ..base import VoxelDevice


class BaseCamera(VoxelDevice):
    """
    Base class for camera devices.
    """

    @property
    @abstractmethod
    def exposure_time_ms(self):
        """
        Get the exposure time in milliseconds.

        :return: The exposure time in milliseconds.
        :rtype: int
        """
        pass

    @exposure_time_ms.setter
    @abstractmethod
    def exposure_time_ms(self, value):
        """
        Set the exposure time in milliseconds.

        :param value: The exposure time in milliseconds.
        :type value: int
        """
        pass

    @property
    @abstractmethod
    def width_px(self):
        """
        Get the width in pixels.

        :return: The width in pixels.
        :rtype: int
        """
        pass

    @width_px.setter
    @abstractmethod
    def width_px(self, value):
        """
        Set the width in pixels.

        :param value: The width in pixels.
        :type value: int
        """
        pass

    @property
    @abstractmethod
    def width_offset_px(self):
        """
        Get the width offset in pixels.

        :return: The width offset in pixels.
        :rtype: int
        """
        pass

    @width_offset_px.setter
    @abstractmethod
    def width_offset_px(self, value):
        """
        Set the width offset in pixels.

        :param value: The width offset in pixels.
        :type value: int
        """
        pass

    @property
    @abstractmethod
    def height_px(self):
        """
        Get the height in pixels.

        :return: The height in pixels.
        :rtype: int
        """
        pass

    @height_px.setter
    @abstractmethod
    def height_px(self, value):
        """
        Set the height in pixels.

        :param value: The height in pixels.
        :type value: int
        """
        pass

    @property
    @abstractmethod
    def height_offset_px(self):
        """
        Get the height offset in pixels.

        :return: The height offset in pixels.
        :rtype: int
        """
        pass

    @height_offset_px.setter
    @abstractmethod
    def height_offset_px(self, value):
        """
        Set the height offset in pixels.

        :param value: The height offset in pixels.
        :type value: int
        """
        pass

    @property
    @abstractmethod
    def pixel_type(self):
        """
        Get the pixel type.

        :return: The pixel type.
        :rtype: str
        """
        pass

    @pixel_type.setter
    @abstractmethod
    def pixel_type(self, value):
        """
        Set the pixel type.

        :param value: The pixel type.
        :type value: str
        """
        pass

    @property
    @abstractmethod
    def bit_packing_mode(self):
        """
        Get the bit packing mode.

        :return: The bit packing mode.
        :rtype: str
        """
        pass

    @bit_packing_mode.setter
    @abstractmethod
    def bit_packing_mode(self, value):
        """
        Set the bit packing mode.

        :param value: The bit packing mode.
        :type value: str
        """
        pass

    @property
    @abstractmethod
    def line_interval_us(self):
        """
        Get the line interval in microseconds.

        :return: The line interval in microseconds.
        :rtype: int
        """
        pass

    @property
    @abstractmethod
    def trigger(self):
        """
        Get the trigger mode.

        :return: The trigger mode.
        :rtype: str
        """
        pass

    @trigger.setter
    @abstractmethod
    def trigger(self, value):
        """
        Set the trigger mode.

        :param value: The trigger mode.
        :type value: str
        """
        pass

    @property
    @abstractmethod
    def binning(self):
        """
        Get the binning mode.

        :return: The binning mode.
        :rtype: str
        """
        pass

    @binning.setter
    @abstractmethod
    def binning(self, value):
        """
        Set the binning mode.

        :param value: The binning mode.
        :type value: str
        """
        pass

    @property
    @abstractmethod
    def sensor_width_px(self):
        """
        Get the sensor width in pixels.

        :return: The sensor width in pixels.
        :rtype: int
        """
        pass

    @property
    @abstractmethod
    def sensor_height_px(self):
        """
        Get the sensor height in pixels.

        :return: The sensor height in pixels.
        :rtype: int
        """
        pass

    @property
    @abstractmethod
    def frame_time_ms(self):
        """
        Get the frame time in milliseconds.

        :return: The frame time in milliseconds.
        :rtype: int
        """
        pass

    @property
    @abstractmethod
    def mainboard_temperature_c(self):
        """
        Get the mainboard temperature in Celsius.

        :return: The mainboard temperature in Celsius.
        :rtype: float
        """
        pass

    @property
    @abstractmethod
    def sensor_temperature_c(self):
        """
        Get the sensor temperature in Celsius.

        :return: The sensor temperature in Celsius.
        :rtype: float
        """
        pass

    @property
    @abstractmethod
    def readout_mode(self):
        """
        Get the readout mode.

        :return: The readout mode.
        :rtype: str
        """
        pass

    @property
    @abstractmethod
    def latest_frame(self):
        """
        Get the latest frame.

        :return: The latest frame.
        :rtype: np.ndarray
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Reset the camera.
        """
        pass

    @abstractmethod
    def prepare(self):
        """
        Prepare the camera for acquisition.
        """
        pass

    @abstractmethod
    def start(self):
        """
        Start the camera acquisition.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stop the camera acquisition.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close the camera and release resources.
        """
        pass

    @abstractmethod
    def grab_frame(self):
        """
        Grab a frame from the camera.

        :return: The grabbed frame.
        :rtype: np.ndarray
        """
        pass

    @abstractmethod
    def signal_acquisition_state(self):
        """
        Signal the acquisition state of the camera.
        """
        pass

    @abstractmethod
    def log_metadata(self):
        """
        Log the metadata of the camera.
        """
        pass

    @abstractmethod
    def abort(self):
        """
        Abort the camera acquisition.
        """
        pass
