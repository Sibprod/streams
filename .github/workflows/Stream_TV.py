name : stream France 2

on:
  push:
    branches:
      - main

jobs
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Vérifier le dépôt
      uses: actions/checkout@v2

    - name: Configurer Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Exécuter le script
Python
      run: python ../streams/feed/france2.py
