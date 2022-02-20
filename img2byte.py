# this code is from https://github.com/deep2essence/pywallet/blob/main/utils/image.py
import cv
import os
def img2byte(img,debug=False,grayscale=False):
    if isinstance(img,str):
        if not os.path.exists(img): return ""
        filepath = img
        img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    rows,cols=img.shape[:2]
    if rows != 16 or cols !=16:
        img = cv2.resize(img, (16, 16))
        #_,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        _,filename = os.path.split(filepath)
        fn,ext = os.path.splitext(filename)
        fullpath = os.path.join("keyimgs",fn.replace("Scrapper", "prvkey")+ext)
        cv2.imwrite(fullpath,img)
    bytestr=""
    if grayscale:
        for byte in np.reshape(img,img.shape[0] * img.shape[1]): bytestr += hex(byte/16).replace("0x","").strip("L")
    else:
        binstr=""
        for binary in np.reshape(img,img.shape[0] * img.shape[1]): binstr += "1" if binary > 0 else "0"
        bytestr = hex(int(binstr,2)).replace("0x","").strip("L")
        bytestr = '0'*(64-len(bytestr)) + bytestr
    if bytestr == '0' * 64: bytestr = '1'*64
    if debug:
        from eth.key import priv2addr
        from eth.req import getBalance
        addr = priv2addr(bytestr)
        print addr,bytestr,getBalance(addr)
    return bytestr
