# Led Light Show
Raspberry Pi controlled led light shows

# SetUp
```sh
  git clone https://github.com/AlexE543/LED_LightShow.git
```
Navigate into the folder of the clone
```sh
pip3 install adafruit-circuitpython-lis3dh
git submodule init
git submodule update

python3 -m venv .env
source .env/bin/activate
pip install circuitpython-build-tools
circuitpython-build-bundles --filename_prefix adafruit-circuitpython-neopixel --library_location .
```

