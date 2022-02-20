import cv2
import numpy as np

def byte2img(bytestr,filename=None,debug=False,grayscale=False):
    bytestr = bytestr[2:] if isinstance(bytestr,str) and bytestr.startswith('0x') else bytestr
    hexlen = len(bytestr)
    binlen = 4*hexlen
    binstr = bin(int(bytestr,16))[2:]
    binstr = '0'*(binlen-len(binstr)) + binstr
    hexarr = np.uint8([int(byte,16)*16 for byte in bytestr])
    binarr = np.uint8([int(binary)*255 for binary in binstr])
    if len(bytestr) == 64:
        img = np.reshape(binarr,(16,16))# if not grayscale else np.reshape(hexarr,(8,8))
    elif len(bytestr) == 40:
        img = np.reshape(binarr,(10,16)) if not grayscale else np.reshape(hexarr,(5,8))
    else: return
    if filename:
        cv2.imwrite(filename,img)
    if debug:
        cv2.imshow('image',img)
        if cv2.waitKey(10000) & 0xFF == ord('q'):return
