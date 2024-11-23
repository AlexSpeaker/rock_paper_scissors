#!/bin/bash
cd ..
path_project='game'

echo "START MYPY"
mypy $path_project

echo "START BLACK"
black $path_project

echo "START ISORT"
isort --profile black $path_project

echo "START FLAKE8"
flake8 --ignore=E501 $path_project