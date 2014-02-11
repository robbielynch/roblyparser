RoblyParser
=======

A simple HTML parser written in Python.

Usage
----
```python
from roblyparser.robly_parser import RoblyParser

URL = "http://github.com"

# To get a website as an object
parser = RoblyParser()
html_object = parser.get_webpage_as_object(URL)
```