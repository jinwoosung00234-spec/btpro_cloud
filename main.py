
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(
            text='BTP PRO KINSHASA', 
            font_size=24, 
            bold=True, 
            color=(0.1, 0.4, 0.7, 1)
        ))
        
        btn_rdm = Button(text='[4] Résistance des Matériaux (RDM)', background_color=(0.2, 0.6, 0.8, 1))
        btn_rdm.bind(on_press=self.aller_vers_rdm)
        layout.add_widget(btn_rdm)
        
        btn_beton = Button(text='[1] Calcul de Béton & Matériaux', background_color=(0.2, 0.6, 0.8, 1))
        layout.add_widget(btn_beton)

        self.add_widget(layout)

    def aller_vers_rdm(self, instance):
        self.manager.current = 'rdm_screen'

class RdmScreen(Screen):
    def __init__(self, **kwargs):
        super(RdmScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text='Module RDM & Contrôle Normatif', font_size=20))
        
        btn_retour = Button(text='Retour au menu', background_color=(0.8, 0.2, 0.2, 1))
        btn_retour.bind(on_press=self.retour_menu)
        layout.add_widget(btn_retour)
        
        self.add_widget(layout)

    def retour_menu(self, instance):
        self.manager.current = 'menu_screen'

class BtpProApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical')
        
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(RdmScreen(name='rdm_screen'))
        
        root_layout.add_widget(sm)
        
        # Espace réservé pour la bannière publicitaire Google AdMob
        banner_layout = BoxLayout(size_hint_y=None, height=50, padding=5)
        banner_layout.add_widget(Label(
            text='[ Espace Bannière Google AdMob ]', 
            font_size=12,
            color=(0.5, 0.5, 0.5, 1)
        ))
        root_layout.add_widget(banner_layout)
        
        return root_layout

if __name__ == '__main__':
    BtpProApp().run()

