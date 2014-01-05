"""
Python script for building LaTeX envlab formatted envelope list
"""
import subprocess
import os

# TODO: pull these from command line args
TEMPLATE_FILE='envelopes_template.tex'
DATA_FILE='addresses.dat'
RESULT_FILE = 'envelopes.tex'

ADDRESS_LINE="\mlabel{%%\n%(from_address)s}{%%\n%(to_address)s}"

def build_addresses(address_file):
  """Build the formatted address list from the given file-like object
  """
  format_vars = {
      'from_address':
          r'Mark and Karen Tozzi\\1404 Duckwall Road\\Berkeley Springs, WV 25411',
  }

  addresses = []
  with open(address_file) as infile:
    for to_address in infile:
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
  rendered = render_template(TEMPLATE_FILE, build_addresses(DATA_FILE))
  with open(RESULT_FILE, 'w') as outfile:
    outfile.write(rendered)

  subprocess.call(['/opt/local/bin/pdflatex', RESULT_FILE],
      env={'TEXINPUTS': './envlab:'})
  os.unlink(RESULT_FILE)

