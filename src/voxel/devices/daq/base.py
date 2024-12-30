from abc import abstractmethod

from ..base import VoxelDevice


class BaseDAQ(VoxelDevice):
    """Base class for DAQ devices."""

    @abstractmethod
    def add_task(self, task_type: str, pulse_count=None):
        """
        Add a task to the DAQ.

        :param task_type: Type of the task ('ao', 'co', 'do')
        :type task_type: str
        :param pulse_count: Number of pulses for the task, defaults to None
        :type pulse_count: int, optional
        """
        pass

    @abstractmethod
    def timing_checks(self, task_type: str):
        """
        Perform timing checks for the task.

        :param task_type: Type of the task ('ao', 'co', 'do')
        :type task_type: str
        """
        pass

    @abstractmethod
    def generate_waveforms(self, task_type: str, wavelength: str):
        """
        Generate waveforms for the task.

        :param task_type: Type of the task ('ao', 'do')
        :type task_type: str
        :param wavelength: Wavelength for the waveform
        :type wavelength: str
        """
        pass

    @abstractmethod
    def write_ao_waveforms(self):
        """
        Write analog output waveforms to the DAQ.
        """
        pass

    @abstractmethod
    def write_do_waveforms(self):
        """
        Write digital output waveforms to the DAQ.
        """
        pass

    @abstractmethod
    def plot_waveforms_to_pdf(self):
        """
        Plot waveforms and optionally save to a PDF.
        """
        pass

    @abstractmethod
    def start(self):
        """
        Start all tasks.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stop all tasks.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close all tasks.
        """
        pass

    @abstractmethod
    def restart(self):
        """
        Restart all tasks.
        """
        pass

    @abstractmethod
    def wait_until_done_all(self, timeout=1.0):
        """
        Wait until all tasks are done.

        :param timeout: Timeout in seconds, defaults to 1.0
        :type timeout: float, optional
        """
        pass

    @abstractmethod
    def is_finished_all(self):
        """
        Check if all tasks are finished.

        :return: True if all tasks are finished, False otherwise
        :rtype: bool
        """
        pass
