# 2. Wireshark. Работа с DNS

## А

1. 147.8.2.58 - IP-адрес сайта Гонконгского университета
2. raptor.dns.ox.ac.uk - авторитетный DNS-сервер Оксфордского университета.
3. У www.google.com несколько IP-адресов. У spbu.ru 1 IP-адрес.

<img width="1440" alt="task1" src="https://user-images.githubusercontent.com/41862239/227238772-105e4a46-613e-4092-849e-101d3bd6bedc.png">

## Б

1. Запрос и ответ отправлены с помощью протокола UDP.
2. У запроса DNS порт назначения 53.
3. DNS-запрос отправлен на IP-адрес 192.168.1.104. Этот адрес совпадает с адресом моего локального DNS-сервера.
4. Запрашивается запись типа A, в запросе содержится 0 ответов.
5. В ответном сообщении 3 ответа: каноничное имя и 2 IP-адреса сервиса.
6. 104.16.44.99 - IP-адрес назначения пакета с SYN, и этот адрес соответствует первому адресу из ответного сообщения DNS.
7. Хост выполняет 1 новый запрос DNS к analytics.ietf.org перед загрузкой изображений.

<img width="1440" alt="task2 1" src="https://user-images.githubusercontent.com/41862239/227238807-b500863d-c4da-4f50-812d-24211a081d7d.png">
<img width="1440" alt="task2 2" src="https://user-images.githubusercontent.com/41862239/227238816-0483ba60-e904-44bb-90a5-261edc9bde35.png">
<img width="1440" alt="task2 3" src="https://user-images.githubusercontent.com/41862239/227238836-1da279bd-2155-40ff-9657-c7a070a75592.png">
<img width="1440" alt="task2 4" src="https://user-images.githubusercontent.com/41862239/227238853-b1240bb1-18bd-42b2-a959-658598198299.png">

## В

1. У запроса DNS порт назначения 53, как и порт источника в ответе.
2. DNS-запрос отправлен на IP-адрес 192.168.1.1. Этот адрес совпадает с адресом моего локального DNS-сервера.
3. Запрашивается запись типа A, в запросе содержится 0 ответов.
4. В ответном сообщении 2 ответа: каноничное имя и 1 IP-адрес сервиса.

<img width="1440" alt="task3 1" src="https://user-images.githubusercontent.com/41862239/227238887-9fe2b6a3-f2c4-44d7-8519-944d5db29faa.png">
<img width="1440" alt="task3 2" src="https://user-images.githubusercontent.com/41862239/227238898-4505fab9-f796-4737-87a0-99bca727a262.png">

## Г

1. DNS-запрос отправлен на IP-адрес 192.168.1.1. Этот адрес совпадает с адресом моего локального DNS-сервера.
2. Запрашивается запись типа NS, в запросе содержится 0 ответов.
3. В ответном сообщении содержатся имена ns2.pu.ru и ns.pu.ru DNS-серверов университета. IP-адреса в ответе не содержатся.

<img width="1440" alt="task4" src="https://user-images.githubusercontent.com/41862239/227238936-049c99db-84a6-49a3-9c39-c627973d2920.png">

## Д

1. DNS-запрос отправлен на IP-адрес 192.70.196.210. Этот адрес не совпадает с адресом моего локального DNS-сервера. Он принадлежит хосту ns2.pu.ru.
2. Запрашивается запись типа A, в запросе содержится 0 ответов.
3. В ответном сообщении 2 ответа: каноничное имя и 1 IP-адрес сервиса.

<img width="1440" alt="task5" src="https://user-images.githubusercontent.com/41862239/227238954-081c86a0-86ee-461f-8088-86341d7623e3.png">

## Е

1. Whois – это база данных, в которой хранятся сведения о доменах.
2. Я использовал сервисы whois.com и whois.domaintools.com для получения имён DNS-серверов yandex.ru и jetbrains.com. Для yandex.ru я получил имя ns1.yandex.ru, для jetbrains.com я получил имя NS-1519.AWSDNS-61.ORG.
3. Я послал запросы к своему локальному DNS-серверу, а также к серверам yandex.ru и jetbrains.com, и получил от них ответы.

<img width="1440" alt="task6 1" src="https://user-images.githubusercontent.com/41862239/227238975-a6236d49-d4ed-4d91-904a-fbae0ae7242e.png">
<img width="1440" alt="task6 2" src="https://user-images.githubusercontent.com/41862239/227238998-79e3a935-2eb4-446c-8b81-c05c0e203fde.png">
<img width="1440" alt="task6 3" src="https://user-images.githubusercontent.com/41862239/227239011-19ef69ee-d255-4f82-b4ba-2168d8601ac1.png">
