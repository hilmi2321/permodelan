import streamlit as st
import pandas as pd

def mcg_to_uniform(a, m, seed, n):
    """
    Fungsi untuk menghasilkan n bilangan acak menggunakan 
    Multiplicative Congruential Generator (MCG).

    Parameters:
    a (int): Pengali
    m (int): Modulus
    seed (int): Nilai awal (seed)
    n (int): Jumlah bilangan acak yang ingin dihasilkan

    Returns:
    list: Daftar bilangan acak yang dihasilkan
    list: Daftar nilai perulangan X
    """
    # Inisialisasi daftar untuk menyimpan bilangan acak dan nilai perulangan X
    random_numbers = []
    xm = [seed]
    random_variable = []
    
    # Inisialisasi nilai awal
    X = seed
    
    for _ in range(n):
        # Hitung bilangan acak berikutnya
        X = (a * X) % m
        # Konversi bilangan acak menjadi rentang [0, 1)
        uniform_random = X / m
        # Konversi dari inisialisasi bilangan acak ke variabel acak
        variable = (2 * uniform_random / 5) ** 0.5
        # Simpan bilangan acak yang dihasilkan
        random_numbers.append(uniform_random)
        # Simpan nilai perulangan X
        xm.append(X)
        # Simpan perulangan variabel acak
        random_variable.append(variable)

    # Mengembalikan daftar bilangan acak dan daftar nilai perulangan X
    return random_numbers, xm , random_variable

# Contoh penggunaan
a = 123   # Pengali (contoh)
m = 2**27-1     # Modulus (contoh)
seed = 10122028    # Nilai awal (contoh)
n = 300      # Jumlah bilangan acak yang ingin dihasilkan

random_numbers, xm , random_variable = mcg_to_uniform(a, m, seed, n)
# Create DataFrame
data = {
    'i': range(1, n+1),
    'Zi': xm[:-1],
    'Zi(Random Integer Number Multiplicate)': [f"({a} * {xm_val}) mod {m}" for xm_val in xm[:-1]],
    'Ui(Uniform R.N)': [f"{xm_val} / {m} = {number:.4f}" for xm_val, number in zip(xm[1:], random_numbers)],
    'Xi': random_variable
}
df = pd.DataFrame(data)

# Convert DataFrame to HTML without index
html_table = df.to_html(index=False)

# Display HTML table
st.write(html_table, unsafe_allow_html=True)

