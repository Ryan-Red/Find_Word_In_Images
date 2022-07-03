import pytesseract
import glob 
import re


class ImageFinder:
    def __init__(self, directory, dictExists=False):

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        self.directory = directory
        self.dictExists = dictExists
        self.dict = {}


    def createImageList(self):
        self.imageList = glob.glob(self.directory + "\\*.jpg") + glob.glob(self.directory + "\\*.png")

    def scanImage(self, image):

        # Get the text
        rawText = pytesseract.image_to_string(image).replace("\n", " ")

        #C Clean out any punctuation using regex
        cleanedText = re.sub(r"<>[,.;@#?!&$]+\*", " ", rawText)

        text = list(set(cleanedText.split(" "))) # removing any duplicates by turning the strings into a set, and then back into a list of strings

        for word in text:
            if word in self.dict:
                self.dict[word] = self.dict[word] + [self.directory + "\\" + image]
            else:
                self.dict[word] = [self.directory + "\\" + image]

    def scanAllImages(self):
        for images in self.imageList:
            self.scanImage(images)

    def printKeys(self):
        for key in self.dict.keys():
            print("Key: " + str(key) + " --- Occurances: " + str(len(self.dict[key])))

    def searchWords(self, words):

        resultsDict = {}
        
        text = words.split(" ")

        for word in text:
            if word in self.dict:
                images = self.dict[word]
                for image in images:
                    if image in resultsDict:
                        resultsDict[image] += 1
                    else:
                        resultsDict[image] = 1


        return resultsDict

                

      






