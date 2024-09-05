# Oil Paint Color Utility (OPMXR)

OPMXR is a command-line utility for working with oil paint colors. It provides various functionalities such as finding the closest oil paint color to a given RGB value, mixing colors to achieve a target color, and listing available oil paint colors.

## Features

- Find the closest oil paint color for a given RGB value
- Get the RGB value for a given oil paint color name
- Suggest a mix of basic pigments to achieve a desired color
- Mix colors to achieve a given color name
- List all available oil paint colors

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/gv-sh/opmxr.git
   cd opmxr
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script using `python opmxr.py` followed by the desired command and arguments. Here are some examples:

1. Find the closest oil paint color:
   ```
   python opmxr.py closest-color 227 0 34
   ```

2. Get the RGB value for a color name:
   ```
   python opmxr.py color-rgb "Cadmium Red"
   ```

3. Mix colors to achieve a target RGB:
   ```
   python opmxr.py mix-color 227 0 34 --complexity high
   ```

4. Mix colors to achieve a given color name:
   ```
   python opmxr.py mix-name "Cadmium Red" --complexity medium
   ```

5. List all available colors:
   ```
   python opmxr.py list-colors
   ```

Use the `--help` option to see all available commands and options.

## Running Tests

To run the unit tests, execute the following command from the project root directory:
```
python -m unittest tests.py
```