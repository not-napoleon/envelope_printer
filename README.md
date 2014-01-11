envelope_printer
================

LaTeX and associated helper files to print my holiday card envelopes 

These are the texlive packages I had installed to get this running: 
(Via macports)

  lcdf-typetools @2.99_0+texlive (active)
  texlive-basic @30847_0+doc (active)
  texlive-bin @2013_4+x11
  texlive-bin @2013_5+x11 (active)
  texlive-bin-extra @30842_0+doc (active)
  texlive-common @2013_0 (active)
  texlive-fonts-recommended @30307_1+doc (active)
  texlive-fontutils @30842_0+doc (active)
  texlive-latex @30738_0+doc (active)
  texlive-latex-extra @30788_0+doc (active)
  texlive-latex-recommended @30811_0+doc (active)
  texlive-pictures @30637_0+doc (active)

You probably don't need all of those.


To get the main address printing in the caligraphy font, I tweaked 
the envlab macro to use \normalfont on line 749 of envlab/envlab.dtx
(instead of \ssfamily\selectfont).  There's probably a better way to
do that.
