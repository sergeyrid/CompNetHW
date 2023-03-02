# 1. Программирование

Решение находится в файле `app.py`.

<img width="1440" alt="GET1" src="https://user-images.githubusercontent.com/41862239/222445370-d74d300e-1e1f-431d-bd69-3bdb6c888328.png">
<img width="1440" alt="POST" src="https://user-images.githubusercontent.com/41862239/222445387-91b544ff-b1bb-493e-bbb0-0dcf24afe78e.png">
<img width="1440" alt="GET2" src="https://user-images.githubusercontent.com/41862239/222445399-84af9db2-b3ce-417c-a459-2ab770008558.png">
<img width="1440" alt="PUT" src="https://user-images.githubusercontent.com/41862239/222445410-c9439f56-2d14-4584-b807-361ad99c3b78.png">
<img width="1440" alt="DELETE" src="https://user-images.githubusercontent.com/41862239/222445416-a8a5b84e-dd76-4808-af7e-a1effb4e40ad.png">
<img width="1440" alt="GET3" src="https://user-images.githubusercontent.com/41862239/222445427-f10ec26d-7bcc-4a0a-8b80-48431bb621a0.png">

# 2. Задачки

## 1

После того, как последний пакет пройдёт первое соединение, останется задержка в $(N-1)\frac{L}{R}$. Задержка на прохождение всеми пакетами первого соединения равна $P\frac{L}{R}$. Таким образом суммарная задержка равна $(N+P-1)\frac{L}{R}$.

## 2

Пусть $X=40$ Мбит - размер файла. Аналогично первому заданию, задержка равна $\approx \frac{X}{R_1} \approx 200$ с.

## 3

В каждый момент времени вероятность одновременной передачи данных $\geq 12$ пользователями равна $\sum_{i=12}^{60}0.2^{i}0.8^{60-i}{60 \choose i} \approx 0.55$.

## 4

Пусть $P$ - количество пакетов, которое получается при разбиении файла на сегменты по $S$ бит. $P=\frac{X}{S}$.

Задержка равна $(3+P-1)\frac{L}{R}=\frac{X+2S}{S}\frac{S+80}{R}=\frac{2S^2+(X+80)S+80X}{SR}$.

Найдём минимум функции $f(S)=\frac{2S^2+(X+80)S+80X}{SR}$.

$f'(S)=\frac{1}{R}(2-\frac{80X}{S^2})=0 \Rightarrow S=\sqrt{40X}$.

## 5

а) Суммарная задержка равна $\frac{L}{R}+\frac{IL}{R(1-I)}=\frac{L}{R}+\frac{aL^2}{R^2(1-\frac{aL}{R})}=\frac{L}{R}+\frac{aL^2}{R^2-aLR}=\frac{L(R-aL)+aL^2}{R(R-aL)}=\frac{L}{R-aL}$

б) $\frac{L}{R-aL}=\frac{L}{R}\frac{1}{1-I}$

При увеличении $\frac{L}{R}$ увеличивается $I$, то есть увеличивается и $\frac{1}{1-I}$.

Значит при увеличении $\frac{L}{R}$ задержка увеличивается.
