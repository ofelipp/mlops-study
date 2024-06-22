class DatabaseInterface:

    def create(self, register: object):
        raise NotImplementedError

    def read(self, query: str):
        raise NotImplementedError

    def update(self, register_id: int, new_register: object):
        raise NotImplementedError

    def delete(self, register_id: int):
        raise NotImplementedError
