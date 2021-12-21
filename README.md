# Dependencies

## geckodriver (firefox)

Download the geckodriver from mozilla

https://github.com/mozilla/geckodriver/releases

Copy the geckodriver side by side the creadors_auto_follow.py

## python dependencies

```
pip install selenium
```

# run

```
$ python creadors_auto_follow.py
```

Enter username and password and twitch code and the program will start following streamers

# binary build

We used pyinstaller to bundle the windows exe for convinience. Linux users can run the python script directly.

```
$ pip install pyinstaller

$ pyinstaller .\creadors_auto_follow.py --onefile --clean
```

