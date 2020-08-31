from selenium import webdriver
import unittest

class Test(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\Phoebe\Documents\Uni Work\Bridging Coursework\geckodriver.exe')
        self.browser.get('http://127.0.0.1:8000')
    def tearDown(self):  
        self.browser.quit()

    def testTitle(self):
        assert "Phoebe's Blog" in self.browser.title

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  