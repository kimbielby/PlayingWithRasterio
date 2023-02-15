# TODO:
#  1. Get image and find top-left and bottom-right geocoords in it
#  2. Calc all possible geolocation x-y points in the image
#  3. Search the general geojson file to find every possible bounding box within the image
#  4. For all bounding boxes found, save them in a new geojson file for that image
#  5. Convert geocoords from each bounding box to pixel x-y coords
#  6. Save the pixel x-y coords in a json file with headings needed for csv

# todo (shouldbeworking2.tif):
#  1. top-left geocoord is: 279255.7771, 693690.5070378605
#     bottom-right geocoord is: 279521.4213, 693507.1507621396
#  2. min-x: 279255.7771
#     max-x: 279521.4213
#     min-y: 693507.1507621396
#     max-y: 693690.5070378605
#  3. geocoords need to be:
#     more than 279255.7771, 693507.1507621396
#     less than 279521.4213, 693690.5070378605