# ==========================================
# 1. Variabel dan tipe data string
# ==========================================
device_id = "72e08x0"
print(device_id)
print(type(device_id))

# ==========================================
# 2. Daftar username sebagai list
# ==========================================
username_list = [
    "madebowa",
    "jnguyen",
    "tbecker",
    "nhersh",
    "redwards"
]

print(username_list)
print(type(username_list))

# ==========================================
# 3. Daftar username yang diperbarui
# ==========================================
username_list_2 = [
    "madebowa",
    "jnguyen",
    "tbecker",
    "nhersh",
    "redwards",
    "lpope"
]

print(username_list_2)

# ==========================================
# 4. Variabel integer
# ==========================================
max_logins = 3
login_attempts = 2

print(type(max_logins))
print(type(login_attempts))

# ==========================================
# 5. Perbandingan login
# ==========================================
print(login_attempts <= max_logins)  # True

login_attempts = 10
print(login_attempts <= max_logins)  # False

# ==========================================
# 6. Variabel boolean
# ==========================================
login_status = False
print(type(login_status))
