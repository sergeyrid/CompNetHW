# 1. Wireshark

1. Сообщения DHCP посылаются поверх протокола UDP.
<img width="1440" alt="1" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/23975977-f909-49b8-b840-fae937d1a29a">

2. Ethernet-адрес у моего хоста - это a0:78:17:87:f7:57.
<img width="1440" alt="2" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/99115b6e-c048-4bf5-b71e-ee69f8212789">

3. В наборе Request/ACK DHCP сообщений Transaction-ID принимает значение 0x35334103. Это поле нужно для идентификации ответов от сервера.
<img width="1440" alt="3" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/e2e0befc-74be-42a9-8c35-450883a7315e">

4. В инкапсулирующей IP-дейтаграмме DHCP сообщений используется исходный IP-адрес 0.0.0.0 и конечный IP-адрес 255.255.255.255.
<img width="1440" alt="4" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/e37b815e-9b8a-4bdc-8665-fc1350e4e0ff">

5. IP-адрес моего DHCP-сервера - это 192.168.1.1.
<img width="1440" alt="5" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/dea479f9-fd82-41f3-b842-031c3e2d55b6">

6. Срок аренды IP-адреса нужен, чтобы освободить адрес в случае, если по истечении срока аренда не будет продлена. В моём эксперименте длительность срока аренды равна двум часам.
<img width="1440" alt="6" src="https://github.com/sergeyrid/CompNetHW/assets/41862239/f963383f-0e08-4643-9f3f-e29e70a019a7">

# 3. Задачи

## 1

а) $Np(1-p)^{N-1} \to \max$

$(Np(1-p)^{N-1})' = 0$

$N(1-p)^{N-1} - N(N-1)p(1-p)^{N-2} = 0$

$p \neq 1,0 \Rightarrow (1-p) - (N-1)p = 0$

$p = \frac{1}{N}$

б) $\lim_{N \to \infty} N(\frac{1}{N})(1-\frac{1}{N})^{N-1} = \lim_{N \to \infty} (1-\frac{1}{N})^{N-1} = \frac{1}{e}$

## 2

$N := 4$ - количество активных узлов.

а) $P = p^1(1-p)^{N-1} = p(1-p)^3$

б) $P = (N - 1)(p^1(1-p)^{N-1}) = 3p(1-p)^3$

в) Пусть $P_i$ - вероятность того, что передача в $i$-м кванте - успешная.

$P = (1 - P_1)(1 - P_2)P_3 = (1 - Np(1-p)^{N-1})^2(Np(1-p)^{N-1}) =$

$= Np(1-p)^{N-1} + (Np(1-p)^{N-1})^3 - 2(Np(1-p)^{N-1})^2 = 4p(1-p)^3 + 64p^3(1-p)^9 - 32p^2(1-p)^6$

г) Эффективность равна $Np(1-p)^{N-1} = 4p(1-p)^3$

## 3

Пусть $F$ - суммарное количество бит, переданное в одном раунде опроса.

Тогда пропускная способность равна $\frac{F}{\frac{F}{R} + Nd} = \frac{1}{\frac{1}{R} + \frac{Nd}{F}} \to \max \Rightarrow F \to \max$

$F \leq QN \Rightarrow$ максимальная пропускная способность равна $\frac{1}{\frac{1}{R} + \frac{d}{Q}}$
