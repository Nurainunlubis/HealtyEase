from pydantic import BaseModel
from sqlalchemy import DateTime
from datetime import  date

# user
class UserDetailsNoPassword(BaseModel):
    username: str
    fullname: str
    nik: str
    email: str
    telphone: str

class UserBase(BaseModel):
    username: str 
    
class UserCreate(UserBase):
    password: str
    
class UserDetails(UserCreate):
    fullname : str
    nik : str
    email : str
    telphone : str


class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# dokter

class DokterBase(BaseModel):
    fullname :str
    email :str
    telphone :str
    spesialis :str
    keterangan :str
    rating :int
    img_name :str

class DokterCreate(DokterBase):
    pass

class Dokter(DokterBase):
    id: int
    class Config:
        orm_mode = True
        
    


# Obat

class ObatBase(BaseModel):
    nama : str
    jenis : str
    harga : str
    img_name : str
    desc : str

class ObatCreate(ObatBase):
    pass

class Obat(ObatCreate):
    id: int
    class Config:
        orm_mode = True

class PendaftaranCreate(BaseModel):
    id_user: int
    alamat: str
    id_dokter: int
    kategori: str
    keluhan: str
    metode_pembayaran: str
    id_poliklinik: int


class PendaftaranResponse(PendaftaranCreate):
    id_pendaftaran: int
    no_antrian: int
    status_pembayaran: str
    status_antrian: str
    tanggal_pendaftaran: date

    class Config:
        orm_mode = True
        
                
class StatusUpdate(BaseModel):
    status: str
    
class QueueResponse(BaseModel):
    status_antrian: str
    no_antrian: int
    fullname: str



class Token(BaseModel):
    access_token: str
    token_type: str
