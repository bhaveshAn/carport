# Parking Lot Problem

## Set up the project (Build on Python 3.5.2 and Linux Ubuntu 16.04 LTS)

Following command **installs dependencies**, **builds the binary** and **runs unittests**

* **PyInstaller** has been used for build purpose.

```
bin/setup
```

After running above command a executable binary file is created which can be found as `dist/main`

```
dist/main
```

Building your own binary

```
pyinstaller src/main.py --onefile
```

## Running automated tests

```
bin/run_functional_tests
```


## Running the application

Following commands runs the application in 2 modes

1. File Mode

```
bin/parking_lot file_input.txt
```

2. Interactive Mode

```
bin/parking_lot
```

## Running the application as python scripts (Python 3.5.2)

Following commands runs the application in 2 modes

1. File Mode

```
python3 src/main.py file_input.txt
```

2. Interactive Mode

```
python3 src/main.py
```

## Running unittests as python scripts (Python 3.5.2)

```
python3 tests_parking_lot.py
```


**Submitted By : [Bhavesh Anand](https://bhaveshan.github.io)**
