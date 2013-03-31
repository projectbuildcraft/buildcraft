all:
	
clean:
	rm *.pyc
run:
	./buildcraft.py
babies:
	fortune | cowsay
pull:
	git pull origin master
gui:
	./buildcraft
release:
	cd linux; python freeze.py ../gui.py ; make
