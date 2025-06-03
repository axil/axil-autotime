# axil-autotime
An improved version of `ipython-autotime` by Phillip Cloud:  
&nbsp; &nbsp; – uses better timer function on Windows;  
&nbsp; &nbsp; – ignores function and class definitions.

## Installation:

```console
$ pip install axil-autotime
```
## Usage

Run `%load_ext autotime` to load the extension.

<img src="https://raw.githubusercontent.com/axil/axil-autotime/master/img/screenshot.png" width="400">

```python
In [1]: %load_ext autotime
time: 264 µs (started: 2020-12-15 11:44:36 +01:00)

In [2]: x = 1
time: 416 µs (started: 2020-12-15 11:44:45 +01:00)

In [3]: x / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-034eb0c6102b> in <module>
----> 1 x/0

ZeroDivisionError: division by zero
time: 88.7 ms (started: 2020-12-15 11:44:53 +01:00)
```

## Want to turn it off?

```python
In [4]: %unload_ext autotime
```
