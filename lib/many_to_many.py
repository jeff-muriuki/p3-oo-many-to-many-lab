class Author:
    all= []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value    

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts() ]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all= []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value    

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]    
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:
    all= []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author= author
        self.book= book
        self.date= date
        self.royalties= royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]








    