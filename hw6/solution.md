# 1. Wireshark: UDP

1. UDP-заголовок содержит 4 поля: Source Port, Destination Port, Length и Checksum.
2. Длина каждого поля заголовка составляет 2 байта.
3. Значение в поле Length - это длина датаграммы.
4. Максимальная длина пакета равна 65535, так как она записывается двумя байтами. При этом в эту длину также включена длина заголовка, равная 8 байтам, поэтому на полезную нагрузку остаётся максимум 65527 байт.
5. Количество портов записывается двумя байтами, поэтому их может быть максимум 65535.
6. Номер протокола UDP - 17 в десятичной системе и 11 в шестнадцатиричной.
7. Номера портов отправителя и получателя в ответе являются перестановкой номеров этих портов в запросе.

<img width="1440" alt="udp1" src="https://user-images.githubusercontent.com/41862239/230461682-44a5b958-3cd7-406a-a129-a8e9fe06f70d.png">
<img width="1440" alt="udp2" src="https://user-images.githubusercontent.com/41862239/230461688-5c9ab2fa-c878-406b-bebe-bc91d49ca083.png">
<img width="1440" alt="udp3" src="https://user-images.githubusercontent.com/41862239/230463121-34ffb52a-8887-4046-b1e1-f230e95d63fe.png">


# 2. Программирование. FTP

1.

<img width="1440" alt="filezilla.png" src="https://user-images.githubusercontent.com/41862239/230449666-7dfb5280-c1b5-435e-b6ba-6d718f19b1ef.png">

2. Решение находится в файле `ftp.py`.
3. Решение находится в файле `ftp_gui.py`.
