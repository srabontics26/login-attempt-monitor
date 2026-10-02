# Login Attempt Monitor

A Python tool that checks login logs for repeated failed attempts.

## About the Project

I made this project to practice Python and learn how login activity can be reviewed for suspicious patterns.

The program counts failed login attempts from different IP addresses and reports an address when it has multiple failed attempts.

## Features

- Reads sample login activity
- Counts failed login attempts
- Groups attempts by IP address
- Flags repeated failures
- Simple command-line output

## Technologies Used

- Python 3
- collections.Counter

## How to Run

Run the program with:

```bash
python login_monitor.py
