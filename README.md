# Document-Scanner

# Install packages/modules
Clone Project from repository:
```
git clone https://github.com/HoDoTenHuy/Document-Scanner.git
```

Create env using Conda:
```
conda create --name env_name python==3.8
```

Activate env:
```
conda activate env_name
```

To install the packages/modules, run the command:
```
python -m pip3 install -r requirements.txt
```

Run app:
```
python app.py --image path/to/image
```

# Building a Document Scanner with OpenCV

Creating a document scanner with OpenCV is a straightforward process that involves three simple steps:

## Step 1: Detect Edges
Utilize OpenCV to detect edges in the image.

## Step 2: Find Contour
Use the detected edges to find the contour (outline) representing the piece of paper being scanned.

## Step 3: Perspective Transform
Apply a perspective transform to obtain the top-down view of the document.

Follow these steps to implement your document scanner using OpenCV and enhance your document processing capabilities.
