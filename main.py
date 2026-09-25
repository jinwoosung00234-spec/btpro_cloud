from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# --- 1. ÉCRAN PRINCIPAL (MENU) ---
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=15)
        
        # En-tête
        title = Label(
            text="BTP PRO KINSHASA", 
            font_size='22sp', 
            bold=True, 
            size_hint_y=None, 
            height=50
        )
        subtitle = Label(
            text="Sélectionnez un module de calcul :", 
            font_size='15sp', 
            size_hint_y=None, 
            height=30
        )
        
        main_layout.add_widget(title)
        main_layout.add_widget(subtitle)
        
        # Menu défilant pour éviter les chevauchements
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=12, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        modules = [
            ("[1] Module Dosage Béton & Mortier", "beton"),
            ("[2] Module Ferraillage & Armatures", "ferraillage"),
            ("[3] Module Calcul Escalier (Blondel)", "escalier"),
            ("[4] Résistance des Matériaux (RDM)", "rdm"),
            ("[5] Module Maçonnerie & Blocs", "maconnerie"),
            ("[6] Module Revêtement & Carrelage", "carrelage")
        ]
        
        for text, screen_name in modules:
            btn = Button(
                text=text, 
                size_hint_y=None, 
                height=55, 
                font_size='15sp',
                background_color=(0.15, 0.45, 0.85, 1)
            )
            btn.bind(on_release=lambda instance, sc=screen_name: setattr(self.manager, 'current', sc))
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        main_layout.add_widget(scroll)
        self.add_widget(main_layout)


# --- 2. MODULE DOSAGE BÉTON ---
class BetonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=10)
        
        layout.add_widget(Label(text="Module Dosage Béton", font_size='20sp', bold=True, size_hint_y=None, height=40))
        
        self.input_vol = TextInput(
            hint_text="Volume de béton (m³)", 
            input_filter='float', 
            multiline=False, 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.input_vol)
        
        self.input_dosage = TextInput(
            hint_text="Dosage Ciment (ex: 350 kg/m³)", 
            input_filter='float', 
            multiline=False, 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.input_dosage)
        
        btn_calc = Button(
            text="Calculer les Matériaux", 
            size_hint_y=None, 
            height=50, 
            background_color=(0, 0.6, 0.3, 1)
        )
        btn_calc.bind(on_release=self.calculer)
        layout.add_widget(btn_calc)
        
        self.lbl_result = Label(
            text="", 
            font_size='15sp', 
            halign='left', 
            valign='top'
        )
        self.lbl_result.bind(size=self.lbl_result.setter('text_size'))
        layout.add_widget(self.lbl_result)
        
        btn_back = Button(text="Retour au menu", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def calculer(self, instance):
        try:
            vol = float(self.input_vol.text) if self.input_vol.text else 0.0
            dosage = float(self.input_dosage.text) if self.input_dosage.text else 350.0
            
            sac_ciment = (vol * dosage) / 50
            sable_m3 = vol * 0.4
            gravier_m3 = vol * 0.8
            eau_litres = vol * 175
            
            self.lbl_result.text = (
                f"Résultats pour {vol} m³ (Dosage {dosage} kg/m³) :\n\n"
                f"• Ciment (50kg) : {sac_ciment:.1f} sacs ({vol * dosage:.0f} kg)\n"
                f"• Sable : {sable_m3:.2f} m³\n"
                f"• Gravier : {gravier_m3:.2f} m³\n"
                f"• Eau : {eau_litres:.1f} Litres"
            )
        except ValueError:
            self.lbl_result.text = "Veuillez entrer des chiffres valides."


# --- 3. MODULE FERRAILLAGE ---
class FerraillageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=10)
        layout.add_widget(Label(text="Module Ferraillage & Armatures", font_size='20sp', bold=True, size_hint_y=None, height=40))
        layout.add_widget(Label(text="Calcul du nombre et poids des barres HA", font_size='15sp'))
        
        btn_back = Button(text="Retour au menu", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)


# --- 4. MODULE ESCALIER ---
class EscalierScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=10)
        layout.add_widget(Label(text="Module Escalier (Blondel)", font_size='20sp', bold=True, size_hint_y=None, height=40))
        layout.add_widget(Label(text="Calcul de la gironde et hauteur des marches", font_size='15sp'))
        
        btn_back = Button(text="Retour au menu", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)


# --- 5. MODULE RDM ---
class RDMScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=10)
        layout.add_widget(Label(text="Module Résistance des Matériaux", font_size='20sp', bold=True, size_hint_y=None, height=40))
        
        self.input_f = TextInput(hint_text="Force appliquée (kN)", input_filter='float', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.input_f)
        
        btn_calc = Button(text="Calculer", size_hint_y=None, height=50, background_color=(0, 0.6, 0.3, 1))
        btn_calc.bind(on_release=self.calculer)
        layout.add_widget(btn_calc)
        
        self.lbl_result = Label(text="", font_size='15sp')
        layout.add_widget(self.lbl_result)
        
        btn_back = Button(text="Retour au menu", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def calculer(self, instance):
        try:
            f = float(self.input_f.text)
            self.lbl_result.text = f"Résultat RDM : {f:.2f} kN"
        except ValueError:
            self.lbl_result.text = "Entrée invalide."


# --- 6. MODULE MAÇONNERIE ---
class MaconnerieScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=10)
        layout.add_widget(Label(text="Module Maçonnerie & Blocs", font_size='20sp', bold=True, size_hint_y=None, height=40))
        layout.add_widget(Label(text="Calcul des blocs de ciment et mortier de pose", font_size='15sp'))
        
        btn_back = Button(text="Retour au menu", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)


# --- 7. MODULE CARRELAGE ---
class CarrelageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[20, 40, 20, 20], spacing=10)
        layout.add_widget(Label(text="Module Carrelage", font_size='20sp', bold=True, size_hint_y=None, height=40))
        layout.add_widget(Label(text="Calcul de la surface et nombre de carreaux", font_size='15sp'))
        
        btn_back = Button(text="Retour au menu", size_hint_y=None, height=50)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)
        self.add_widget(layout)


# --- APPLICATION PRINCIPALE ---
class BTPApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(BetonScreen(name='beton'))
        sm.add_widget(FerraillageScreen(name='ferraillage'))
        sm.add_widget(EscalierScreen(name='escalier'))
        sm.add_widget(RDMScreen(name='rdm'))
        sm.add_widget(MaconnerieScreen(name='maconnerie'))
        sm.add_widget(CarrelageScreen(name='carrelage'))
        return sm

if __name__ == '__main__':
    BTPApp().run()
        
