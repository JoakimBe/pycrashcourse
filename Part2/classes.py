# Define a class
class Book:

    def __init__(self, number_of_pages, page_weight):
        self.numberOfPages = number_of_pages
        self.pageWeight = page_weight

    name = "Name is not set"
    author = "Author is not set"
    editor = "Editor is not set"
    weightInfo = "{name} väger {weight}. Ramen är inte inkluderad i vikten"
    coverWeight = 0

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_editor(self, editor):
        self.editor = editor

    def book_weight(self):
        return self.numberOfPages * self.pageWeight


# Define a new class that inherits the parent class Book
class Cover(Book):

    def __init__(self, number_of_pages, page_weight, cover_weight):
        self.numberOfPages = number_of_pages
        self.pageWeight = page_weight
        self.cover_weight = cover_weight

    def total_weight(self):
        return self.book_weight()+self.cover_weight

    def book_summary(self):
        return {
            'name': self.name,
            'author': self.author,
            'editor': self.editor,
            'total_pages_weight': self.book_weight(),
            'total_book_page': self.total_weight()
        }

# # Create an instance of Book and feed it information about the book "Lord Of The Rings"
# # The instance is persistent throughout the application lifecycle and can be changed without
# # interference with other instances of Book
# lordOfTheRings = Book(480, 0.7)

# # Call the method set_name in the instance we created to set a name for the book.
# lordOfTheRings.set_name = "Sagan Om Ringen"
#
# # Create a new instance of Book, but this time we feed it information about another book.
# # We now have 2 instance of Book, both living their own lives and will not interfer with each other.
# theHobbit = Book(400, 0.6)
# theHobbit.set_name = "Hobbiten"
#
# # To prove my point, print info from both instances of Book
# print(lordOfTheRings.weightInfo.format(name=lordOfTheRings.name, weight=lordOfTheRings.book_weight()))
# print(theHobbit.weightInfo.format(name=theHobbit.name, weight=theHobbit.book_weight()))
#
# # Create an instance of the class Cover. Cover inherits the parent class Book.
# # The constructor input adds a third attribute, 10, which is the cover weight.
# lordOfTheRingsWithCover = Cover(480, 0.7, 10)
#
# # Call the methods total_weight and book_summary and save the returned information on two variables.
# bookTotalWeight = lordOfTheRingsWithCover.total_weight()
# bookSummary = lordOfTheRingsWithCover.book_summary()
#
# # Print information using the Cover instance and see that it makes use of
# # attrbutes and methods from both Book and Cover.
# print("Boken vägen {weight} , ramen inluderad".format(weight=bookTotalWeight))
# print(bookSummary)
