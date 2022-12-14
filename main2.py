############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import pyttsx3



    ############################################# FUNCTIONS ################################################
sound_engine=pyttsx3.init("sapi5")
jarvis_voices=sound_engine.getProperty("voices")
sound_engine.setProperty("voice",jarvis_voices[0].id)

def jarvis_speak(audio):
    
    # say method on the sound_engine that passing input text to be spoken
    sound_engine.say(audio)
    # run and wait method, it processes the voice commands. 
    sound_engine.runAndWait()    


##################################################################################
def gender():
    sound_engine=pyttsx3.init("sapi5")
    jarvis_voices=sound_engine.getProperty("voices")
    sound_engine.setProperty("voice",jarvis_voices[0].id)
    


    def jarvis_speak(audio):
    
        # say method on the sound_engine that passing input text to be spoken
        sound_engine.say(audio)
        # run and wait method, it processes the voice commands. 
        sound_engine.runAndWait()

    def faceBox(faceNet,frame):
        frameHeight=frame.shape[0]
        frameWidth=frame.shape[1]
        blob=cv2.dnn.blobFromImage(frame, 1.0, (300,300), [104,117,123], swapRB=False)
        faceNet.setInput(blob)
        detection=faceNet.forward()
        bboxs=[]
        for i in range(detection.shape[2]):
            confidence=detection[0,0,i,2]
            if confidence>0.7:
                x1=int(detection[0,0,i,3]*frameWidth)
                y1=int(detection[0,0,i,4]*frameHeight)
                x2=int(detection[0,0,i,5]*frameWidth)
                y2=int(detection[0,0,i,6]*frameHeight)
                bboxs.append([x1,y1,x2,y2])
                cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0), 1)
        return frame, bboxs


    faceProto = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\competitiveprograming\\JARVIS\\opencv_face_detector.pbtxt"
    faceModel = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\competitiveprograming\\JARVIS\\opencv_face_detector_uint8.pb"

    ageProto = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\competitiveprograming\\JARVIS\\age_deploy.prototxt"
    ageModel = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\competitiveprograming\\JARVIS\\age_net.caffemodel"

    genderProto = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\competitiveprograming\\JARVIS\\gender_deploy.prototxt"
    genderModel = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\competitiveprograming\\JARVIS\\gender_net.caffemodel"



    faceNet=cv2.dnn.readNet(faceModel, faceProto)
    ageNet=cv2.dnn.readNet(ageModel,ageProto)
    genderNet=cv2.dnn.readNet(genderModel,genderProto)

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
    genderList = ['Male', 'Female']


    video=cv2.VideoCapture(0)

    padding=20

    while True:
        ret,frame=video.read()
        frame,bboxs=faceBox(faceNet,frame)
        for bbox in bboxs:
            # face=frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
            face = frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
            blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPred=genderNet.forward()
            gender=genderList[genderPred[0].argmax()]


            ageNet.setInput(blob)
            agePred=ageNet.forward()
            age=ageList[agePred[0].argmax()]


            label="{},{}".format(gender,age)         
            cv2.rectangle(frame,(bbox[0], bbox[1]-30), (bbox[2], bbox[1]), (0,255,0),-1) 
            cv2.putText(frame, label, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2,cv2.LINE_AA)
        #cv2.imshow("Age-Gender",frame)
        k=cv2.waitKey(1)
    

        jarvis_speak("pleace lean your face in your webcam")
        
        try: 
            if k==ord('q') or gender=="Male" or gender=="Female":
                
                #print(gender)
                
                jarvis_speak("becouse")
                jarvis_speak("i want to identify weather you are male object or female object")  
                hour=int(datetime.datetime.now().hour)
                if   gender=="Male" :
                    if hour>=0 and hour<12:
                        jarvis_speak("i detected you are a male object ")
                        jarvis_speak("very good morning")
                    elif hour>=12 and hour<18:
                        jarvis_speak("i detected you are a male object ")
                        
                        jarvis_speak("very good afternoon  ")
                    else:
                        jarvis_speak("i detected you are a male object ")
                        
                        jarvis_speak("verygood evening ")            
                    
                    jarvis_speak("wellcom  to  apec  college  of  engineering") 
                   
       
                elif gender=="Female":
                    if hour>=0 and hour<12:
                        jarvis_speak("i detected you are a female object ")
                        
                        jarvis_speak("very good morning ")
                    elif hour>=12 and hour<18:
                        jarvis_speak("i detected you are a female object ")
                        
                        jarvis_speak("very good afternoon ")
                    else:
                        jarvis_speak("i detected you are a female object ")
                        
                        jarvis_speak("very good evening ")            
                    jarvis_speak("wellcom  to  apec  college  of  engineering") 
                
                break
        except Exception as e:
            jarvis_speak("the face is not detect") 
            break  
          

    video.release()
    cv2.destroyAllWindows()

     
def attd():
    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def quiting():
        jarvis_speak("thank you ,    have a nice day")
        window.destroy()     

    def mannule():
        jarvis_speak("hear is your user manule") 
        mess._show(title='USER MANULE', message="FOR MEMBERSHIPED STUDENTS:-\n\n\n--> TO TAKE ATTENDANCE ,CLICK TAKE ATTENDANCE BUTTON\n\n--> TO QUIT,CLICK QUICK BUTTON\n\n\nFOR NON-MEMBERSHIPED STUDENTS\n\n\n--> ENTER YOUR ID\n\n-->ENTER YOUR NAME\n\n-->CLICK TAKE IMAGE TO TAKE IMAGE\n\n-->CLICK SAVE PROFILE TO SAVE THE PROFILE")      

    ##################################################################################

    def tick():
        time_string = time.strftime('%H:%M:%S')
        clock.config(text=time_string)
        clock.after(200,tick)

    ###################################################################################

    def contact():
        jarvis_speak("Please contact us on : 'gokulmadyy@gmail.com' ")
        mess._show(title='Contact us', message="Please contact us on : 'gokulmadyy@gmail.com' ")

    ###################################################################################

    def check_haarcascadefile():
        exists = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            jarvis_speak("Please contact us for help on gokulmadyy@gmail.com")
            mess._show(title='Some file missing', message='Please contact us for help')
            
            window.destroy()

    ###################################################################################

    def save_pass():
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel")
        exists1 = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt")
        if exists1:
            tf = open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt", "r")
            key = tf.read()
        else:
            master.destroy()
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                jarvis_speak("Password not set!! Please try again")
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
                
            else:
                tf = open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt", "w")
                tf.write(new_pas)
                jarvis_speak("New password was registered successfully!!")
                mess._show(title='Password Registered', message='New password was registered successfully!!')
               
                return
        op = (old.get())
        newp= (new.get())
        nnewp = (nnew.get())
        if (op == key):
            if(newp == nnewp):
                txf = open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt", "w")
                txf.write(newp)
            else:
                jarvis_speak("Confirm new password again!!!")
                mess._show(title='Error', message='Confirm new password again!!!')
                
                return
        else:
            jarvis_speak("Please enter correct old password.")
            mess._show(title='Wrong Password', message='Please enter correct old password.')
            return
        jarvis_speak("Password changed successfully!!")    
        mess._show(title='Password Changed', message='Password changed successfully!!')
        
        master.destroy()

    ###################################################################################

    def change_pass():
        global master
        master = tk.Tk()
        master.geometry("400x160")
        master.resizable(False,False)
        master.title("Change Password")
        master.configure(background="white")
        lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
        lbl4.place(x=10,y=10)
        global old
        old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
        old.place(x=180,y=10)
        lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
        lbl5.place(x=10, y=45)
        global new
        new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
        new.place(x=180, y=45)
        lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
        lbl6.place(x=10, y=80)
        global nnew
        nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
        nnew.place(x=180, y=80)
        cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
        cancel.place(x=200, y=120)
        save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
        save1.place(x=10, y=120)
        master.mainloop()

    #####################################################################################

    def psw():
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel")
        exists1 = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt")
        if exists1:
            tf = open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("TC:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\psd.txt", "w")
                tf.write(new_pas)
                jarvis_speak("New password was registered successfully!!")
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('Password', 'Enter Password', show='*')
        if (password == key):
            TrainImages()
        elif (password == None):
            pass
        else:
            jarvis_speak("You have entered wrong password")
            mess._show(title='Wrong Password', message='You have entered wrong password')

    ######################################################################################

    def clear():
        txt.delete(0, 'end')
        res = "Take Images  --->  Save Profile"
        message1.configure(text=res)


    def clear2():
        txt2.delete(0, 'end')
        res = "Take Images  --->  Save Profile"
        message1.configure(text=res)

    #######################################################################################

    def TakeImages():
        check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails")
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImage\\sample_image/")
        serial = 0
        exists = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv")
        if exists:
            with open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 0
            csvFile1.close()
        Id = (txt.get())
        name = (txt2.get())
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            jarvis_speak("pleace lean your face in your webcam")  
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImage\\sample_image/" + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    jarvis_speak("the object trained successfully")
                    
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            row = [serial, '', Id, '', name]
            with open('C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message1.configure(text=res)
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                message.configure(text=res)

    ########################################################################################

    def TrainImages():
        check_haarcascadefile()
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = getImagesAndLabels("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImage\\sample_image/")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            jarvis_speak("Please Register someone first!!!")
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\Trainner.yml")
        res = "Profile Saved Successfully"
        message1.configure(text=res)
        message.configure(text='Total Registrations till now  : ' + str(ID[0]))

    ############################################################################################3

    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids

    ###########################################################################################

    def TrackImages():
        check_haarcascadefile()
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\Attendance")
        assure_path_exists("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails")
        for k in tv.get_children():
            tv.delete(k)
        msg = ''
        i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\Trainner.yml")
        if exists3:
            recognizer.read("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\TrainingImageLabel\\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv")
        if exists1:
            df = pd.read_csv("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv")
        else:
            mess._show(title='Details Missing', message='Students details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
            window.destroy()
        jarvis_speak("pleace lean your face in your webcam")    
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

                else:
                    Id = 'Unknown'
                    bb = str(Id)
                   
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
                
            cv2.imshow('Taking Attendance', im)
            k=cv2.waitKey(1)           
            if (k== ord('q')) or ret==False:
                cv2.putText(im, jarvis_speak(str(bb)), (x, y + h), font, 1, (255, 255, 255), 2)
                jarvis_speak("the attendence is taken successfully")
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\Attendance\\Attendance_" + date + ".csv")
        if exists:
            with open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\Attendance\\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\Attendance\\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\Attendance\\Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()

    ######################################## USED STUFFS ############################################
        
    global key
    key = ''

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    day,month,year=date.split("-")

    mont={'01':'January',
        '02':'February',
        '03':'March',
        '04':'April',
        '05':'May',
        '06':'June',
        '07':'July',
        '08':'August',
        '09':'September',
        '10':'October',
        '11':'November',
        '12':'December'
        }

    ######################################## GUI FRONT-END ###########################################
    
    window = tk.Tk()
    window.geometry("1280x720")
    window.resizable(True,False)
    window.title("Attendance System")
    window.configure(background='#11294f')

    frame1 = tk.Frame(window, bg="#0a476e")
    frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

    frame2 = tk.Frame(window, bg="#0a476e")
    frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

    message3 = tk.Label(window, text="ATTENDANCE MONITARING SYSTEM BY FACE RECOGNITION" ,fg="#ffffff",bg="#11294f" ,width=55 ,height=1,font=('Copperplate Gothic Bold', 23, ' bold '))
    message3.place(x=10, y=10)

    frame3 = tk.Frame(window, bg="#c4c6ce")
    frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

    frame4 = tk.Frame(window, bg="#11294f")
    frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

    datef = tk.Label(frame4, text = "  |  "+day+"-"+mont[month]+"-"+year+"  |  ", fg="#ffffff",bg="#11294f" ,width=55 ,height=1,font=('Linux', 14, ' bold '))
    datef.pack(fill='both',expand=1)

    clock = tk.Label(frame3,fg="orange",bg="#11294f" ,width=55 ,height=1,font=('Linux', 14, ' bold '))
    clock.pack(fill='both',expand=1)
    tick()

    head2 = tk.Label(frame2, text="        FOR NEW REGISTRATION                       ", fg="#ffffff",bg="#0666a1" ,font=('Copperplate Gothic Bold', 17, ' bold ') )
    head2.grid(row=0,column=0)

    head1 = tk.Label(frame1, text="        FOR ALREADY REGISTRATION                        ", fg="#ffffff",bg="#0666a1" ,font=('Copperplate Gothic Bold', 17, ' bold ') )
    head1.place(x=0,y=0)


    lbl = tk.Label(frame2, text="Enter ID           ",width=20  ,height=1  ,fg="#03e6ff"  ,bg="#0a476e" ,font=('Copperplate Gothic Bold', 17, ' bold ') )
    lbl.place(x=80, y=55)
   

    txt = tk.Entry(frame2,width=32 ,fg="black",font=('NSimSun', 15, ' bold '))
    txt.place(x=30, y=88)

    lbl2 = tk.Label(frame2, text="Enter Name            ",width=20  ,fg="#03e6ff"  ,bg="#0a476e" ,font=('Copperplate Gothic Bold', 17, ' bold '))
    lbl2.place(x=80, y=140)
    

    txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('NSimSun', 15, ' bold ')  )
    txt2.place(x=30, y=173)

    message1 = tk.Label(frame2, text="Take Images  --->  Save Profile       " ,bg="#0666a1" ,fg="#03e6ff"  ,width=50 ,height=1, activebackground = "yellow" ,font=('NSimSun', 15, ' bold '))
    message1.place(x=1, y=230)

    message = tk.Label(frame2, text="" ,bg="#0666a1" ,fg="#ffffff"  ,width=50,height=1, activebackground = "yellow" ,font=('NSimSun', 15, ' bold '))
    message.place(x=-30, y=450)

    lbl3 = tk.Label(frame1, text="ATTENDANCE                                   ",width=50  ,fg="#ffffff"  ,bg="#0666a1"  ,height=1 ,font=('Copperplate Gothic Bold', 17, ' bold '))
    lbl3.place(x=-85, y=115)

    res=0
    exists = os.path.isfile("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv")
    if exists:
        with open("C:\\Users\\Madesh\\Desktop\\gokulpythonprogeaming\\FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM\\StudentDetails\\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0 
        
    message.configure(text='Total Registrations till now  : '+str(res))

    ##################### MENUBAR #################################

    menubar = tk.Menu(window,relief='ridge')
    filemenu = tk.Menu(menubar,tearoff=0)
    filemenu.add_command(label='Change Password', command = change_pass)
    filemenu.add_command(label='Contact Us', command = contact)
    filemenu.add_command(label='Exit',command = quiting)
    filemenu.add_command(label='Manule',command = mannule)

    menubar.add_cascade(label='Help',font=('Open Sans Bold', 29, ' bold '),menu=filemenu)

    ################## TREEVIEW ATTENDANCE TABLE ####################

    tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
    tv.column('#0',width=82)
    tv.column('name',width=130)
    tv.column('date',width=133)
    tv.column('time',width=133)
    tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
    tv.heading('#0',text ='ID')
    tv.heading('name',text ='NAME')
    tv.heading('date',text ='DATE')
    tv.heading('time',text ='TIME')

    ##################### SCROLLBAR ################################

    scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
    scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
    tv.configure(yscrollcommand=scroll.set)

    ###################### BUTTONS ##################################

    clearButton = tk.Button(frame2, text="Clear", command=clear  ,fg="#03e6ff"  ,bg="#0666a1"  ,width=11 ,activebackground = "#23bddb" ,font=('NSimSun', 15, ' bold '))
    clearButton.place(x=335, y=86)
    clearButton2 = tk.Button(frame2, text="Clear", command=clear2  ,fg="#03e6ff"  ,bg="#0666a1"  ,width=11 , activebackground = "#23bddb" ,font=('NSimSun', 15, ' bold '))
    clearButton2.place(x=335, y=172)    
    takeImg = tk.Button(frame2, text="Take Images", command=TakeImages  ,fg="#03e6ff"  ,bg="#135da8"  ,width=34  ,height=1, activebackground = "#23bddb" ,font=('NSimSun', 15, ' bold '))
    takeImg.place(x=50, y=300)
    trainImg = tk.Button(frame2, text="Save Profile", command=psw ,fg="#03e6ff"  ,bg="#135da8"  ,width=34  ,height=1, activebackground = "#23bddb" ,font=('NSimSun', 15, ' bold '))
    trainImg.place(x=50, y=380)
    trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages  ,fg="#03e6ff"  ,bg="#135da8"  ,width=35  ,height=1, activebackground = "#23bddb" ,font=('NSimSun', 15, ' bold '))
    trackImg.place(x=50,y=54)
    quitWindow = tk.Button(frame1, text="QUIT", command=quiting  ,fg="#03e6ff"  ,bg="#0666a1"  ,width=35 ,height=1, activebackground = "#23bddb" ,font=('NSimSun', 15, ' bold '))
    quitWindow.place(x=50, y=475)
    

    ##################### END ######################################

    window.configure(menu=menubar)
    window.mainloop()

    ####################################################################################################
if __name__ == "__main__" :   
    gender()
    attd()
