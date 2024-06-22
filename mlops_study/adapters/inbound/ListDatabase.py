from fastapi import HTTPException
from http import HTTPStatus
from typing import Union, List

from mlops_study.ports.inbound.DatabaseInterface import DatabaseInterface


class ListDatabase(DatabaseInterface):

    def __init__(self):
        self.database = []

    def create(self, register: object):
        self.database.append(register)

    # TODO: Revisar
    def read(self, register_ids: List[int]) -> List[object]:
        if register_ids == ["*"]:
            return self.database

        register_positions = [
            self._get_index_from_register(register_id)
            for register_id in register_ids
        ]

        if None in register_positions:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"ID {register_ids[register_positions.index(None)]} not found"
            )

        return [self.database[position] for position in register_positions]

    # TODO: Revisar
    def update(self, register_id: int, new_register: object):
        register_position = self._get_index_from_register(register_id)

        if register_position is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="ID not found"
            )

        self.database[register_id] = new_register

    # TODO: Revisar
    def delete(self, register_id: int):
        register_position = self._get_index_from_register(register_id)

        if register_position is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="ID not found"
            )

        del self.database[register_id]

    def get_database_length(self) -> int:
        return len(self.database)

    def _get_index_from_register(self, register_id) -> Union[int, None]:
        index_list = [
            True if register.id == register_id else False
            for register in self.database
        ]

        if True not in index_list:
            return None

        return index_list.index(True)
