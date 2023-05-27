# 1. Wireshark: ICMP

## 1

1. IP-адрес моего хоста - это 192.168.1.103. IP-адрес хоста назначения - это 54.252.93.212.
<img width="1440" alt="1 1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/2e8d5f5d-48c8-405a-8ca1-0c40c5f58f92">

2. ICMP - это протокол сетевого уровня, а протоколы сетевого уровня не используют порты.

3. Для пакета на скриншоте ICMP-тип равен 8, а кодовый номер равен 0. В этом пакете ещё есть поля Checksum, Identifier (BE), Identifier (LE), Sequence Number (BE), Sequence Number (LE) и Timestamp. На поля контрольной суммы, порядкового номера и идентификатора приходится 2 + 4 + 4 = 10 байт.
<img width="1440" alt="1 3" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/983439d9-43d7-4d31-a92a-a2e9bc06d86d">

4. Для ответа ICMP-тип равен 0, а кодовый номер равен 0. В этом пакете ещё есть поля Checksum, Identifier (BE), Identifier (LE), Sequence Number (BE), Sequence Number (LE) и Timestamp. На поля контрольной суммы, порядкового номера и идентификатора приходится 2 + 4 + 4 = 10 байт.
<img width="1440" alt="1 4" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/2d9730a1-f959-4e33-b507-73a1485e4a17">

## 2

1. ICMP-пакет с эхо-запросом на скриншоте отличается от ICMP-пакетов с ping-запросами из задания 1 тем, что в нём данные занимают 64 байта вместо 48, отсутствует поле Timestamp и TTL не равен 64.
<img width="1440" alt="2 1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/2db3ea82-513f-45f8-9ea3-7052f916c450">

2. В ICMP-пакете с сообщением об ошибке присутствуют дополнительные поля Unused, Internet Protocol и ICMP. В поле Unused скорее всего ничего полезного не хранится. В полях Internet Protocol и ICMP продублирована иформация из соответствующего ICMP-запроса.
<img width="1440" alt="2 2" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/b02fee9f-e6a8-4fa7-9f31-bfe4f04db264">

3. У последних трёх ICMP-пакетов, полученных исходным хостом, отстутствуют дополнительные поля, а ICMP-тип равен 0 вместо 11. Это обусловлено тем, что эти пакеты являются ответами на ping, а не ошибками.
<img width="1440" alt="2 3" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/e10e1131-9a6e-4ed9-a8b0-98b2b55f38bf">

4. На скриншоте видно, что между запросами 7 и 8 есть значительная задержка. Маршрутизатор 104.44.43.236 находится в Швеции, а маршрутизатор 104.44.22.164 - в США.
<img width="1440" alt="2 4" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/9678f4b2-172a-4373-b705-2b6c785f3cf3">

# 3. Задачи

## 2

1. До одной потери будет отправлено $\frac{W}{2} + \alpha\frac{W}{2} + \alpha^2\frac{W}{2} + \dots + 2\frac{W}{2} = \frac{(2 \alpha - 1) W}{2 \alpha - 2}$ байт $\Rightarrow L = \frac{2 \alpha - 2}{(2 \alpha - 1) W}$.

2. Для увеличения размера окна с $\frac{W}{2}$ до $W$ требуется константное количество событий получения ACK-пакета, поэтому на это требуется одинаковое количество времени независимо от средней пропускной способности.
