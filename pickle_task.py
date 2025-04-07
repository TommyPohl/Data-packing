import pickle

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year



b1 = Book("lotr", "tolkien", 1973)
b2 = Book("dragonlance", "weiss", 1999)


raw_data = b1, b2

with open("books.pkl", "wb") as f:
    pickle.dump(raw_data, f)


with open("books.pkl", "rb") as f:
    data = pickle.load(f)


print(data)