from typing import Optional

from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/luas-lingkaran-kali-x/{r}/{x}")
def luas_lingkaran(r: int, x: int):
    if r and x:
        return {"r": r, "hasil": 22/7*r**2*x}
    return {"status": "error"}

@app.post("/hasil-kali-ganjil/")
def kali(a: Optional[int] = Form(...), b: Optional[int] = Form(...)):
    if a and b:
        hasil_kali = a*b
        if hasil_kali % 2 == 0:
            return {"status": "genap", "number": hasil_kali}
        return {"status": "ganjil", "number": hasil_kali}
    return {"status": "error"}

@app.post("/pangkat/")
def pangkat(a: Optional[int] = None, b: Optional[int] = None):
    if a and b:
        return {"a": a, "b": b, "pangkat-dua": a**b}
    return {"status": "error"}