from typing import Dict, Optional

from tigerasi.tiger_controller import TigerController

from voxel.devices.flip_mount.base import BaseFlipMount


class TigerFlipMount(BaseFlipMount):
    """
    ThorlabsFlipMount class for handling Thorlabs flip mount devices.
    """

    def __init__(self, axis: str, tigerbox: TigerController, positions: Dict[str, int]) -> None:
        """
        Initialize the ThorlabsFlipMount object.

        :param axis: Tiger axis
        :type axis: str
        :param tigerbox: TigerController object, defaults to None
        :type tigerbox: Optional[TigerController], optional
        :param positions: Dictionary of positions
        :type positions: dict
        :raises ValueError: If an invalid position is provided
        """
        self.id = f'tiger flip mount: axis = {axis}'
        self.axis = axis
        super().__init__(id)
        self._tigerbox = tigerbox
        self._positions = positions

    @property
    def position(self) -> Optional[str]:
        """
        Get the current position of the flip mount.
        :return: Current position of the flip mount
        :rtype: str | None
        """
        position = self._position
        return next((key for key, value in self._positions.items() if value == position), "Unknown")

    @position.setter
    def position(self, position_name: str) -> None:
        """
        Set the flip mount to a specific position.

        :param position_name: Position name
        :type position_name: str
        """
        if position_name not in self._positions:
            raise ValueError(f"Invalid position {position_name}. Valid positions are {list(self._positions.keys())}")
        self.tigerbox.move_absolute(**{self.axis: self._positions[position_name]}, wait=True)
        self.log.info(f"Flip mount {self.id} moved to position {position_name}")
