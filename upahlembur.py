def baca_waktu(teks):
    """Mengubah teks '18.15' menjadi jam=18 dan menit=15."""
    bagian = teks.split(".")
    jam = int(bagian[0])
    menit = int(bagian[1])
    return jam, menit


def hitung_jam_lembur(jam_selesai, menit_selesai):
    """Menghitung berapa jam lembur sejak jam 16.30."""
    # Lembur mulai jam 16.30
    jam_mulai = 16
    menit_mulai = 30

    #jam dan menit menjadi menit
    total_menit_selesai = jam_selesai * 60 + menit_selesai
    total_menit_mulai = jam_mulai * 60 + menit_mulai

    # selisih menitnya
    selisih_menit = total_menit_selesai - total_menit_mulai

    # belum lewat 16.30, berarti tidak lembur
    if selisih_menit < 0:
        return 0

    # ubah menit menjadi jam penuh
    jam_lembur = selisih_menit // 60

    # maksimal yang dihitung 4 jam
    if jam_lembur > 4:
        jam_lembur = 4

    return jam_lembur


def hitung_upah_lembur(upah_perjam, jam_lembur):
    """Menghitung upah lembur berdasarkan jumlah jam lembur."""
    if jam_lembur == 0:
        return 0
    elif jam_lembur == 1:
        # 1 jam pertama: 1,5x
        return upah_perjam * 1.5
    elif jam_lembur == 2:
        # 1 jam pertama 1,5x + jam ke-2 2x
        return upah_perjam * 1.5 + upah_perjam * 2
    elif jam_lembur == 3:
        # 1,5x + 2x + 2x
        return upah_perjam * 1.5 + upah_perjam * 2 * 2
    else:
        # 4 jam: 1,5x + 2x + 2x + 3x
        return upah_perjam * 1.5 + upah_perjam * 2 * 2 + upah_perjam * 3


def format_rupiah(angka):
    """Mengubah 70000 menjadi 'Rp 70.000'."""
    angka = int(angka)
    teks = f"{angka:,}"
    teks = teks.replace(",", ".")
    return "Rp " + teks