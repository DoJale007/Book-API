from fastapi import FastAPI, Body


app = FastAPI()


BOOKS = [
    {
        "title": "Weather & Climate",
        "author": "Professor Kwadwo Owusu",
        "category": "Physical Geography",
    },
    {
        "title": "Principles & Methods of Cartography",
        "author": "Professor Gilbert Yiran",
        "category": "Cartography",
    },
    {
        "title": "Map Projections",
        "author": "Professor Alex Barimah Owusu",
        "category": "RS/GIS",
    },
    {
        "title": "Soil Survey in Ghana",
        "author": "Dr. Peter Blison Obour",
        "category": "Physical Geography",
    },
    {
        "title": "Geospatial Intelligence",
        "author": "Professor Alex Barimah Owusu",
        "category": "RS/GIS",
    },
    {
        "title": "Environmental Hydrology",
        "author": "Dr. George Owusu",
        "category": "Physical Geography",
    },
    {
        "title": "Industrialization in Ghana",
        "author": "Dr. Isaac Arthur",
        "category": "Human Geography",
    },
]


@app.get("/")
async def read_root():
    return {"Message": "Welcome to GeoBooks API"}


@app.get("/books")
async def get_library():
    return BOOKS


@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book_title.casefold() == book.get("title").casefold():
            return book


@app.get("/books/")
async def read_category_by_query(book_category: str):
    books_to_return = []
    for book in BOOKS:
        if book_category.casefold() == book.get("category").casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_new_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"Message": "Book Added Successfully."}


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book
    return {"Message": "Book updated Successfully"}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"Message": "Book Deleted Successfully"}

    return {"Message": "Book Not Found"}


@app.get("/books/by_author/{book_author}")
async def get_all_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
