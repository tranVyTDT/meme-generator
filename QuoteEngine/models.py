class QuoteModel:
    """ encapsulate the body and author of a Quote """

    def __init__(self, body, author):
        """ create a object of Quote model """
        self.body = body
        self.author = author
        
    def __str__(self):
        """ Present Quote model by a string """
        return f"body {self.body}, author {self.author} "