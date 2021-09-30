import cv2, time

first_frame=None
video = cv2.VideoCapture(0)

while True:
    
    check, frame = video.read()
    frame=cv2.rotate(frame, cv2.ROTATE_180)  
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21,21), 0)
    
    if first_frame is None:
        first_frame=gray
        continue

    Detla_frame=cv2.absdiff(first_frame, gray)
    threshold_frame=cv2.threshold(Detla_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame=cv2.dilate(threshold_frame, None, iterations=2)

    (cnts,_)= cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for Contour in cnts:
        if cv2.contourArea(Contour)<1000:
            continue

        (x, y, w, h)= cv2.boundingRect(Contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    cv2.imshow("capturing", frame)
    # cv2.imshow("gray", gray)
    # cv2.imshow("diff", Detla_frame)
    cv2.imshow("thres", threshold_frame)
    



    key=cv2.waitKey(1)
    if key==ord('q'):
        break 

video.release()
cv2.destroyAllWindows()

