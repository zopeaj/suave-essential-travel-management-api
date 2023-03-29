from pydantic import BaseModel, EmailStr

class UserDatabase(BaseModel):
    id: int
    password: Optional[str] = NONE
    email: EmailStr

class UserResponseDTO(BaseModel):
    email: EmailStr
    name: Optional[str]

class UserCreateDTO(BaseModel):
    name: Optional[str]
    email: Optional[str]
    id: int

class User(BaseModel):
    name: Optional[str]
    email: Optional[str]
    id: int

