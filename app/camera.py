import cv2
import easyocr

haarcascade_location = cv2.data.haarcascades
plate_detection1 = cv2.CascadeClassifier(haarcascade_location + 'haarcascade_russian_plate_number.xml')
plate_detection2 = cv2.CascadeClassifier(haarcascade_location + 'haarcascade_license_plate_rus_16stages.xml')

frame_with_roi = None

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.reader = easyocr.Reader(["en"])

    def __del__(self):
        self.video.release()
    
    def get_frame_plate(self):
        global frame_with_roi

        minArea = 500

        success, frame = self.video.read()
        if not success:
            print('Error camera: failed to grab frame')
            return False

        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        numberPlates = plate_detection1.detectMultiScale(frameGray, scaleFactor=1.1, minNeighbors=4)

        for (x, w, y, h) in numberPlates:
            area = w * h
            if area > minArea:
                frame_with_roi = frame[y:y + h, x:x + w]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, 'Number Plate', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        
        ret, jpeg_frame = cv2.imencode('.jpg', frame)

        if frame_with_roi is not None:
            ret, jpeg_roi = cv2.imencode('.jpg', frame_with_roi)
        else:
            jpeg_roi = None

        return jpeg_frame.tobytes(), jpeg_roi.tobytes() if jpeg_roi is not None else None