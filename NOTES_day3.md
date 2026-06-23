# Day 3 - Python

## Agenda

1. File Handling
2. Logging
3. Environments, Modules, Packages
4. Intro to Regular Expressions

## File Handling

Security Sandbox (Browser) - An interface for safely executing JS code on the browser

Python offers direct access to files using `open` function.

Memory Leak - An instance of wasted system memory when running a program.

Garbage Collectors - Responsible for cleaning up memory in the event your program does not need to utilize it anymore.

`with` => Context manager ==> Safely closes your file automatically even if there is an unexpected error that occurs midway through program execution

## Logging

Logging - Adding records of events

### Hierachy of Logging Levels

- `DEBUG` - Detailed diagnostics (developer level)
- `INFO` - General app flows
- `WARNING` - Something looks wrong but app did not crash
- `ERROR` - Something actually went wrong but other parts of your app continue working
- `CRITICAL` - Entire app goes down

## Environments, Modules and Packages

pip - dependency manager

Virtual Environment - A clone of the python system upon which you can manage dependencies at project/folder level

Tools for Virtual Environments

- venv
- pipenv
- virtualenv

Module - Single python file that contains variables and functions
Package - A directory / folder contains multiple modules, includes a special file : `__init__.py`
