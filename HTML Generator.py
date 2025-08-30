import os
cfg = '.cfg'
html = 'main.html'
h1 = 'head1.html'
h2 = 'head2.html'
h3 = 'head3.html'

dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(dir, html)
h1_path = os.path.join(dir, h1)
h2_path = os.path.join(dir, h2)
h3_path = os.path.join(dir, h3)
cfg_path = os.path.join(dir, cfg)

def html():
        with open(html_path, 'w') as file: # HTML
                file.write('<!DOCTYPE html>\n<html lang="en">\n')

html()

def title():
        file.write('<title>\n')
        file.write(pagetitle)
        file.write('</title>\n')

def head1():
        headn1 = str(input('Now type Head 1, to skip type "iwanttoskip". To finish type "iwanttofinish"\n'))
        if headn1 == 'iwanttoskip':
                print()
        if headn1 == 'iwanttofinish':
                finish()
        else:
                with open(h1_path, 'w') as file: # HTML
                        file.write('<h1>')
                        file.write(headn1)
                        file.write('</h1>\n')

def head2():
        headn2 = str(input('Type Head 2 or use previous instructions\n'))
        if headn2 == 'iwanttoskip':
                head3()
        if headn2 == 'iwanttofinish':
                finish()
        else:
                with open(h2_path, 'w') as file:
                        file.write('<h2>\n')
                        file.write(headn2)
                        file.write('</h2>\n')

def head3():
        headn3 = str(input('Head 3 or skip\n'))
        if headn3 == 'iwanttofinish':
                finish()
        else:
                with open(h3_path, 'w') as file:
                        file.write('<h3>\n')
                        file.write(headn3)
                        file.write('</h3>\n')

def finish():
        print('Your file is ready! And located in script folder')

with open(cfg_path, 'w') as file: # CONFIG
        file.write('File Created: \nFile Edited (times): \nHead1 Created: \nHead2 Created: \nHead3 Created: ')

mode = str(input('Welcome to HTML Generator. Choose your mode to start:\nNew - n\nEdit - e\n'))
if mode == 'n':
        pagetitle = str(input('Type your page title\n'))
        title()
        head1()
        head2()
        head3()
        with open(h1_path, 'r') as file:
                file.read(100)
                
        print('Updating config...')