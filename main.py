#our code here
#import Image from PIL
import ntpath
class ImgFile(object):
	"""Image file class"""
	def __init__(self,path):
		self.path=path
		self.name=self.retrieve_name()
		
	def get_name(self):
		return self.name
	
	def get_path(self):
		return self.path
	
	def retrieve_name(self):
		name=ntpath.basename(self.path)
		index=0
		for char in name:
			if char=='.':
				return name[:index]
			index+=1
def main():
	p="C:\bool\bool\pee.txt"
	img=ImgFile(p)
	print img.get_name()
	
if __name__ == '__main__':
	main()