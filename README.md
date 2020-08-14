# Tinder Bot for Data Scientists

Python Tinder Bot, which auto right swipes right for you, and also collects all profiles data such as Name, age, and Bio

This project is inspired from Aron Jack's [Automated Tinder Bot video](https://www.youtube.com/watch?v=lvFAuUcowT4).

## My Motvation/Why I'm doing it?

There are many Python bots available currently, and as being a Data Science aspirant, I wanted real dataset that consists real bios of real girls who stay around my city. By which I'll be able to perform Data Analysis on it and get valuable information such as what kind of bios do specific age groups of girls use on Tinder, what are the words used the most! Sentiment analysis on them, etc etc.

## Dependencies:
Python 3.5 or above.
Libraries used in this project:
 1. Selenium
 2. Pandas
 3. Chromium ([How to install it](https://www.youtube.com/watch?v=dz59GsdvUF8))

## How to use it:

1. Either clone or download the repository
2. Open the directory where you have saved inside the command prompt, and type `$pip install -r requirements.txt` to install all the dependencies.

> Note: Chormium will not be insatlled from requirements.txt, so you
> will have to download it and install. [Check this
> video](https://www.youtube.com/watch?v=dz59GsdvUF8).

3. Open `login_info.py` and enter your emial and passowrd in variables: `email_id` and `passowrd` and save it.
4. Open command prompt and run the comand `python tinder_bot.py`

- Chrome window will be opened and you will see it will automatically login and start swiping for you.
- Once you finish your likes you will get Finished LIKES!!! message on command prompt.
- There will be a file named *Bios_Collected.csv* in the same direcoty where all the data will be stored.

If you don't want to store the data you could just replace `profile_info = bot.auto_swipe()` with just `bot.auto_swipe()`

## Credits:

 [Aaron](https://github.com/aj-4)
