# SVG-PC-Editor

A desktop-ready version of **SVG-Edit** using **Python** and **pywebview**.

## Overview

This project adapts the popular web-based SVG editor **SVG-Edit** to run as a desktop application. It uses Python and `pywebview` to wrap the HTML/JS interface in a native desktop window.

## Features

- Dark and Light mode
- Full-featured SVG editor (based on SVG-Edit)
- Desktop window using `pywebview` (no need for a browser)
- Integration between Python and JavaScript through `SVGEditAPI.py`
- Local storage management with persistence
- Optional internal web server for advanced use cases

## Project Structure

- `main.py` — Main entry point, loads the editor via `pywebview`
- `mainWServer.py` — Alternate version that runs a local server
- `SVGEditAPI.py` — API bridge between Python and JavaScript
- `LocalStorageManager.py` — Handles localStorage saving
- `html/` — Contains the modified SVG-Edit frontend

## Requirements

- Python 3.8+
- `pywebview` library

Install with:

```bash
pip install pywebview
