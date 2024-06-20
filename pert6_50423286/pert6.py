from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

def main():
    global app, window, nama_textbox, ktp_textbox, alamat_textbox, barang_textbox
    app = QApplication([])

    window = QWidget()
    window.setGeometry(400, 200, 400, 300)
    window.setWindowTitle("Ujian AP2B - 50423286")

    layout = QVBoxLayout()
    layout.setSpacing(10)
    layout.setContentsMargins(20, 20, 20, 20)

    label_judul = QLabel("Masukkan Barang Belanjaan Anda: ")
    label_judul.setAlignment(Qt.AlignCenter)
    label_judul.setFont(QFont("Arial", 16, QFont.Bold))
    label_judul.setStyleSheet('color: #00215E')

    label_nama = QLabel("Nama: ")
    label_ktp = QLabel("KTP: ")
    label_alamat = QLabel("Alamat: ")
    label_barang = QLabel("Barang: ")

    labels = [label_nama, label_ktp, label_alamat, label_barang]
    for i in labels:
        i.setFont(QFont("Arial", 12, QFont.Bold))
        i.setStyleSheet('color: #00215E')

    nama_textbox = QLineEdit()
    ktp_textbox = QLineEdit()
    alamat_textbox = QLineEdit()
    barang_textbox = QLineEdit()

    nama_textbox.setPlaceholderText("Masukkan Nama Anda")
    ktp_textbox.setPlaceholderText("Masukkan No KTP Anda")
    alamat_textbox.setPlaceholderText("Masukkan Alamat Anda")
    barang_textbox.setPlaceholderText("Masukkan Barang Belanjaan Anda")

    textboxes = [nama_textbox, ktp_textbox, alamat_textbox, barang_textbox]
    for tbox in textboxes:
        tbox.setFont(QFont("Arial", 12, QFont.Bold))
        tbox.setStyleSheet('padding: 5px; border: .5px solid #FC4100; border-radius: 5px;')

    button_input = QPushButton("Input Data")
    button_input.setFont(QFont("Arial", 12, QFont.Bold))
    button_input.setStyleSheet('color: #FFFAE6; background-color: #FC4100; padding: 5px; border: 1px solid #FC4100; border-radius: 5px; font-weight: bold; margin-top: 5px;')
    button_input.clicked.connect(on_clicked)

    layout.addWidget(label_judul)
    layout.addWidget(label_nama)
    layout.addWidget(nama_textbox)
    layout.addWidget(label_ktp)
    layout.addWidget(ktp_textbox)
    layout.addWidget(label_alamat)
    layout.addWidget(alamat_textbox)
    layout.addWidget(label_barang)
    layout.addWidget(barang_textbox)
    layout.addWidget(button_input, alignment=Qt.AlignCenter)

    window.setLayout(layout)
    window.show()
    app.exec_()

def on_clicked():
    if nama_textbox.text() and ktp_textbox.text() and alamat_textbox.text():
        message = QMessageBox()
        message.setStyleSheet("background-color: #00215E; color: #FC4100")
        message.information(window, "Data diri", "Nama: " + nama_textbox.text() + "\nNPM: " + ktp_textbox.text() + "\nKelas: " + alamat_textbox.text() + "\nJurusan: " + barang_textbox.text() + "\nNo Hp: " + .text())

        nama_textbox.setText("")
        ktp_textbox.setText("")
        alamat_textbox.setText("")
        barang_textbox.setText("")
        .setText("")
    else :
        message = QMessageBox()
        message.setStyleSheet("background-color: #FC4100; color: #AF0404")
        message.warning(window, "Input Error", "Data tidak boleh kosong!")

if __name__ == '__main__':
    main()