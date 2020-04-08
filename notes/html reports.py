#######################################################################################################################
#                           HERE HOW TO SET UP HTML REPORTS
#######################################################################################################################

'''
1. Install html-testRunner plugin (pip install html-testRunner)
2. Create new package for reports "Reports"
3. Edit constructor at the end of you testCase as bellow, where output is equal Reports Package path

if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output ='C:/Users/Admin/PycharmProjects/HRM100Full_Git/Reports'))

4. Run tests in terminal using command: python name_test.py

'''

