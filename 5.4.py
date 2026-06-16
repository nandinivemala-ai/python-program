class book:
    def __init__(self,title):
        self.title=title

    def create_book_list():
        return[book("python 101"),book("AI"),book("data")]
        
books=book.create_book_list()

for b in books:
    print("book title:",b.title)
