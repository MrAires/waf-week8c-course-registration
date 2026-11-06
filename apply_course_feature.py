from pathlib import Path
import sys
html_path=Path('templates/index.html')
html=html_path.read_text(encoding='utf-8')
if sys.argv[1]=='course':
    addition='            <option>Data Science</option>\n'
    if 'Data Science</option>' not in html:
        html=html.replace('            <option>Software Engineering</option>', '            <option>Software Engineering</option>\n'+addition.rstrip())
elif sys.argv[1]=='collab':
    if 'Contribution: registration instructions' not in html:
        html=html.replace('<h3>Registered Students</h3>', '<p>Contribution: registration instructions - select a course and click Register Course.</p>\n    <h3>Registered Students</h3>')
else:
    raise SystemExit('Usage: python apply_course_feature.py course|collab')
html_path.write_text(html,encoding='utf-8')
print('Updated course registration HTML:',sys.argv[1])
