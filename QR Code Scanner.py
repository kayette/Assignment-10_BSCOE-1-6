from pyzbar import pyzbar; from datetime import *; import time
import webbrowser
import cv2

def time_registry(img):
    QRScanner = pyzbar.decode(img)
    for info in QRScanner:
        a, b, c, d = info.rect 
        QR_txt = info.data.decode('utf-8') 
        cv2.rectangle(img, (a, b),(a+c, b+d), (0, 255, 0), 3) 
        TxtFont = cv2.FONT_HERSHEY_COMPLEX_SMALL 
        cv2.putText(img, QR_txt, (a + 10, b - 10), TxtFont, 1.0, (255, 0, 0), 2) 
        local_time = datetime.now() 
        datezone = local_time.strftime("%B %d, %Y") 
        current_time = time.localtime() 
        timezone = time.strftime("%H:%M", current_time) 
        timezoneNUM = int(time.strftime("%H", current_time)) 
        timezoneDate = time.strftime("%M", current_time) 
        hour_clock = 12
        with open('Contact Tracing Form.txt', "w") as textfile:
            if timezoneNUM >= 0 and timezoneNUM < hour_clock:
                textfile.write(QR_txt + (f"\n\n>>> REAL-TIME MANAGEMENT SYSTEM <<< \nDate Tracking Record: {datezone}\nTime Tracking Record: {timezone} AM"))
            else:
                timeCurrent = (timezoneNUM) - hour_clock
                textfile.write(QR_txt + (f"\n\n>>> REAL-TIME MANAGEMENT SYSTEM <<< \nDate Tracking Record: {datezone}\nTime Tracking Record: {timeCurrent}:{timezoneDate} PM"))
    return img; 

def webcamScanner():
    scan = cv2.VideoCapture(0) 
    detectQR = cv2.QRCodeDetector() 
    while True: 
        _, img = scan.read() 
        data, vrcam, _ = detectQR.detectAndDecode(img)
        img = time_registry(cv2.resize(img, None, fx=1.5, fy=1.5, interpolation = cv2.INTER_LINEAR_EXACT))
        if data:
            a = data
            break
        cv2.imshow('Kazuha QR Code Scanner', img) 
        if cv2.waitKey(1) == ord('q'): 
            break 
    b = webbrowser.open(str(a))
    scan.release() 
    cv2.destroyAllWindows()

webcamScanner() 