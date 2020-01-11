# pdf2pro6x
Convert PDF files to ProPresenter 6 Bundle files.

## Get started
Prerequisite: pdf2pro6x uses pdf2image which uses poppler, so make sure you have it installed. See [pdf2image](https://github.com/Belval/pdf2image#how-to-install).

**Hint: I recommend using a virtualenv to not mix dependencies from different projects.**

Install the dependencies with:
```shell script
pip install pdf2image
```

Now you can run pdf2pro6x:
```shell script
python pdf2pro6x.py path_to_pdf
```

## Create single executable file
**Hint: Pre-built executables for MacOS & Windows can be found in the [Release](https://github.com/P1zz4br0etch3n/pdf2pro6x/releases) Assets.**

First you have to install pyinstaller:
```shell script
pip install pyinstaller
```

To create an executable for your system run:
```shell script
pyinstaller -F pdf2pro6x.py
```

After that you will find the executable in the `dist` directory.