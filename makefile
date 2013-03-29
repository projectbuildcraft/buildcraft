all:
	
clean:
	rm *.pyc
run:
	./buildcraft.py
babies:
	fortune | cowsay
pull:
	git pull origin master
