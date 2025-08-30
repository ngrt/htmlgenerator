import os
html = 'main.html'

dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(dir, html)


def file_create():
        headn1 = str(input('Now type Head 1, to skip type "iwanttoskip". To finish type "iwanttofinish"\n'))
        if headn1 == 'iwanttoskip':
                with open(html_path, 'w') as file:
                        file.write('<!DOCTYPE html>\n<html lang="en">\n')
                        file.write('<title>\n')
                        file.write(pagetitle)
                        file.write('</title>\n')
                        headn2 = str(input('Type Head 2 or use previous instructions\n'))
                        if headn2 == 'iwanttoskip':
                                headn3 = str(input('Head 3 or type "iwanttofinish"\n'))
                                if headn3 == 'iwanttofinish':
                                        finish()
                                else:
                                        file.write('<h3>\n')
                                        file.write(headn3)
                                        file.write('</h3>\n')
                                        finish()
                        if headn2 == 'iwanttofinish':
                                finish()
                        else:
                                file.write('<h2>\n')
                                file.write(headn2)
                                file.write('</h2>\n')
                                headn3 = str(input('Head 3 or type "iwanttofinish"\n'))
                                if headn3 == 'iwanttofinish':
                                        finish()
                                else:
                                        file.write('<h3>\n')
                                        file.write(headn3)
                                        file.write('</h3>\n')
                                        finish()
        if headn1 == 'iwanttofinish':
                finish()
        else:
                with open(html_path, 'w') as file:
                        file.write('<!DOCTYPE html>\n<html lang="en">\n')
                        file.write('<title>\n')
                        file.write(pagetitle)
                        file.write('</title>\n')
                        file.write('<h1>')
                        file.write(headn1)
                        file.write('</h1>\n')
                        headn2 = str(input('Type Head 2 or use previous instructions\n'))
                        if headn2 == 'iwanttoskip':
                                headn3 = str(input('Head 3 or type "iwanttofinish"\n'))
                                if headn3 == 'iwanttofinish':
                                        finish()
                                else:
                                        file.write('<h3>\n')
                                        file.write(headn3)
                                        file.write('</h3>\n')
                                        finish()
                        if headn2 == 'iwanttofinish':
                                finish()
                        else:
                                file.write('<h2>\n')
                                file.write(headn2)
                                file.write('</h2>\n')
                                headn3 = str(input('Head 3 or type "iwanttofinish"\n'))
                                if headn3 == 'iwanttofinish':
                                        finish()
                                else:
                                        file.write('<h3>\n')
                                        file.write(headn3)
                                        file.write('</h3>\n')
                                        finish()

def finish():
        print('Your file is ready! And located in script folder')

a = print('Welcome to HTML Generator.\n')
pagetitle = str(input('Type your page title\n'))
file_create()
