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

## Regular Expressions (RegEx)

- A sequence of characters that form a specific search pattern.

*** All programming languages can interpret this sequence of characters

### Why use RegEx?

- Data Validation
- Text Extraction
- Search and Replace

### Components

RegEx are built from character literals (alphanumeric characters), and metacharacters (symbols that have a special meaning)

1. Anchors - Specify where in the text to look

Examples:-  
    
    a. `^` - check at the start of text
    b. `$` - check at the end of the text

2. Character Classes - Specify types of characters to search for

Examples:-

    a. `\d` - Match digits (0 - 9)
    b. `\w` - Match words (letters, numbers, or underscores)
    c. `\s` - Matches white spaces
    d. `.` - Matches any character

3. Quantifiers - Dictate number of characters

Examples:-  

    a. `+` - one or more
    b. `*` - zero or more
    c. `?` - zero or one
    d. `{n}` - exactly n times


### Examples

1. Match / Confirm text provided is a 3 digit area code - `\d{3}$`
2. Basic Email format - `\w+@\w+\.\w+$`
