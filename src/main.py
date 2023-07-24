import matplotlib.pyplot as plt
from content import add_resume_content
from style import set_style

# Constants
RESUME_PDF_FILENAME = "assets/Example_Resume.pdf"
RESUME_PNG_FILENAME = "assets/Example_Resume.png"
DPI = 300
DECORATIVE_LINE_COLOR = '#007ACC'
DECORATIVE_LINE_ALPHA = 0.0
DECORATIVE_LINE_WIDTH = 50
BACKGROUND_COLOR = 'white'
RESUME_STYLE = set_style()
QR_URL = "example.com"

def create_resume():
    # Setting style for the resume
    RESUME_STYLE

    fig, ax = plt.subplots(figsize=(8.5, 11))

    # Add decorative lines
    ax.axvline(x=.5, ymin=0, ymax=1, color=DECORATIVE_LINE_COLOR, alpha=DECORATIVE_LINE_ALPHA, linewidth=DECORATIVE_LINE_WIDTH)
    plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
    plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

    # Set background color
    ax.set_facecolor(BACKGROUND_COLOR)

    # Remove axes
    plt.axis('off')

    # Add content
    add_resume_content(fig, ax, QR_URL)

    try:
        plt.savefig(RESUME_PDF_FILENAME, format="pdf", bbox_inches="tight")
        plt.savefig(RESUME_PNG_FILENAME, dpi=DPI, bbox_inches='tight')
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")

if __name__ == "__main__":
    create_resume()
