from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """ IngestorInterface """

    @staticmethod
    @abstractmethod
    def can_ingest(cls, path):
        """ check for a path can be ingested """
        

    @staticmethod
    @abstractmethod
    def parse(cls, path):
        """ parse a path get quote """
