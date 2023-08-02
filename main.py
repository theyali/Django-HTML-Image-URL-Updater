import eel
from bs4 import BeautifulSoup
import os
import wx

eel.init("web")

@eel.expose
def pythonFunction(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

@eel.expose
def update_img_src(path, substring_to_remove, images_folder):
    print(path)
    with open(path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_src = img_tag.get('src')
        if img_src and img_src.startswith(substring_to_remove):
            new_img_src = "{% static '" + os.path.join(images_folder, os.path.basename(img_src)) + "' %}"
            img_tag['src'] = new_img_src

    updated_content = soup.prettify()

    with open(path, 'w') as file:
        file.write(updated_content)

@eel.expose
def update_css_src(path, substring_to_remove, images_folder):
    print(path)
    with open(path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_src = img_tag.get('src')
        if img_src and img_src.startswith(substring_to_remove):
            new_img_src = "{% static '" + os.path.join(images_folder, os.path.basename(img_src)) + "' %}"
            img_tag['src'] = new_img_src

    updated_content = soup.prettify()

    with open(path, 'w') as file:
        file.write(updated_content)

eel.start("templates/main.html", size=(400, 400))
