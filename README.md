# SF Food Truck finder
A command line program that display a list of food trucks that are open at the current time and date

# Future improvement
* Caching request - Using a distributed in-memory cache in every hour expiration instead of using a local sqlite.
* Geo location detection
  * Web version - Auto detection by a browser
  * Command line - IP based geo location detection like with maxmind (https://www.maxmind.com/en/home)

# How to run this script
* Install dependencies
```
sudo pip install --upgrade pip
pip install virtualenv
virtualenv python
source python/bin/activate
```
* Run requirement packages
```
pip install -e .
```
* Run this script
```
> show_open_food_trucks

- Options
  -h --help                         Show this screen.
  --version                         Show version.
  --limit=<number>                  A number of items to display [default: 10].
```