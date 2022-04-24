# View Bot
#### By natrix
 Here is the user guide:
 
# How to use ? 

1- Try:
```PY
pip --version 
``` 
To see if pip works on your machine, else uninstall and install python with the latest version.

2- Install:
```
pip install selenium 
pip install time 
``` 
To get required modules.

3- Then go to line 6 to 10 
```PY
driver = webdriver.Chrome(executable_path="chromedriver.exe")
```
And change it with your [chromedriver](https://chromedriver.chromium.org/downloads) path.

4- Finally go to line 12 to 16 and paste your youtube url in 
```PY
driver.get("https://youtu.be/WLmAcdPvX8g") <-- Url here
```
5- Run & enjoy 

Code by [natrix](https://github.com/natrixdev) please ping me if you use my code 
Thanks to chromedriver for this amazing free service.

Code editor : [Visual Studio Code](https://code.visualstudio.com) with [python](https://www.python.org) language
