# Python Resume Generator

This repository contains Python scripts for generating a professional resume, complete with QR code. The final resume can be saved in PDF or PNG format.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Running the Project](#running-the-project)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [Credit](#credit)

## Getting Started

1. Ensure that you have `Python 3.11.2` and `pipenv` installed on your machine.
2. Clone this repository to your local machine using `git clone https://github.com/neo-con/Resume.git`
3. Navigate to the directory where you cloned the repository.
4. Run `pipenv install` to install the necessary Python libraries.

## Prerequisites

The scripts use the `matplotlib` and `qrcode` packages. Install them with `pipenv` (see above).

## Running the Project

To generate a resume, simply run the main.py script:

`python3 main.py`

This will create a resume in PDF and PNG format, saving it in the assets directory.

## Code Overview

The project contains several Python scripts, each serving a specific purpose:

- `main.py`: The entry point of the application. This script combines all the elements and generates the final resume.

```python
if __name__ == "__main__":
    create_resume()
```

- `qr_code.py`: This script handles the generation of the QR code.
  
```python
def add_qr_code(fig, ax, url):
    qr_code = create_qr_code(url)
    imagebox = OffsetImage(plt.imread(qr_code), zoom=0.2)
    ab = AnnotationBbox(imagebox, (0.84, 0.12))
    ax.add_artist(ab)
```

- `style.py:` This script defines the overall style of the resume.

```python
def set_style():
    # Set font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'STIXGeneral'
```

- `text_constants.py`: This script contains the text content for the resume. UPDATE YOUR INFORMATION HERE.
  
```python
Header = '>>This resume vitae was synthesized entirely utilizing Python.'
Name = 'JANE SMITH'
Title = 'AI Enthusiast & Entrepreneurial Technologist'
...
```
- `content.py`: This script manages the addition of content to the resume.
  
```python
def add_resume_content(fig, ax, url):
    # Add text
    add_text(ax)

    # Add QR code
    add_qr_code(fig, ax, url)
```

## Contributing

Contributions are welcome. Please open an issue to discuss your suggestion or open a pull request with your changes.


## Credit

This project was inspired by a [write-up](https://towardsdatascience.com/generating-a-resume-in-python-1480a4d6a399) by Eddie Kirkland on generating a Python resume. You can view the original work on his [GitHub](https://github.com/e-kirkland/datascience/tree/master/Resume).
