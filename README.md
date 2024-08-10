<h1 align="center">Django Plate Number Detection</h1>

<div align="center">

![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)&nbsp;
![OpenCV](https://img.shields.io/badge/-OpenCV-05122A?style=flat&logo=opencv)&nbsp;
![Django](https://img.shields.io/badge/-Django-05122A?style=flat&logo=django)&nbsp;
![TailwindCSS](https://img.shields.io/badge/-TailwindCSS-05122A?style=flat&logo=tailwindcss)&nbsp;
![PyTorch](https://img.shields.io/badge/-PyTorch-05122A?style=flat&logo=pytorch)&nbsp;

</div>

<p align="center">This repository is web application that aims to provide various features such as video live stream, haarcascade classifier, and optical character recognition (OCR). This app is built using Python, OpenCV, Django, TailwindCSS (django-tailwind), EasyOCR</p>

## Table of Contents

- [Tech Stack](#tech-stack)
- [Running on Localhost](#running-on-localhost)

## Tech Stack

- [Python](https://www.python.org) (`Programming Language`): Python is a high-level, interpreted programming language known for its simplicity and versatility, widely used in web development, data analysis, artificial intelligence, scientific computing, and more.
- [OpenCV](https://opencv.org) (`Computer Vision`): OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It provides a comprehensive set of features for image processing, computer vision, and machine learning.
- [Django](https://www.djangoproject.com) (`Framework`): Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is designed to help developers build robust and scalable web applications quickly.
- [TailwindCSS](https://tailwindcss.com) (`CSS Framework`): TailwindCSS is a utility-first CSS framework for building custom user interfaces rapidly and efficiently. It provides a comprehensive set of CSS utility classes that allow developers to design directly in their markup.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) (`OCR`): EasyOCR is a ready-to-use Optical Character Recognition (OCR) library built with deep learning techniques. It can handle text in different languages and is designed for high accuracy and performance.

## Running on Localhost

1. Clone this repository

```bash
git clone https://github.com/armandwipangestu/django-plate-number-detection.git && cd django-plate-number-detection
```

2. Install `python-virtualenv` (in my case use `Arch Linux`) and create the virtual environment

> **NOTE**: If you are using windows you can install with anaconda, then create the virtual environment
>
> ```ps
> conda create -n django-plate-number-detection python==3.8
> ```

```bash
sudo pacman -S python-virtualenv
```

```bash
virtualenv django-plate-number-detection
```

3. Activate the virtual environment to the current shell session

> **NOTE**: If you are using windows and anaconda, to activate the virtual environment use this command instead
>
> ```ps
> conda activate django-plate-number-detection
> ```

```bash
source django-plate-number-detection/bin/activate
```

4. Install dependency required library

```bash
pip install -r requirements.txt
```

5.
