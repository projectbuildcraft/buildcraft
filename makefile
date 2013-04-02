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
	mv linux/gui linux/buildcraft
	cp -R images linux/images
	cp linux/buildcraft linux/debian/usr/games/buildcraft
	cd linux ; fakeroot dpkg-deb --build debian; mv debian.deb buildcraft_0.5.1-0_all.deb
