# COMMANDER

A CLI tool to manage in a more straightforward and natural way your projects.
Based on Django's approach

### Status

Incompleted

### Content Table

- [Used Technologies](#used-technologies)
- [Features](#features)
- [How to Run](#how-to-run)
- [Author](#author)
- [License](#license)

### Used Technologies

- Python 3+

### Features

- [x] `JSON` configurable
- [x] custom template support

### How to Run

- Installation

```shell
$ pip install tb111-commander
```

- Setup

```shell
# execute the initialization for a new project
$ commander -i
# or
$ commander --init

# if you still using in a legacy project follows this steps:

# create config root folder
$ mkdir commander

# create the main project localizer
$ touch root.py

# write the follow json in:

{ "PROJECT_PATH": "<path>" }
```

### Author

@thebe111

### License

- MIT
