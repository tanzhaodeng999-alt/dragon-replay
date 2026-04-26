name: dragon-replay

on:
  workflow_dispatch:
  schedule:
    - cron: "10 7 * * 1-5"

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
    - name: checkout
      uses: actions/checkout@v3

    - name: setup python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: install
      run: pip install -r requirements.txt

    - name: run
      run: python main.py
