import cv2

webcam = cv2.VideoCapture(0)
Ativar = True



if webcam.isOpened():

    while Ativar:
        foi, imagem = webcam.read()
        cv2.imshow("Test", imagem)
        key = cv2.waitKey(1)
        print(key)
        if key == 27:
            Ativar = False

webcam.release()
cv2.destroyAllWindows()
