#our code here
import Image from PIL
class ImgFile:
	"""Image file class"""
	def __init__(self,path)
		self.path=path
		self.name=retrieve_name(path)
		
	def get_name(self):
		return self.name
	
	def get_path(self):
		return self.path
	
	def retrieve_name(path):
		ls=list(path)
		index=0
		for char in ls:
			if ls[index]=='.':
				fin=index
				index-=1
				while ls[index]!='/':
					index-=1
				else:
					return path[index+1:fin]
					
			index+=1		
		print "Bad source path input"
		return 0 	#to trigger a second loop in main?

def main():
	print 'hello'

if __name__ == '__main__':
	main()
