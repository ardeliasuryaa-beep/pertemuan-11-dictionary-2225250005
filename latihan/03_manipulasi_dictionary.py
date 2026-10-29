data = {
    "nama": "Ayu",
    "nilai": 85
}

# Menambahkan data kelas
data["kelas"] = "A"

# Mengubah nilai
data["nilai"] = 90
print("Setelah ditambah dan diubah:", data)

# Menghapus data kelas
data.pop("kelas")
print("Setelah kelas dihapus:", data)