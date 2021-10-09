from website import create_app
from flask import render_template,Response
import cv2

from website.models import User


app = create_app()
camera=cv2.VideoCapture(0)

def generate_frames():
        while True:
                
            ## read the camera frame
            success,frame=camera.read()
            if not success:
                break
            else:
                ret,buffer=cv2.imencode('.jpg',frame)
                frame=buffer.tobytes()

            yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/video')
def video():
        return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)