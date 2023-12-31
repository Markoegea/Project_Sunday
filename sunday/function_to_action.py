import os

#Your Functions goes here and in the functions.json file

def eval_function(function:str):
    eval(function)


def print_screen(value):
    print(value)

def create_html_folder(folder_name:str):
    path = "./"+ folder_name
    folderImg = path + "/Img"
    folderStyle = path + "/CSS"
    folderJS = path + "/JS"
    todas = [path, folderImg, folderStyle, folderJS]

    for i in todas:
        os.mkdir(i)

    archivoHTML = open(path+"/main.html", "at")
    archivoHTML.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="CSS/style.css">
    </head>
    <body>

        <script src="JS/ScriptMain.js"></script>
    </body>
    </html>''')
    archivoHTML.close()

    archivoCSS = open(folderStyle+"/style.css", "at")
    archivoCSS.close()

    archivoJS = open(folderJS+"/ScriptMain.js", "at")
    archivoJS.close()

if __name__ == '__main__':
    eval_function('print_screen("I love you")')