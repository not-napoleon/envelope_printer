"""
Python script for building LaTeX envlab formatted envelope list
"""
import subprocess
import os
import csv

# TODO: pull these from command line args
TEMPLATE_FILE='envelopes_template.tex'
DATA_FILE='addresses.csv'
RESULT_FILE = 'envelopes.tex'

ADDRESS_LINE="\mlabel{%%\n%(from_address)s}{%%\n%(to_address)s}"

def build_addresses(to_addresses):
  """Build the formatted address list from the given file-like object
  """
  format_vars = {
      'from_address':
          r'Mark and Karen Tozzi\\1404 Duckwall Road\\Berkeley Springs, WV 25411',
  }

  addresses = []
  for to_address in to_addresses:
    to_address = to_address.strip()
    if to_address == '':
      continue
    format_vars['to_address'] = to_address
    addresses.append(ADDRESS_LINE % format_vars)
  return addresses

def render_template(template_file, addresses):
  """Plug the address list into the TeX document
  """
  with open(template_file) as infile:
    template = infile.read()

  result = template % '\n'.join(addresses)
  return result


if __name__ == '__main__':
  to_addresses = []
  with open(DATA_FILE, 'rb') as raw:
    for line in csv.reader(raw):
      line = [field.strip() for field in line if field != '']
      tex_formatted = r"\\".join(line)
      for char in ('&', '#'):
        tex_formatted = tex_formatted.replace(char, r'\%s' % char)
      to_addresses.append(tex_formatted)

  rendered = render_template(TEMPLATE_FILE, build_addresses(to_addresses))
  with open(RESULT_FILE, 'w') as outfile:
    outfile.write(rendered)

  subprocess.call(['/opt/local/bin/pdflatex', RESULT_FILE],
      env={'TEXINPUTS': './envlab:'})
  os.unlink(RESULT_FILE)
