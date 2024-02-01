compile:
	pyinstaller --onefile --icon=icon.ico main.py

compile_run:
	pyinstaller --onefile --icon=icon.ico main.py
	./dist/main

clean:
	rm -rf build dist main.spec __pycache__

run:
	python main.py