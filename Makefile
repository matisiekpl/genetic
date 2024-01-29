pdf:
	python3 report.py
	wkhtmltopdf --enable-local-file-access report.html report.pdf