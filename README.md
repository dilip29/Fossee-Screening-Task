# Project :Fossee Steel Application 


----

> This is a Steel Desktop application build in python that allows user to access data of a steel ...see its various types and features
also add a new steel to the Steel database
## TASK
 > Displaying the properties of the steel section from the given database.
 Appending properties of new steel section(s) to the current database.
---


## Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Use of Badges](#use-of-badges)
- [Features](#features)
- [Installation](#installation)
- [Code Snippet](#code-snippet)
- [Getting Started](#getting-started)
- [Tools](#tools)



---

## Description
> Fosse Steel is build in python using `Pyqt5` library specifically `QtCore`  `QtGui`  `QtWidgets` for **GUI** development and `SqliteStudio` for **Back end database connectivity**.


---

### Use of Badges

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Github Issues](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/issues.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/issues)  [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

- For more on these wonderful `badges`, refer to <a href="http://badges.github.io/badgerbadgerbadger/" target="_blank">`badgerbadgerbadger`</a>.



![steel1](https://user-images.githubusercontent.com/40792388/54923502-6307f080-4f30-11e9-8c97-4fd396085bb4.gif)




## Features
  * Open a specific steel 
  * Select among various types of steels
  * View various features of steel selected
  * Add a new steel entry to the database
  
 





## Installation
* install `PyQt5` python library using pip
```python
pip install PyQt5

```
or
```python
pip3 install PyQt5

```
* Install SqliteStudio for creating database for the `Angles` , `Beams` , `Channels`

- Download Sqlite Studio - [Sqlitestudio](https://sqlitestudio.pl/index.rvt)



![steel2](https://user-images.githubusercontent.com/40792388/54923689-c1cd6a00-4f30-11e9-97ff-477af28fff30.gif)





## Code Snippet

```python
        sql="select Designation from Channels"
            channels=[]
            cur=conn.execute(sql)
            for row in cur:
                channels.append(row[0])

            channel_option, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Steel","Choose a Designation from Channels Section",channels,0,False)
            if ok and channel_option:
                self.lineEdit_6.setText(channel_option)

```






---
## Getting Started
```
git clone https://github.com/kalwaniya/fsf_2019_screening_task3/
```
* install the required tools 

* fork or download the repo 

* run the following command in terminal

```
python3 steel.py
```


![steel3](https://user-images.githubusercontent.com/40792388/54923730-df023880-4f30-11e9-9359-fa412884a033.gif)






## Tools
### References
* [Atom](https://atom.io/)
* [SqliteStudio](https://sqlitestudio.pl/index.rvt)
* [Python](https://www.python.org/)



---



## License
---
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

