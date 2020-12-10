#!d:\AMAZON_ALEXA\Projects\magenta\hw_skill\skill-my-skill-python\.venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'skill-sdk','console_scripts','new-skill'
__requires__ = 'skill-sdk'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('skill-sdk', 'console_scripts', 'new-skill')()
    )
