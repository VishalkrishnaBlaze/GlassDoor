import cv2  
  
class add_user:
    def save(self, name):
        """
        Add the users that are known with their names to the residents folder
        """

        # Load the cascade  
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
  
        # To capture video from webcam.   
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  

        # Read the frame  
        _, img = cap.read()  
  
        # Convert to grayscale  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
        # Detect the faces  
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
        # Draw the rectangle around each face  
        for (x, y, w, h) in faces:  
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            faces = img[y:y + h, x:x + w]
            cv2.imwrite(f'Residents/{name}.jpeg', faces)   
        
        print(f"[INFO] Resident {name} added to the database...")

        # Release the VideoCapture object  
        cap.release() 