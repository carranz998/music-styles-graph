from neo4j import GraphDatabase
from utils.thread_safe_singleton import ThreadSafeSingleton


class DatabaseSession(metaclass=ThreadSafeSingleton):
    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        self.driver.close()
