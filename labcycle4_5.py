class publisher:
    pass


class book(publisher):
    def __init__(self,title,author):
        self.T
        self.A

    def display(self):
        print("in book class")


class python(book):
    def __init__(self,price,no_pages):
        self.p=price
        self.n=no_pages

    def display(self):
        print("in class python")


py1=python(100,250)
py1.display()
