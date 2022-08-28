import neo4j
from neo4j import GraphDatabase
from utils.thread_safe_singleton import ThreadSafeSingleton


class DatabaseConnection(metaclass=ThreadSafeSingleton):
    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        if self.driver:
            self.driver.close()

    def execute_transaction(self, query: str) -> None:
        if self.driver:
            with self.driver.session() as session:
                session.write_transaction(self.__execute_query, query)

    def __execute_query(self, tx: neo4j.Transaction, query: str) -> None:
        tx.run(query)
