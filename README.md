# Computer-Vision-w-MS
Computer Vision Project with MicroSoft Cognitive Service (Oxford Project) API

https://www.microsoft.com/cognitive-services/en-us/computer-vision-api


## Analyze an image  

This feature returns information about visual content found in an image. Use tagging, descriptions and domain-specific models to identify content and label it with confidence. Apply the adult/racy settings to enable automated restriction of adult content. Identify image types and color schemes in pictures.


## Processing

Connect to the API

Get the responses from the Cognitive Service

Decode the json file to csv format

### Example 
Features:
Feature Name	Value
Description	{ "type": 0, "captions": [ { "text": "a man swimming in a pool of water", "confidence": 0.7850108693093019 } ] }
Tags	[ { "name": "water", "confidence": 0.9996442794799805 }, { "name": "sport", "confidence": 0.9504992365837097 }, { "name": "swimming", "confidence": 0.9062818288803101, "hint": "sport" }, { "name": "pool", "confidence": 0.8787588477134705 }, { "name": "water sport", "confidence": 0.631849467754364, "hint": "sport" } ]
Image Format	jpeg
Image Dimensions	1500 x 1155
Clip Art Type	0 Non-clipart
Line Drawing Type	0 Non-LineDrawing
Black & White Image	False
Is Adult Content	False
Adult Score	0.14916780591011047
Is Racy Content	False
Racy Score	0.12426207214593887
Categories	[ { "name": "people_swimming", "score": 0.98046875 } ]
Faces	[ { "age": 28, "gender": "Male", "faceRectangle": { "left": 744, "top": 338, "width": 305, "height": 305 } } ]
