import cv2
import face_recognition

# Görüntüyü yükleme
image = cv2.imread('example.jpg')

# Görüntüdeki yüzleri algılama
face_locations = face_recognition.face_locations(image)

# Her bir yüzün koordinatlarını yazdırma
for face_location in face_locations:
    top, right, bottom, left = face_location
    # Algılanan yüzün etrafına dikdörtgen çizme
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Sonucu gösterme
cv2.imshow('Image with faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
