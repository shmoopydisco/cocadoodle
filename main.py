#our code here
from PIL import Image
from ntpath import basename
import os

class ImgFile(object):
	"""Image file class"""
	def __init__(self,path):
		self.path=path
		self.name=self.retrieve_name()
	
	def get_format(self):
		path=self.get_path()
		index=0
		for char in path:
			if char=='.':
				return path[index+1:]
			index+=1
	
	def valid_format(self):
		frmt=self.get_format()
		
	
	def get_name(self):
		return self.name
	
	def get_path(self):
		return self.path
	
	def retrieve_name(self):
		name=basename(self.path)
		index=0
		for char in name:
			if char=='.':
				return name[:index]
			index+=1
	
	def convert(self,trgt_format,trgt_path):
		try:
			im=Image.open(self.get_path())
			im.save("{}{}.{}".format(trgt_path, self.get_name(),trgt_format))
			print "done"
		except Exception, e:
			print e

def main():
	
	#testbed
	"""
	p="C://Users//Daniel//Desktop//shit//bodies.mp3"
	img=ImgFile(p)
	frmt="png"
	pth="C://Users//Daniel//Desktop//"
	img.convert(frmt, pth)
	"""
	
	
if __name__ == '__main__':
	main()