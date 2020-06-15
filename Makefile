# Makefile


2020-SC-SS.csv : 2020-SC-SS.txt
	python3 reformat.py < 2020-SC-SS.txt > 2020-SC-SS.csv

2020-SC-SS.txt : 2020-SC-SS.pdf
	pdftotext -layout 2020-SC-SS.pdf

