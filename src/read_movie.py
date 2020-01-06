import cv2


class ReadMovie(object):

    def __init__(self, filename):
        capture = cv2.VideoCapture(filename)
        self.capture = capture
        self.width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frame_per_second = capture.get(cv2.CAP_PROP_FPS)

    def print_value(self):
        print("image width : " + str(self.width))
        print("image height : " + str(self.height))
        print("total frame count : " + str(self.count))
        print("FPS : " + str(self.frame_per_second))
        number = 0

    def show_movie(self):
        number = 0
        # show movie
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                cv2.imshow("frame", frame)
                # divide avi
                file_path = "../snapshot/snapshot_" + str(number) + ".jpeg"
                cv2.imwrite(file_path, frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    print(str(number) + ": image was output.")
                    break
            number = number + 1
        self.capture.release()
        cv2.destroyAllWindows()


class MainReadMove:
    readMovie = ReadMovie("../mov/mov01.avi")
    readMovie.print_value()
    readMovie.show_movie()

