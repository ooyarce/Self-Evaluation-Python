from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def Test1():
	nlist = []
	for i in range(0,21,2):
		if i == 0:
			continue
		odd = i+1
		nlist.append(i+odd)

	return nlist

def Test2(string):
	#Give format to string and sort it into a list
	txt = string.lower()
	list1 = txt.replace('\n',' ').replace(',',' ').replace('.',' ').split(' ')
	for i in range(list1.count('')):
		list1.remove('')
	list1.sort()

	#Count elements and return list
	twice_words = []
	i = 0
	while i < len(list1)-1:
		if list1.count(list1[i]) == 2:
			twice_words.append(list1[i])
			i+=1
		i+=1

	return twice_words

def Test3():
	#Using Chrome to access web
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('http://it.wikipedia.org/wiki/Birra')

	id_box = driver.find_element('name','search')
	id_box.send_keys('Petrolio')

	login_button = driver.find_element('name','go')
	login_button.click()
	
	time.sleep(10)
	print ("Minimal minimum number of clicks = 1")

text = '''Lorem ipsum dolor sit
amet, consectetur adipiscing elit. Nulla vehicula purus vitae sem lacinia, et
condimentum ipsum vestibulum. Nullam ullamcorper nulla vel ligula feugiat
accumsan. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit
amet faucibus dui.'''

print(Test1())
print(Test2(text))
print(Test3())
