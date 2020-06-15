# Parsing the South Carolina Social Studies Standards

A quick hack to extract the standards from the South Carolina Social Studies Standards PDF and put them into a structured CSV file.

The make command shows how the script is used.  Requires pdftotext, which, for example, is in the poppler-utils package on RedHat/CentOS/Fedora, or poppler on MacPorts.

This isn't perfect. There are some things (table column headers) that are interspersed in the text, and I don't see anyway to disentangle them (there isn't enough info in the PDF).

Note the CSV is in UTF-8 encoding, so if you import it into Excel, make sure the encoding is correct.

