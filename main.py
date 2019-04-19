import os
import sys
import traceback
import logging
import cv2

"""
    user-video:
    This program is used to capture User's Face either via System Embedded Webcam or via External Webcam via USB
    Usage: `python main.py Username_DateTime`
    Output: The Video output will be stored in .avi format in `../../Reports/Username_DateTime/final/` folder
"""
try:
    # Read Commandline Arguments
    fullCmdArguments = sys.argv
    # Skip first Argument i.e. `program_name.py`
    argumentList = fullCmdArguments[1:]
    # Read Further Arguments
    incoming_variable = argumentList[0]

    # Define Folder Paths for Read - Write Operations
    logging.basicConfig(filename='logs/' + incoming_variable + '.log', level=logging.DEBUG)
    final_folder_path = '../../Reports/' + incoming_variable + '/final/'
    logging.info('Final Folder Path:\t' + final_folder_path)

    logging.info('Starting User Video Capture via Webcam')
    # Define Webcam Input
    # 0: External Webcam via USB
    # 1: System Embedded Webcam
    webcam_number = 0
    cap = cv2.VideoCapture(webcam_number)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    filename = final_folder_path + incoming_variable + '_User.avi'
    logging.info('Filename for User Video saving is:\t' + filename)

    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
    # Make a New Directory to Store final Data files i.e. `final/`
    if not os.path.exists(final_folder_path):
        os.mkdir(final_folder_path)
        print('Directory ', final_folder_path, ' Created ')
        logging.info('Directory ' + str(final_folder_path) + ' Created ')
    else:
        print('Directory ', final_folder_path, ' already exists')
        logging.info('Directory ' + str(final_folder_path) + ' already exists ')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # read webcam feed frame by frame
            logging.info('reading frame from webcam')
            frame = cv2.flip(frame, 1)

            # write the flipped frame
            logging.info('writing frame to video file')
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info('Exiting while loop from user Capture Video File')
                break
        else:
            logging.info('Exiting while loop from user Capture Video File')
            break

    # Release everything if job is finished
    logging.debug('Releasing Webcam feed')
    cap.release()
    out.release()
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
