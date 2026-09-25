from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty

# Couleur de fond globale
Window.clearcolor = (0.05, 0.08, 0.16, 1)

class MenuScreen(Screen):
    pass

class RdmScreen(Screen):
    result_text = StringProperty("Résultat : --")

    def calculer_rdm(self):
        try:
            val_str = self.ids.input_rdm.text
            if val_str:
                val = float(val_str)
                # Exemple de calcul RDM
                res = val * 1.5
                self.result_text = f"Résultat RDM : {res:.2f} kN"
            else:
                self.result_text = "Veuillez entrer une valeur."
        except ValueError:
            self.result_text = "Erreur : Nombre invalide."

class BtpProApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(RdmScreen(name='rdm_screen'))
        return sm

if __name__ == '__main__':
    BtpProApp().run()
