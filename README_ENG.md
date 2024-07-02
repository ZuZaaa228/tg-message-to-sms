# Mini guide to use
## 1. Before installation 
### 1. Creating a Telegram account and receiving API keys
Go to my.telegram.org .
Log in using your Telegram account.
Create a new application and get the API_ID and API_HASH.
### 2. Creating a Twilio Account
Go to twilio.com .
Register and receive an Account SID, Auth Token, and a Twilio Phone Number.

## 2. Setting up dependencies
```sh
    pip install -r req.txt
```

### 3. Creation.env
The file should contain the parameters that you received from point 1

    # Telegram Credentials
    API_ID=your_telegram_api_id
    API_HASH=your_telegram_api_hash
    PHONE=+your_telegram_phone_number
    
    # Twilio Credentials
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    TARGET_PHONE_NUMBER=target_phone_number

## 4. Creating files with chats and links to channels
### Create two files:
#### Important: all entries in the file are separated by a space
#### chats.txt:
Contains the public channels that you want to monitor. Write a channel in the following form:
| Channel name | File entry |
|--|--|
| @ChannelName | ChannelName |



#### invite_links.txt: 
Contains invitations to private channels. Links to invitations to private channels.
| Channel name | File entry |
|--|--|
| https://t.me/+i_qwe123QWEasd | +i_qwe123QWEasd |


## Launch:

    python main.py

After that, you will need to enter the code from the phone number to create a session
Wait for the message!
