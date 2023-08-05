# Motion Detection Application

The Motion Detection Application is a Python script that captures video from a camera and detects motion in the video frames using OpenCV. It saves the start and end times of each motion event to a CSV file and generates a motion graph using the Bokeh library.

## Requirements

- Python 3.x
- OpenCV
- pandas
- Bokeh

## Installation

1. Clone the repository or download the script.

git clone https://github.com/your-username/motion-detection.git

2. Install the required libraries using pip.

pip install opencv-python pandas bokeh

## Usage

1. Run the script.

python main.py

2. The script will capture video from the default camera. When motion is detected, it will save the start and end times of the motion event.

3. The motion events will be saved to a CSV file named "Times.csv".

4. A motion graph will be generated and saved as "Graph.html".

## Customization

- You can modify the threshold value (`30`) in the script to adjust the sensitivity of motion detection. Lower values may detect more subtle movements, while higher values may require more significant motion to trigger detection.
- The minimum contour area (`10000`) can also be adjusted to filter out smaller or larger contours based on your requirements.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

This project was inspired by the need to develop a simple motion detection system using Python and OpenCV. Special thanks to the contributors of the OpenCV, pandas, and Bokeh libraries for providing the tools necessary to build this application.

