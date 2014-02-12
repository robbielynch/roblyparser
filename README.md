RoblyParser
=======

A simple HTML parser written in Python.

Usage
----
To get the latest stable release:
```
git clone https://github.com/robbielynch/RoblyParser roblyparser
cd roblyparser
git checkout v0.1
```

Copy the directory into your project and then:
```python
from roblyparser.robly_parser import RoblyParser

URL = "http://github.com"

# To get a website as an object
parser = RoblyParser()
html_object = parser.get_webpage_as_object(URL)
```

###What is in the HTML object?

| Attribute     | Type              |
| ------------- |:-----------------:|
| title         | string            |
| description   | string            |
| h1s           | list of string    |
| keywords      | list of string    |
| links         | list of string    |
| images        | list of string    |
| body          | string            |
| body_html     | string            |
| robots_index  | boolean           |
