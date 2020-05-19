import io
import time
import picamera
from base_camera import BaseCamera

FRAMERATE_FPS = 10

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera(resolution=(320,240)) as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                start_time = time.time()
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # Wait for the target framerate
                time.sleep(max(0, 1/FRAMERATE_FPS - (time.time() - start_time)))
