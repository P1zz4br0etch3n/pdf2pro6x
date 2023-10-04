![app icon](src/main/icons/linux/128.png)

# pdf2pro6x
Convert PDF files to ProPresenter 6 Bundle files.

![screenshot windows](screenshots/screenshot_win.png)

![screenshot mac](screenshots/screenshot_mac.png)

## Prerequisite
pdf2pro6x uses pdf2image which is based on poppler, so make sure you have the latter installed.

See install instructions for [MacOS](https://formulae.brew.sh/formula/poppler) or [Windows](https://stackoverflow.com/a/60659237/7523613).

## Releases
You can download an installer or the cli version for macos and windows from the
[Releases](https://github.com/P1zz4br0etch3n/pdf2pro6x/releases) section.

## Usage
Just open the app, browse for a PDF file or paste its path and click `Convert`.

## Development
Make sure you have qt5 installed and added the bin directory to your PATH:
```sh
$ brew install qt5
$ echo 'export PATH="/opt/homebrew/opt/qt@5/bin:$PATH"' >> ~/.bashrc
```
Then create a virtualenv, activate it and install the requirements:
```sh
$ pip install virtualenv
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt  # this can take a while...
```
Now you're ready to go.