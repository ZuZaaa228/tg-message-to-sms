[ENG README](https://github.com/ZuZaaa228/tg-message-to-sms/blob/master/README_ENG.md)
# Мини гайд на использование
## 1. Перед установкой 
### 1. Создание учетной записи Telegram и получение API ключей
Перейдите на my.telegram.org.
Войдите с использованием вашего Telegram аккаунта.
Создайте новое приложение и получите API_ID и API_HASH.
### 2. Создание учетной записи Twilio
Перейдите на twilio.com.
Зарегистрируйтесь и получите Account SID, Auth Token, и номер телефона Twilio (Twilio Phone Number).

## 2. Устновка зависимостей
```sh
    pip install -r req.txt
```

### 3. Создание .env
В файле должны быть параметры, которые вы получили из пункта 1

    # Учетные данные Telegram
    API_ID=your_telegram_api_id
    API_HASH=your_telegram_api_hash
    PHONE=+your_telegram_phone_number
    
    # Учетные данные Twilio
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    TARGET_PHONE_NUMBER=target_phone_number

## 4. Создание файлов с чатами и ссылками на каналы
### Создайте два файла:
#### Важно:  все записи в файл через пробел
#### chats.txt:
Содержит публичные каналы, которые вы хотите отслеживать. Писать канал в следующем виде:
| Название канала | Запись в файле |
|--|--|
| @ChannelName | ChannelName |



#### invite_links.txt: 
Содержит приглашения на приватные каналы. Ссылки на приглашение в приватные каналы.
| Название канала | Запись в файле |
|--|--|
| https://t.me/+i_qwe123QWEasd | +i_qwe123QWEasd |


## Запуск:

    python main.py

После вам потребуется ввести код с номера телефона для создание сессии
Ждите сообщения!
