# Currency Converter

Приложение для конвертирования валют с использованием данных Центробанка России. Курсы валют обновляются раз в сутки после 00 часов и берутся с помощью сервиса www.cbr-xml-daily.ru.

## Стэк

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-DRF-informational?style=flat&logo=Django&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Requests-informational?style=flat&logo=requests&logoColor=white&color=green)
![](https://img.shields.io/badge/database-Postgresql-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)
![](https://img.shields.io/badge/Broker-Celery-informational?style=flat&logo=celery&logoColor=white&color=green)
![](https://img.shields.io/badge/Broker-Celery_beat-informational?style=flat&logo=celery&logoColor=white&color=green)
![](https://img.shields.io/badge/Cache-Redis-informational?style=flat&logo=redis&logoColor=white&color=green)

## Установка

1. Клонируйте репозиторий на свой компьютер:

   ```
   git clone https://github.com/Heattehnik/currency_converter.git
   ```

2. Создайте файл `.env` в корне приложения, используя образец из `.env_sample`.

3. Запустите приложение из каталога с приложением:

   ```
   docker-compose build
   docker-compose up -d
   ```

5. Приложение будет доступно по адресу `0.0.0.0:8000`.

6. При первом запуске база данных будет заполнена данными из файла `converter.json`, расположенного в каталоге `./fixtures`.

## Использование

Для конвертации валюты, используйте следующий формат URL:

```
http://0.0.0.0:8000/api/rates/?from={currency_from}&to={currency_to}&value={value}
```

Где:
- `currency_from` - из какой валюты конвертируем.
- `currency_to` - в какую валюту конвертируем.
- `value` - объем конвертируемой валюты.

Доступны следующие валюты для конвертации:

1. RUB (Российский рубль)
2. AUD (Австралийский доллар)
3. AZN (Азербайджанский манат)
4. GBP (Фунт стерлингов)
5. AMD (Армянский драм)
6. BYN (Белорусский рубль)
7. BGN (Болгарский лев)
8. BRL (Бразильский реал)
9. HUF (Венгерский форинт)
10. VND (Вьетнамский донг)
11. HKD (Гонконгский доллар)
12. GEL (Грузинский лари)
13. DKK (Датская крона)
14. AED (Дирхам ОАЭ)
15. USD (Доллар США)
16. EUR (Евро)
17. EGP (Египетский фунт)
18. INR (Индийская рупия)
19. IDR (Индонезийская рупия)
20. KZT (Казахстанский тенге)
21. CAD (Канадский доллар)
22. QAR (Катарский риал)
23. KGS (Киргизский сом)
24. CNY (Китайский юань)
25. MDL (Молдавский лей)
26. NZD (Новозеландский доллар)
27. NOK (Норвежская крона)
28. PLN (Польский злотый)
29. RON (Румынский лей)
30. XDR (СДР, МВФ)
31. SGD (Сингапурский доллар)
32. TJS (Таджикский сомони)
33. THB (Тайский бат)
34. TRY (Турецкая лира)
35. TMT (Туркменский манат)
36. UZS (Узбекский сум)
37. UAH (Украинская гривна)
38. CZK (Чешская крона)
39. SEK (Шведская крона)
40. CHF (Швейцарский франк)
41. RSD (Сербский динар)
42. ZAR (Южноафриканский рэнд)
43. KRW (Южнокорейская вона)
44. JPY (Японская иена)

Базовая валюта RUB.

## MISC

Приложение было протестировано со переменными окружения:

- `DB_NAME='postgres'`
- `DB_USER='postgres'`
- `DB_PASSWORD='postgres'`

По умолчанию в приложении отключена авторизация и аутентификация пользователей. Однако при необходимости возможно закрыть неавторизованный доступ к конвертору с помощью JWT.
