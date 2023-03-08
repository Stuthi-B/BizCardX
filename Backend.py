import easyocr as ocr
import torch
import torchvision
import re
import cv2

def extractData():
    img = cv2.imread("./cards/3.png", -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    email = []
    mobno = []
    url = []
    pincode = []
    address = []
    company = []
    card_holder=[]
    designation=[]
    reader = ocr.Reader(['en','en'], gpu=True)
    data = reader.readtext(img, detail = 0)
    for i in data:
        print(i)
        mobno.append(i) if re.search(r"(\+?\d{1,3}[- ]?\d{3}[- ]?\d{4})",i) != None else ""
        email.append(i) if re.search(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+',i) != None else ""
        url.append(i) if re.search(r'^((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?\/?$',i) != None else ""
        pincode.append(re.findall(r"(\d{6})", i)) if re.findall(r"(\d{6})", i) else ""
        address.append(i) if re.search(r"([0-9a-zA-Z #,-]+) , ([a-zA-Z ]+), \s*([a-zA-Z]+);", i) else ""
        company.append(i) if re.findall('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', i) else ""
        card_holder.append(i) if  re.findall("^[A-Z][-a-zA-Z]+$",i) else ""
    # designation.append(data[1])
    print(mobno, email, url, pincode, address, company, card_holder)


extractData()