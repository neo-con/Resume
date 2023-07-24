import matplotlib.pyplot as plt

from qr_code import add_qr_code
from text_constants import *


def add_resume_content(fig, ax, url):
    # Add text
    add_text(ax)

    # Add QR code
    add_qr_code(fig, ax, url)


def add_text(ax):
    # Header, Name, Title, and Contact
    plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
    plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
    plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
    plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')

    # Projects
    plt.annotate(ProjectsHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
    plt.annotate(ProjectOneTitle, (.02,.832), weight='bold', fontsize=10)
    plt.annotate(ProjectOneDesc, (.04,.78 + 0.015), weight='regular', fontsize=9)
    plt.annotate(ProjectTwoTitle, (.02,.745+ 0.015), weight='bold', fontsize=10)
    plt.annotate(ProjectTwoDesc, (.04,.71+ 0.03), weight='regular', fontsize=9)
    plt.annotate(ProjectThreeTitle, (.02,.672+ 0.03), weight='bold', fontsize=10)
    plt.annotate(ProjectThreeDesc, (.04,.638+ 0.03), weight='regular', fontsize=9)
    #plt.annotate(Portfolio, (.02,.6), weight='bold', fontsize=10)

    # Experience
    plt.annotate(WorkHeader, (.02,.600+0.03), weight='bold', fontsize=10, color='#58C1B2')
    plt.annotate(WorkOneTitle, (.02,.572+0.03), weight='bold', fontsize=10)
    plt.annotate(WorkOneTime, (.02,.557+0.03), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkOneDesc, (.04,.445+0.03), weight='regular', fontsize=9)
    plt.annotate(WorkTwoTitle, (.02,.4+0.03), weight='bold', fontsize=10)
    plt.annotate(WorkTwoTime, (.02,.385+0.03), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkTwoDesc, (.04,.337+0.03), weight='regular', fontsize=9)
    plt.annotate(WorkThreeTitle, (.02,.295+0.03), weight='bold', fontsize=10)
    plt.annotate(WorkThreeTime, (.02,.28+0.03), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkThreeDesc, (.04,.247+0.018), weight='regular', fontsize=9)
    plt.annotate(WorkFourTitle, (.02,.202+0.03), weight='bold', fontsize=10)
    plt.annotate(WorkFourTime, (.02,.187+0.03), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(WorkFourDesc, (.04,.154+0.03), weight='regular', fontsize=9)

    #Education
    plt.annotate(EduHeader, (.02,.185 -0.035), weight='bold', fontsize=10, color='#58C1B2')
    plt.annotate(EduOneTitle, (.02,.155-0.035), weight='bold', fontsize=10)
    plt.annotate(EduOneTime, (.02,.14-0.035), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(EduOneDesc, (.04,.125-0.035), weight='regular', fontsize=9)
    plt.annotate(EduTwoTitle, (.02,.08-0.035), weight='bold', fontsize=10)
    plt.annotate(EduTwoTime, (.02,.065-0.035), weight='regular', fontsize=9, alpha=.6)
    plt.annotate(EduTwoDesc, (.04,.05-0.035), weight='regular', fontsize=9)

    # Skills and Extras
    plt.annotate(SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
    plt.annotate(SkillsDesc, (.7,.56), weight='regular', fontsize=10, color='#ffffff')
    plt.annotate(ExtrasTitle, (.7,.43), weight='bold', fontsize=10, color='#ffffff')
    plt.annotate(ExtrasDesc, (.7,.345), weight='regular', fontsize=10, color='#ffffff')
    plt.annotate(CodeTitle, (.7,.2), weight='bold', fontsize=10, color='#ffffff')