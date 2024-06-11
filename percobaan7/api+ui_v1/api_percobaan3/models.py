from database import BaseDB
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Nullable, String, func, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from typing import List
from sqlalchemy import Table
from sqlalchemy import DateTime


#import List





class User(BaseDB):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    fullname = Column(String,nullable=False)
    nik = Column(String,nullable=False)
    email = Column(String, unique=True, index=True)
    telphone = Column(String,nullable=False)
    hashed_password = Column(String)
    
    pendaftarans = relationship("Pendaftaran", back_populates="user")
    

class Dokter(BaseDB):
    __tablename__ = "dokter"
    id_dokter = Column(Integer, primary_key=True)
    fullname = Column(String,unique=True)
    email = Column(String,nullable=False)
    telphone = Column(String,nullable=False)
    id_poliklinik = Column(Integer,nullable=False)
    keterangan = Column(String,nullable=False)
    rating = Column(Integer,nullable=False)
    harga = Column(Integer,nullable=False)
    
    
class Obat(BaseDB):
    __tablename__ = "obat"
    id_obat = Column(Integer, primary_key=True)
    nama = Column(String)
    jenis = Column(String)
    harga = Column(String)
    desc = Column(String)    

class Status(BaseDB):
    __tablename__ = 'status'
    id_status = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    status  = Column(String, nullable=False) # urutan: keranjang_kosong, belum_bayar, 
    #bayar, (pesanan_diterima atau pesanan_batal), pesanaan_diantar, pesanan_selesai
    timestamp = Column(DateTime, nullable=False, server_default=func.now(),index=True)
    
    # relasi_status = relationship("Pendaftaran", back_populates="relasi_status")

class Poliklinik(BaseDB):
    __tablename__ = 'poliklinik'
    id_poliklinik = Column(Integer, primary_key=True)
    nama_poliklinik = Column(String, nullable=False)

class Pendaftaran(BaseDB):
    __tablename__ = 'pendaftaran'
    id_pendaftaran = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('users.id'))  
    alamat = Column(String, nullable=False)
    id_dokter = Column(Integer, ForeignKey('dokter.id_dokter'), nullable=False)
    kategori = Column(String, nullable=False)
    keluhan = Column(String, nullable=False)
    no_antrian = Column(Integer, nullable=False)
    status_pembayaran = Column(String, nullable=False)
    status_antrian = Column(String, nullable=False)
    metode_pembayaran = Column(String, nullable=False)
    tanggal_pendaftaran = Column(Date, nullable=False, default=func.current_date())
    id_poliklinik = Column(Integer, ForeignKey('poliklinik.id_poliklinik'), nullable=False)
    
    user = relationship("User", back_populates="pendaftarans")