import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
css_dir = base_dir
components_dir = os.path.join(css_dir, 'components')

if not os.path.exists(components_dir):
    os.makedirs(components_dir)

style_path = os.path.join(css_dir, 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define sections to extract
sections = [
    ("NAV", "nav.css"),
    ("HERO", "hero.css"),
    ("SERVICES SECTION - PREMIUM REDESIGN", "services.css"),
    ("CAR FLEET - PREMIUM DESIGN", "fleet.css"),
    ("WHY US - PREMIUM DESIGN", "why.css"),
    ("REVIEWS - PREMIUM DESIGN", "reviews.css"),
    ("PREMIUM FORMS", "forms.css"),
    ("ROUTE PAGE - SEO LANDING PAGES", "route.css"),
    ("FOOTER - PREMIUM DESIGN", "footer.css")
]

imports = []
remaining_content = content

for section_name, filename in sections:
    # Look for the section comment and the start of the next section comment (or EOF)
    pattern = r'(/\*\s*' + re.escape(section_name) + r'\s*\*/.*?)(?=/\*\s*[A-Z0-9\- ]+\s*\*/|\Z)'
    match = re.search(pattern, remaining_content, re.DOTALL)
    if match:
        section_content = match.group(1)
        with open(os.path.join(components_dir, filename), 'w', encoding='utf-8') as f:
            f.write(section_content.strip() + '\n')
        remaining_content = remaining_content.replace(match.group(0), '')
        imports.append(f'@import url("components/{filename}");')

# Write the new style.css with imports at the top
new_style_content = '\n'.join(imports) + '\n\n' + remaining_content.strip() + '\n'

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(new_style_content)

print("Modularized CSS successfully.")
