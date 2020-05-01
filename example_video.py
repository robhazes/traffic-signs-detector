import os

from detector.detector import create_detector_from_file

import settings


detector = create_detector_from_file('./cfg/config.json')
in_file = settings.IN_FILE
out_file = settings.OUT_FILE
detector.detect_video_feed(in_file, show_output=True, output=out_file)
