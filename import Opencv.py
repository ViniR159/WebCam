import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
Ativar = True

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2)
mpDrawn = mp.solutions.drawing_utils

if webcam.isOpened():
    while Ativar:
        foi, imagem = webcam.read()
        resultado = Hand.process(imagem)
        HandPoints = resultado.multi_hand_landmarks

        if HandPoints:
            for i in HandPoints:
                print(i)
                mpDrawn.drawn_landmarks(imagem,i,hand.HAND_CONNECTIONS)


        cv2.imshow("Test", imagem)
        key = cv2.waitKey(1)
        # print(key)
        if key == 27:
            Ativar = False

        

webcam.release()
cv2.destroyAllWindows()
