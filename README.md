# Data Augmentation
A simple GPU-based image-enhancing tool for YOLO-labeled images written in python. <br/>
The image-enhancer are called `Augmenters` and they all implement the _**abstract class**_ `Augmenter`. <br/>

Each augmenter has: 
- an `__init__` constructor 
- a `transform` method which takes in a `PIL` Image and returns the transformed image as a NumPy array
- a `get_transformed_YOLO_values` method which takes the original YOLO label values of an image and returns the transformed ones
- a `get_augmenter_signature` method which returns a string containing the abbreviated name of the augmenter  <br/>

The base `Augmenter` abstract class also defines some utility methods to convert image to NumPy arrays and viceversa. <br/>

The currently available augmenters are:
- `AugmenterBlur`
- `AugmenterContrastBrightness`
- `AugmenterGrayscale`
- `AugmenterHFlip`
- `AugmenterVFlip`
- `AugmenterHShear`
- `AugmenterVShear`
- `AugmenterNoise`
- `AugmenterRotate`
- `AugmenterScale`
- `AugmenterSharp`
- `AugmenterTraslate`

---

The project also contains the `ImageManager` and the `LabelManager` _**abstract classes**_ which extend the `FileManager` _**abstract class**_ and that define many files/images/YOLO labels manipulation methods to smooth out the file-system related parts of the data-augmentation/image-enhancement. <br/>

The available implementations of these classes are called: 
- `ImageManagerImpl`
- `LabelManagerImpl`

---

A high level class for directly transforming images and their labels is also provided and it's called `WorkerImpl` which is based upon the `Worker` _**abstrac class**_ and exposes the `transform_images_and_YOLO_labels` method.

Testers can be found in the `Testers` directory.

--- 

## Authors:
Cristian Davide Conte <br/>
Simone Morelli
