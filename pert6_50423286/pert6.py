from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

def main():
    global app, window, nama_textbox, npm_textbox, kelas_textbox, jurusan_textbox, hp_textbox
    app = QApplication([])

    window = QWidget()
    window.setGeometry(400, 200, 400, 300)
    window.setWindowTitle("Pertemuan 6 - 50423286")

    layout = QVBoxLayout()
    layout.setSpacing(10)
    layout.setContentsMargins(20, 20, 20, 20)

    label_judul = QLabel("Masukkan data diri Anda: ")
    label_judul.setAlignment(Qt.AlignCenter)
    label_judul.setFont(QFont("Arial", 16, QFont.Bold))
    label_judul.setStyleSheet('color: #00215E')

    label_nama = QLabel("Nama: ")
    label_npm = QLabel("NPM: ")
    label_kelas = QLabel("Kelas: ")
    label_jurusan = QLabel("Jurusan: ")
    label_hp = QLabel("No Hp: ")

    labels = [label_nama, label_npm, label_kelas, label_jurusan, label_hp]
    for i in labels:
        i.setFont(QFont("Arial", 12, QFont.Bold))
        i.setStyleSheet('color: #00215E')

    nama_textbox = QLineEdit()
    npm_textbox = QLineEdit()
    kelas_textbox = QLineEdit()
    jurusan_textbox = QLineEdit()
    hp_textbox = QLineEdit()

    nama_textbox.setPlaceholderText("Masukkan nama, contoh: *Andi Budi")
    npm_textbox.setPlaceholderText("Masukkan npm, contoh: *50xxxxx")
    kelas_textbox.setPlaceholderText("Masukkan kelas, contoh: *1IA03 atau 1ia03")
    jurusan_textbox.setPlaceholderText("Masukkan jurusan, contoh: *Informatika")
    hp_textbox.setPlaceholderText("Masukkan no hp yang aktif, contoh: *08xxxxxxxx")

    textboxes = [nama_textbox, npm_textbox, kelas_textbox, jurusan_textbox, hp_textbox]
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
    layout.addWidget(label_npm)
    layout.addWidget(npm_textbox)
    layout.addWidget(label_kelas)
    layout.addWidget(kelas_textbox)
    layout.addWidget(label_jurusan)
    layout.addWidget(jurusan_textbox)
    layout.addWidget(label_hp)
    layout.addWidget(hp_textbox)
    layout.addWidget(button_input, alignment=Qt.AlignCenter)

    window.setLayout(layout)
    window.show()
    app.exec_()

def on_clicked():
    if nama_textbox.text() and npm_textbox.text() and kelas_textbox.text():
        message = QMessageBox()
        message.setStyleSheet("background-color: #00215E; color: #FC4100")
        message.information(window, "Data diri", "Nama: " + nama_textbox.text() + "\nNPM: " + npm_textbox.text() + "\nKelas: " + kelas_textbox.text() + "\nJurusan: " + jurusan_textbox.text() + "\nNo Hp: " + hp_textbox.text())

        nama_textbox.setText("")
        npm_textbox.setText("")
        kelas_textbox.setText("")
        jurusan_textbox.setText("")
        hp_textbox.setText("")
    else :
        message = QMessageBox()
        message.setStyleSheet("background-color: #FC4100; color: #AF0404")
        message.warning(window, "Input Error", "Data tidak boleh kosong!")

if __name__ == '__main__':
    main()