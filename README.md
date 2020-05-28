# OLT.crack
To mark answers quickly.

## Prerequisites

[Python3](https://www.python.org) must be pre-installed

## STEPS
- Clone or download all three files.
- Open terminal or CMD
- Change current directory to where these files are located.
```bash
cd /path/to/project
```
- Install dependencies
```bash
python3 -m pip install -r requirements.txt --user
```
Or simply
```bash
pip install -r requirements.txt
```
- Install Google Tesseract OCR (additional info how to install the engine on Linux, Mac OSX and Windows). You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable pytesseract.pytesseract.tesseract_cmd. Under Debian/Ubuntu you can use the package tesseract-ocr. For Mac OS users. please install homebrew package tesseract.
( Taken from ![this answer](https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror) )
### On Linux

sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

### On Mac

brew install tesseract

### On Windows

download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe' to your script. (replace path of tesseract binary if necessary)

references: https://pypi.org/project/pytesseract/ (INSTALLATION section) and https://github.com/tesseract-ocr/tesseract/wiki#installation

- Run the script:
```bash
python3 master.py
```
- Follow the instructions, open the browser and terminal/cmd side by side, otherwise it may not work.
<img src="https://i.ibb.co/xqZYj7m/Screenshot-from-2020-05-28-15-22-28.png">
- Thanks!
