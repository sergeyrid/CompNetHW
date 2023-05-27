# 1. Wireshark. IP

1. IP-адрес моего компьютера - это 192.168.1.103.
<img width="1440" alt="1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/1a018078-f957-45e5-97b7-1d10526d99dc">

2. В поле протокола верхнего уровня IP-пакета указано ICMP.

3. В IP-заголовке 20 байт. Суммарная длина IP-заголовка равна 56 байт, значит полезная нагрузка равна 56 - 20 = 36 байт.

4.

a) В рамках одной последовательности ICMP-сообщений изменяются поля Identification, TTL и Header Checksum.

b) Остальные поля не меняются и не должны меняться. Поля Identification, TTL и Header Checksum должны изменяться.

c) Значения поля Identification изменяются без какой-либо видной мне закономерности.

<img width="1440" alt="4 1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/73fa96e7-c44a-42a1-b6a5-bd7585fa6c1f">
<img width="1440" alt="4 2" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/a567e5c4-bd48-4732-9013-f36672e475e4">

5. Для пакета на скриншоте значение в поле Identification равно 0x6d85, а значение в поле TTL равно 10.
<img width="1440" alt="5" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/781421f4-8a1b-4766-b172-308b4af8b1d6">

6. В сообщениях протокола ICMP, где содержится информация об истечении предписанного времени жизни, значение поля Identification изменяется, а значение поля TTL остаётся неизменным.
<img width="1440" alt="6 2" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/01d4dd88-7d6e-4ba9-9133-439c296e0961">
<img width="1440" alt="6 1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/5aa0c416-7430-47c1-866f-1264c045c681">

7. Для пакета на скриншоте значение в поле Identification равно 0xa40f, а значение в поле TTL равно 64.
<img width="1440" alt="6 2" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/01d4dd88-7d6e-4ba9-9133-439c296e0961">

8.

a) Первое сообщение протокола ICMP с эхо-запросом было фрагментировано между тремя дейтаграммами.

b) Во всех трёх фрагментах отличаются значения полей Fragment Offset и Header Checksum. У первых двух фрагментов совпадают, но у третьего отличаются значения полей Total Length и Flags.

<img width="1440" alt="8 1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/f0060610-f23f-49d9-9c20-b7097a4007ea">
<img width="1440" alt="8 2" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/c5ab546d-02ee-4528-860b-6d27f5c628d3">
<img width="1440" alt="8 3" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/151d0656-c39c-4517-a4fb-33f314869512">

# 2. Программирование


## 1

- Решение находится в папке `ping`

<img width="1440" alt="1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/406d3600-ace1-4f9f-80ab-aeff1ae554b9">
