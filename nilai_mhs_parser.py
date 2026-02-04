import os
import csv

def parse_csv_files(data_dir='data'):
    base = os.path.join(os.path.dirname(__file__), data_dir)
    if not os.path.isdir(base):
        return
    for fname in sorted(os.listdir(base)):
        if not fname.lower().endswith('.csv'):
            continue
        path = os.path.join(base, fname)
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            mata_kuliah = None
            pengajar = None
            kode_kelas = None
            
            for row in reader:
                row_data = row
                if row_data[0].strip() == 'Mata kuliah':
                    mata_kuliah = row_data[2].strip()
                    kode_kelas = row_data[8].strip()
                elif row_data[0].strip() == 'Pengajar':
                    pengajar = row_data[2].strip()
                elif row_data[0].strip().isdigit():
                    nim = row_data[1].strip()
                    nama = row_data[2].strip()
                    nilai = row_data[3].strip()
                    nilai_angka = row_data[4].strip()
                    nilai_huruf = row_data[5].strip()
                    tahun_akademik = '2024-1'
                    
                    result_rows = [
                        nim, nama, nilai, nilai_angka, nilai_huruf,
                        mata_kuliah, pengajar, kode_kelas, tahun_akademik
                    ]

                    yield result_rows
                else:
                    continue

if __name__ == '__main__':
    headers = ['NIM', 'NAMA', 'NILAI', 'NILAI ANGKA', 'NILAI HURUF',
                'MATA KULIAH', 'PENGAJAR','KODE KELAS', 'TAHUN AKADEMIK']
    data_rows = []
    for data in parse_csv_files():
        data_rows.append(data)

    with open('output.csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(headers)
        writer.writerows(data_rows)