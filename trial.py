import os
import sys
import traceback
import logging
import cv2
from datetime import datetime

'''
    user-video:
    This program is used to capture User's Face either via System Embedded Webcam or via External Webcam via USB
    Usage: `python main.py Username_DateTime`
    Output: The Video output will be stored in .avi format in `../../Reports/Username_DateTime/final/` folder
'''
try:
    # Read Commandline Arguments
    fullCmdArguments = sys.argv
    # Skip first Argument i.e. `program_name.py`
    argumentList = fullCmdArguments[1:]
    # Read Further Arguments
    incoming_variable = argumentList[0]

    # create logs directory
    if not os.path.isdir('logs/'):
        os.mkdir('logs/')

    # create parent directory for all images
    if not os.path.isdir('data/'):
        os.mkdir('data/')

    image_folder = 'data/' + incoming_variable

    # create output directory to save images
    if not os.path.isdir(image_folder):
        os.mkdir(image_folder)

    counter = 0

    # Define Folder Paths for Read - Write Operations
    logging.basicConfig(filename='logs/' + incoming_variable + '.log', level=logging.DEBUG)

    logging.info('Starting User Video Capture via Webcam')
    # Define Webcam Input
    # 0: System Embedded Webcam
    # 1: External Webcam via USB
    webcam_number = 0
    cap = cv2.VideoCapture(webcam_number)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'avc1')    # `XVID` for avi file

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # read webcam feed frame by frame
            frame = cv2.flip(frame, 1)

            # write the flipped frame
            logging.info(str(datetime.now()) + '\tsaving frame to file')
            print(str(datetime.now()) + '\tsaving frame to file')
            print(str(datetime.now().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3]))
            img_path = os.path.join(
                image_folder,
                str(datetime.now().strftime('%Y-%m-%d %H.%M.%S.%f')[:-3]) + '.png')
            cv2.imwrite(img_path, frame)  # save frame as JPEG file
            # out.write(frame)

            cv2.imshow('User Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info(str(datetime.now()) + '\tExiting while loop from user Video after pressing `q`')
                break
            # To stop duplicate images
            counter += 1
        else:
            logging.info(str(datetime.now()) + '\tExiting while loop from user Capture Video File')
            break

    # Release everything if job is finished
    logging.debug('Releasing Webcam feed')
    cap.release()
    cv2.destroyAllWindows()
except (OSError, ModuleNotFoundError, FileNotFoundError, EOFError, IOError, IndexError) as ose:
    error_trace = traceback.print_exc(file=sys.stdout)
    logging.debug(ose)
    sys.exit()
except NameError as ne:
    error_trace = traceback.print_exc(file=sys.stdout)
    logging.debug(ne)
    print(ne)
    sys.exit()
except ValueError as ve:
    error_trace = traceback.print_exc(file=sys.stdout)
    logging.debug(ve)
    print(ve)
    sys.exit()
