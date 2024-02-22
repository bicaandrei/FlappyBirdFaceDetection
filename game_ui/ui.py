import cv2

class UI:

    def __init__(self, bird_service, pipe_service):

        self.__bird_service = bird_service
        self.__pipe_service = pipe_service
        self.__face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.__eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        self.__startSecondPipe = False
        self.__startThirdPipe = False
        self.__pipeSpeed = 6

        self.__bird_pngs = [

            "PNGs/184-1842460_flappy-bird-bird-png-transparent-png.png"

        ]

        self.__lower_pipe_pngs = [

            "PNGs/250Complement_flappy-bird-pipes-png-bottle.png",
            "PNGs/250_flappy-bird-pipes-png-bottle.png"

        ]

        self.__upper_pipe_pngs = [

            "PNGs/250_flappy-bird-pipes-png-bottle.png",
            "PNGs/250Complement_flappy-bird-pipes-png-bottle.png"

        ]

    def changePipes(self, pipe_nr):

        UpperPipe = self.__pipe_service.add_pipe(self.__upper_pipe_pngs[pipe_nr])
        upper_pipe_body = UpperPipe.get_pipe()

        LowerPipe = self.__pipe_service.add_pipe(self.__lower_pipe_pngs[pipe_nr])
        lower_pipe_body = LowerPipe.get_pipe()

        return UpperPipe, LowerPipe, upper_pipe_body, lower_pipe_body

    def game(self):

     cap = cv2.VideoCapture(0)
     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
     print(cap.get(3))

     if (cap.isOpened == False):
            print("Error opening camera!")

     UpperPipe, LowerPipe, upper_pipe_body, lower_pipe_body = self.changePipes(0)
     UpperPipe1, LowerPipe1, upper_pipe_body1, lower_pipe_body1 = self.changePipes(1)
     UpperPipe2, LowerPipe2, upper_pipe_body2, lower_pipe_body2 = self.changePipes(0)
     bird = self.__bird_service.add_bird(self.__bird_pngs[0])
     bird_body = bird.get_bird()
     while True:

        return_value, frame = cap.read()
        if return_value == True:

           inverted_frame = cv2.flip(frame, 1)
           gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           gray_frame = cv2.flip(gray_frame, 1)

           try:

              inverted_frame[0:UpperPipe.get_pipe_height(), int(cap.get(3)) - UpperPipe.get_pipe_width()-UpperPipe.pipe_x:int(cap.get(3))-UpperPipe.pipe_x] = upper_pipe_body
              inverted_frame[int(cap.get(4)) - LowerPipe.get_pipe_height():int(cap.get(4)), int(cap.get(3)) - LowerPipe.get_pipe_width()-LowerPipe.pipe_x:int(cap.get(3))-LowerPipe.pipe_x] = lower_pipe_body
              if UpperPipe.pipe_x >= int(cap.get(3)) / 3:
                  self.__startSecondPipe = True
              if UpperPipe.pipe_x >= 2*int(cap.get(3)) / 3:
                  self.__startThirdPipe = True

              UpperPipe.pipe_x += self.__pipeSpeed
              LowerPipe.pipe_x += self.__pipeSpeed

           except ValueError:

              UpperPipe, LowerPipe, upper_pipe_body, lower_pipe_body = self.changePipes(1)
              UpperPipe.pipe_x = 0
              LowerPipe.pipe_x = 0

           try:

              if self.__startSecondPipe == True:
                   inverted_frame[0:UpperPipe1.get_pipe_height(),int(cap.get(3)) - UpperPipe1.get_pipe_width() - UpperPipe1.pipe_x:int(cap.get(3)) - UpperPipe1.pipe_x] = upper_pipe_body1
                   inverted_frame[int(cap.get(4)) - LowerPipe1.get_pipe_height():int(cap.get(4)),int(cap.get(3)) - LowerPipe1.get_pipe_width() - LowerPipe1.pipe_x:int(cap.get(3)) - LowerPipe1.pipe_x] = lower_pipe_body1
                   UpperPipe1.pipe_x += self.__pipeSpeed
                   LowerPipe1.pipe_x += self.__pipeSpeed

           except ValueError:

              UpperPipe1, LowerPipe1, upper_pipe_body1, lower_pipe_body1 = self.changePipes(0)
              UpperPipe1.pipe_x = 0
              LowerPipe1.pipe_x = 0

           try:

               if self.__startThirdPipe == True:
                   inverted_frame[0:UpperPipe2.get_pipe_height(),int(cap.get(3)) - UpperPipe2.get_pipe_width() - UpperPipe2.pipe_x:int(cap.get(3)) - UpperPipe2.pipe_x] = upper_pipe_body2
                   inverted_frame[int(cap.get(4)) - LowerPipe2.get_pipe_height():int(cap.get(4)),int(cap.get(3)) - LowerPipe2.get_pipe_width() - LowerPipe2.pipe_x:int(cap.get(3)) - LowerPipe2.pipe_x] = lower_pipe_body2
                   UpperPipe2.pipe_x += self.__pipeSpeed
                   LowerPipe2.pipe_x += self.__pipeSpeed

           except ValueError:

               UpperPipe2, LowerPipe2, upper_pipe_body2, lower_pipe_body2 = self.changePipes(0)
               UpperPipe2.pipe_x = 0
               LowerPipe2.pipe_x = 0

           faces = self.__face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
           for (x, y, w, h) in faces:
               cv2.rectangle(inverted_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
               # roi_face_gray = ray_frame[y:y+h, x:x+w]
               roi_face_color = inverted_frame[y:y + h, x:x + w]
               try:

                   inverted_frame[y + int(h / 2):y + int(h / 2) + bird.get_bird_height(),x + int(w / 2):x + int(w / 2) + bird.get_bird_width()] = bird_body
                   bird.bird_x = x+int(w/2)+bird.get_bird_width()
                   bird.bird_y = y+int(h/2)+int(bird.get_bird_height()/2)
                   print(x, y)
                   cv2.line(inverted_frame, (bird.bird_x, bird.bird_y), (bird.bird_x, bird.bird_y+2), (255, 0, 0), 2)
               except ValueError:
                   print('plm iesi pasarea')

           cv2.imshow('CurrentFrame', inverted_frame)

           if cv2.waitKey(1) & 0xFF == ord('q'):
              break
        else:
          break

     cap.release()
     cv2.destroyAllWindows()