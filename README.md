# pdf2pro6x
Convert PDF files to ProPresenter 6 Bundle files.

## Get started
pdf2pro6x uses pdf2image which uses poppler, so you have to install that first. See [pdf2image](https://github.com/Belval/pdf2image).

After that, make sure you have pipenv installed or run:
```shell script
pip install --user pipenv
```

Then install the dependencies with:
```shell script
pipenv install
```

Now you can run pdf2pro6x:
```shell script
pipenv run python pdf2pro6x.py path_to_pdf
```

## Create single executable file
To create an executable for your system install the dev dependencies:
```shell script
pipenv install --dev
```

Then run:
```shell script
pipenv run pyinstaller -F pdf2pro6x.py
```

After that you will find the executable in the `dist` directory.