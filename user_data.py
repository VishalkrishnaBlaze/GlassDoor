# Importing required libraries
import cv2
import os  
  
class user:
    def add_user(self, name):
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
        
        if os.path.exists(f"./Residents/{name}.jpeg"):
            print(f"[INFO] Resident {name} added to the database...")
            cv2.imshow(f'User', faces)
            cv2.waitKey(0)

        else:
            print("Please try again.")

        # Release the VideoCapture object  
        cap.release()

    def delete_user(self, name):
        """
        Delete the user from the residents folder
        """

        # If the user exists delete it, else throw 'user not found'
        if os.path.exists(f"./Residents/{name}.jpeg"):
            os.remove(f"./Residents/{name}.jpeg")
            print(f"[INFO] The user {name} removed from the database")
        else:
            print("[INFO] The user does not exist")

    def list_users(self):
        """
        List out all the names of known user's faces 
        """

        # Create an empty list to save names
        user_list = []

        # Go the the directory with saved  images
        Resident_images_location = os.path.abspath('.')+'//Residents//'
        
        if len(os.listdir(Resident_images_location)) == 0:
            print("[INFO] No saved users.")

        else:    
            # Loop over all the files if ends with '.jpeg append the name to the list
            for user_image_location in os.listdir(Resident_images_location):
                if user_image_location.endswith('.jpeg'):
                    user_list.append(user_image_location[:-5])
            print(*user_list, sep = "\n")
            del user_list, Resident_images_location, user_image_location