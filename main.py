import pytesseract
import cv2
from tesseract_local_path import local_path

pytesseract.pytesseract.tesseract_cmd = local_path
