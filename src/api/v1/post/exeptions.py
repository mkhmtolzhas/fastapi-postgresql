from fastapi import HTTPException

class PostExeption:
    class PostNotFound(HTTPException):
        def __init__(self):
            super().__init__(status_code=404, detail="Post not found")

    class PostAlreadyExists(HTTPException):
        def __init__(self):
            super().__init__(status_code=400, detail="Post already exists")

    
    