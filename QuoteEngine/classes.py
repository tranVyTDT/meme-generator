import csv
import os
from docx import Document
from .interfaces import IngestorInterface
from .models import QuoteModel



class TextIngestor(IngestorInterface):
    """ Ingest text file """

    def can_ingest(path):
        """ Check for given a text file path, is the file exist """
        return os.path.exists(path)
    
    def parse(path):
        """ 
        Perform parse a txt file path 
        
        Args:
            path(str): path of a file
        
        Returns:
            list[QuoteModel]
        """
        quote_models = []
        with open(path) as f:
            for line in f:
                body, author = line.split("-")
                quote_models.append(QuoteModel(body, author))
        return quote_models

class CSVIngestor(IngestorInterface):
    """ Ingest csv file """

    def can_ingest(path):
        """ Check for given a csv file path, is the file exist """
        return os.path.exists(path)

    def parse(path):
        """ 
        Perform parse a csv file path 
        
        Args:
            path(str): path of a file
        
        Returns:
            list[QuoteModel]
        """
        quote_models = []
        with open(path) as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            
            for row in csv_reader:
                quote_models.append(QuoteModel(row[0], row[1]))
        return quote_models


class PDFIngestor(IngestorInterface):
    """ ingest pdf file """

    def can_ingest(path):
        """ Check for given a pdf file path, is the file exist """
        return os.path.exists(path)



class DocxIngestor(IngestorInterface):
    """ ingest docx file """

    def can_ingest(path):
        """ Check for given a docx file path, is the file exist """
        return os.path.exists(path)

    def parse(path):
        """ 
        Perform parse a docx file path 
        
        Args:
            path(str): path of a file
        
        Returns:
            list[QuoteModel]
        """
        doc = Document(path)
        quote_models = []
        for paragraph in doc.paragraphs:
            try:
                text = paragraph.text
                body, author = text.split("-")
                quote_models.append(QuoteModel(body, author))
            except ValueError: pass
        return quote_models
    

class Ingestor(IngestorInterface):
    """ ingest file """

    def can_ingest(path):
        """ Check for given a file path, is the file exist """
        return True if os.path.exists(path) else False

    def parse(path):
        """ select corresponding Ingestor class with the path """
        if "txt" in path[-4:]:
            return TextIngestor.parse(path)
        elif "csv" in path[-4:]:
            return CSVIngestor.parse(path)
        elif "docx" in path[-4:]:
            return DocxIngestor.parse(path)
        if "pdf" in path[-4:]:
            return PDFIngestor.parse(path)