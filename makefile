run: create.py
		    python create.py

convert: run
		convert image.ppm image.png

clean:
	  rm image.ppm image.png
