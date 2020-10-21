from pytesseract import Output
import argparse
import cv2
import pytesseract
import text_to_speech


def convert(imagePath):
    
 
	# load the input image, convert it from BGR to RGB channel ordering,
	# and use Tesseract to localize each area of text in the input image
	#image = cv2.imread(args["image"])
	min_conf = 0
	print(imagePath)
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
	finalText = []

	# loop over each of the individual text localizations
	for i in range(0, len(results["text"])):
		# extract the bounding box coordinates of the text region from
		# the current result
		x = results["left"][i]
		y = results["top"][i]
		w = results["width"][i]
		h = results["height"][i]
		# extract the OCR text itself along with the confidence of the
		# text localization
		text = results["text"][i]
		conf = int(results["conf"][i])
		
 		# filter out weak confidence text localizations
		if conf > min_conf:
			if(text != ',' or text != ', '):
				finalText.append(text)
			# display the confidence and text to our terminal
			#print("Confidence: {}".format(conf))
			#print("Text: {}".format(text))
			#print("")
			# strip out non-ASCII text so we can draw the text on the image
			# using OpenCV, then draw a bounding box around the text along
			# with the text itself
			text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
			#cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
				#1.2, (0, 0, 255), 3)
	# show the output image
	cv2.imshow("Image", image)
	cv2.imwrite("output.png", image)
	print(finalText)
	text_to_speech.saySentence(finalText)
	#cv2.waitKey(0)



#convert("currentFramemod3.png")