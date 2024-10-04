# setup_db.py

from main import app, db
import os

# Var olan veritabanı dosyasını silme (eğer varsa)
if os.path.exists("instance/diary.db"):
    os.remove("instance/diary.db")
    print("Eski veritabanı silindi.")
else:
    print("Veritabanı dosyası mevcut değil, oluşturulacak.")

# Uygulama bağlamını başlatma
app.app_context().push()

# Veritabanı tablolarını oluşturma
db.create_all()
print("Yeni veritabanı başarıyla oluşturuldu!")
