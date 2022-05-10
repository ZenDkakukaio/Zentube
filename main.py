from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivy.config import Config
from layout import MyLayout

Config.set("kivy", "window_icon", "")

import json as js

with open("media/media.json") as f:
    data = js.load(f)

Window.size = (350, 650)
title_window = "ZENTUBE VERSION 1.0"

class MyApp(MDApp):
    def build(self):
        self.load_file_kv()
        self.icon = data["logo"]["media1"]
        self.title = title_window
        self.theme_cls.theme_style = "Light"
        return MyLayout()



    def load_file_kv(self):
        Builder.load_file("layout.kv")



if __name__ == "__main__":
    obj = MyApp()
    obj.run()