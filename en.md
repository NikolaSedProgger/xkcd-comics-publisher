# Comics publisher

This project publishes a random comic by xkcd on your community wall

### How to install
Python3 should already be installed. Then use `pip` (or `pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```
It is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html)

### Getting the right data to work with
First, create a [standalone app](https://vk.com/editapp?act=create) for your community and get a client id
Next, enter it in the .env file in the line with CLIENT_ID

```
CLIENT_ID=YourClientId
GROUP_ID=
ACCESS_TOKEN=
API_VERSION=5.131
```

Open the console and write
```
python get_access_token.py
```
We follow the received link and get the access_token from the link to the page we went to
`https://oauth.vk.com/blank.html# --> access_token=YourAccesToken <-- &expires_in=number&user_id=YourUserId`

Next, we add it to the .env file in the line with ACCESS_TOKEN
```
CLIENT_ID=YourClientId
GROUP_ID=
ACCESS_TOKEN=YourAccessToken
API_VERSION=5.131
```

We also need to get the [group id of our group](https://regvk.com/id/)
Next, we add it to the .env file in the line with ACCESS_TOKEN
```
CLIENT_ID=YourClientId
GROUP_ID=YourGroupId
ACCESS_TOKEN=YourAccessToken
API_VERSION=5.131
```

### How to start
Open the console and write
```
python main.py
```

### Project Goals

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).