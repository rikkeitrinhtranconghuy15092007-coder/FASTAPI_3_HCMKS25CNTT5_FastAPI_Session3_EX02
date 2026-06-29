from fastapi import FastAPI

app = FastAPI()

# Dữ liệu sách với trạng thái is_available
books = [
    {"id": 1, "title": "Python Basic", "author": "Nguyen Van A", "category": "programming", "year": 2022, "is_available": True},
    {"id": 2, "title": "Web API Design", "author": "Tran Van B", "category": "web", "year": 2021, "is_available": False},
    {"id": 3, "title": "Database System", "author": "Le Minh C", "category": "database", "year": 2020, "is_available": True},
    {"id": 4, "title": "Clean Code", "author": "Le Anh D", "category": "programming", "year": 2008, "is_available": False},
]

# API 1: Lấy danh sách sách có thể mượn (is_available == True)
@app.get("/books/available")
def get_available_books():
    # Dùng List Comprehension để lọc
    return [book for book in books if book["is_available"] == True]

# API 2: Lấy danh sách sách đang được mượn (is_available == False)
@app.get("/books/borrowed")
def get_borrowed_books():
    # Dùng List Comprehension để lọc
    return [book for book in books if book["is_available"] == False]