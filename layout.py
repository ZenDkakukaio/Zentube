from kivy.uix.screenmanager import ScreenManager, FallOutTransition
from kivymd.toast import toast
from kivymd.uix.menu import  MDDropdownMenu
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.snackbar import Snackbar
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.core.window import Window

import webbrowser
from pytube import YouTube
from data_link import MyDataLink

obj = MDApp()
obj_data_link = MyDataLink()

import json as js

with open("media.json") as f:
    data = js.load(f)

SAVE_PATH = "dowloaded"




class MyLayout(ScreenManager):
    data_fond = data["fond"]["media2"]
    data_logo = data["logo"]["media1"]
    data_fond1 = data["fond1"]["media3"]
    data_analyse = data["analyse"]["media4"]
    data_dowload = data["dowload"]["media5"]
    data1 = {
        'Accueil': 'youtube'
    }

    data_about = {
        "code source": "github",
        "infos": "information",
    }
    state_url = StringProperty()

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.a = ["theme", "A propos", "Quitter"]
        self.dialog = None



    def recovery_link(self, url):
        anim_float_state_url = Animation(opacity = 1, duration = .1, size=(Window.width, dp(0)))
        anim_float_state_url += Animation(opacity=1, duration= .9, size=(Window.width, dp(30)))
        anim_float_state_url += Animation(opacity=1, duration= 3, size=(Window.width, dp(0)))
        anim_float_state_url.start(self.ids.id_float_state_url)
        anim_label_state_url = Animation(opacity = 1, duration = .9)
        anim_label_state_url += Animation(opacity=0, duration=3)
        anim_label_state_url.start(self.ids.id_label_state_url)









    def dowload_media(self, url):
        try:
            self.ids.id_spinner2.active = True
            yt = YouTube(url)
            ys = yt.streams.get_highest_resolution()
            ys.download(SAVE_PATH)
            toast("téléchargement terminé...")
            self.ids.id_spinner2.active = False
            obj_data_link.insert_database(url)
        except Exception as E:
            state_url = f"Erreur de type --> {E}"
            self.ids.id_label_error.text = state_url
            anim_float_error_url = Animation(opacity=1, duration= .1, size=(Window.width, dp(0)))
            anim_float_error_url += Animation(opacity=1, duration= 10, size=(Window.width, dp(100)))
            anim_float_error_url += Animation(opacity=0, duration= 5, size=(Window.width, dp(0)))
            anim_float_error_url.start(self.ids.id_float_error)
            anim_label_state_url = Animation(opacity=1, duration=10)
            anim_label_state_url += Animation(opacity=0, duration=5)
            anim_label_state_url.start(self.ids.id_label_error)


    def callback(self, x):
        self.transition = FallOutTransition(duration=.5)
        self.current = self.ids.sc2.name
        toast("Bienvenue sur Zentube...")


    def check_option(self):
        i = 0
        options = "Acces aux options"

        menu_items = [
            {
                "text": f"{self.a[i]}",
                "viewclass": "OneLineListItem",
                "height": 60,
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in range(len(self.a))
        ]
        self.menu = MDDropdownMenu(
            caller = self.ids.id_menu_icon,
            items = menu_items,
            width_mult = 4
        )
        self.menu.open()
        return toast(options)



    def menu_callback(self, text_item):

        if text_item == str(0):
            p = MDThemePicker()
            p.open()

        elif text_item == str(1):
            self.open_about_app()

        elif text_item == str(2):
            obj.stop()




    def open_about_app(self):
        b = MDGridBottomSheet()

        for item in self.data_about.items():
            b.add_item(
                item[0],
                lambda  x, y=item[0]: self.callback_for_menu_item(y),
                icon_src=item[1],
            )
        b.open()





    def callback_for_menu_item(self, item_about):
        t_info1 = """Démo application de téléchargement de videos sur youtube.




                Version: Beta\n
                contact: Daryl21emani07@gmail.com

                """
        t_infos2 = "              A propos"



        if item_about == "code source":
            self.get_url_github()


        elif item_about == "infos":
            if not self.dialog:
                self.dialog = MDDialog(
                    title=t_infos2,
                    text=t_info1,
                    buttons=[
                        MDIconButton(
                            icon="information",
                            theme_text_color="Custom",
                            text_color=(1, 0, 0, .8),
                            user_font_size="90sp",
                            pos_hint={"center_x": .5, "center_y": .5}
                        ),
                        MDFlatButton(
                            text="                ",

                        ),
                    ],
                )

            self.dialog.open()






    def get_url_github(self):
        path_1 = "https://github.com/ZenDkakukaio/Zentube/"
        webbrowser.open_new(path_1)





