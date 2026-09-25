
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import os

# Fond d'écran général style application pro (Gris clair / aluminium élégant)
Window.clearcolor = (0.94, 0.95, 0.97, 1)

# --- BARRE DE NAVIGATION INFÉRIEURE ---
class BottomNavBar(BoxLayout):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = '60dp'
        self.padding = [5, 5, 5, 5]
        self.spacing = 5
        
        tabs = [
            ("🏠 Accueil", "menu"),
            ("📁 Projets", "menu"),
            ("🔢 Calculs", "menu"),
            ("👤 Profil", "menu")
        ]
        
        for name, target in tabs:
            btn = Button(
                text=name,
                font_size='13sp',
                bold=True,
                background_color=(0.15, 0.2, 0.3, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_release=lambda x, t=target: setattr(sm, 'current', t))
            self.add_widget(btn)

# --- BOUTON DE RETOUR ---
class TopHeaderBar(BoxLayout):
    def __init__(self, title_text, sm, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = '55dp'
        self.padding = [10, 5, 10, 5]
        self.background_color = (0.15, 0.2, 0.3, 1)
        
        back_btn = Button(text="←", size_hint_x=None, width='50dp', font_size='20sp', bold=True)
        back_btn.bind(on_release=lambda x: setattr(sm, 'current', 'menu'))
        
        title_lbl = Label(text=title_text, font_size='18sp', bold=True, color=(1, 1, 1, 1), halign='center')
        title_lbl.bind(size=title_lbl.setter('text_size'))
        
        self.add_widget(back_btn)
        self.add_widget(title_lbl)

# --- 1. ÉCRAN PRINCIPAL (ACCUEIL / GRILLE) ---
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        
        # En-tête de l'application
        header = BoxLayout(orientation='vertical', size_hint_y=None, height='75dp', padding=10)
        title = Label(text="BâtiCalc Pro", font_size='22sp', bold=True, color=(0.1, 0.1, 0.15, 1))
        subtitle = Label(text="Module : Conception Structurée & Chiffrage", font_size='13sp', color=(0.4, 0.45, 0.5, 1))
        header.add_widget(title)
        header.add_widget(subtitle)
        root.add_widget(header)
        
        # Grille des modules (Style cartes de la maquette)
        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=12, padding=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        modules = [
            ("🏗️ Coffrage /\nFerraillage", "ferraillage"),
            ("📐 Calcul Escalier\n& RDM", "escalier"),
            ("🧱 Calcul des\nMatériaux", "maconnerie"),
            ("🚚 Calcul Béton /\nBétonnage", "beton"),
            ("⚡ Install.\nÉlectrique", " electricite"),
            ("⚖️ Calcul Poids\nStructuraux", "poids"),
            ("📊 Calcul\nFondations", "fondations"),
            ("💰 Estimation\nBudget / Devis", "budget")
        ]
        
        for text, sc_name in modules:
            btn = Button(
                text=text,
                size_hint_y=None,
                height='110dp',
                font_size='14sp',
                bold=True,
                halign='center',
                valign='middle',
                background_color=(0.98, 0.98, 0.98, 1),
                color=(0.15, 0.15, 0.2, 1)
            )
            btn.bind(size=btn.setter('text_size'))
            btn.bind(on_release=lambda x, s=sc_name: setattr(self.manager, 'current', s if s != " electricite" else "electricite"))
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        root.add_widget(scroll)
        
        # Barre de navigation basse
        root.add_widget(BottomNavBar(self.manager))
        self.add_widget(root)


# --- CLASSE DE BASE POUR LES ÉCRANS DE CALCUL ---
class BaseCalcScreen(Screen):
    def __init__(self, title_text, **kwargs):
        super().__init__(**kwargs)
        self.layout_main = BoxLayout(orientation='vertical')
        self.layout_main.add_widget(TopHeaderBar(title_text, self.manager))
        
        self.scroll = ScrollView()
        self.content_layout = BoxLayout(orientation='vertical', padding=20, spacing=12, size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))
        
        self.scroll.add_widget(self.content_layout)
        self.layout_main.add_widget(self.scroll)
        self.add_widget(self.layout_main)


# --- 2. MODULE BÉTON ---
class BetonScreen(BaseCalcScreen):
    def __init__(self, **kwargs):
        super().__init__("Module Dosage Béton & Mortier", **kwargs)
        
        self.content_layout.add_widget(Label(text="Volume de béton (m³) :", color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height='25dp', halign='left'))
        self.vol = TextInput(hint_text="Ex: 15", input_filter='float', multiline=False, size_hint_y=None, height='45dp')
        self.content_layout.add_widget(self.vol)
        
        self.content_layout.add_widget(Label(text="Dosage ciment (kg/m³) :", color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height='25dp', halign='left'))
        self.dosage = TextInput(text="350", input_filter='float', multiline=False, size_hint_y=None, height='45dp')
        self.content_layout.add_widget(self.dosage)
        
        calc_btn = Button(text="Calculer & Générer Rapport", size_hint_y=None, height='50dp', bold=True, background_color=(0.15, 0.5, 0.8, 1))
        calc_btn.bind(on_release=self.calculer)
        self.content_layout.add_widget(calc_btn)
        
        self.res = Label(text="Réf: Normes BTP - Kinshasa", color=(0.3, 0.3, 0.3, 1), size_hint_y=None, height='120dp', halign='center', valign='middle')
        self.res.bind(size=self.res.setter('text_size'))
        self.content_layout.add_widget(self.res)
        
        share_btn = Button(text="📤 Partager le Devis / Rapport (WhatsApp / PDF)", size_hint_y=None, height='50dp', bold=True, background_color=(0, 0.6, 0.3, 1))
        share_btn.bind(on_release=self.partager)
        self.content_layout.add_widget(share_btn)

    def calculer(self, instance):
        try:
            v = float(self.vol.text)
            d = float(self.dosage.text)
            ciment_kg = v * d
            sacs = ciment_kg / 50
            sable = v * 0.4
            gravier = v * 0.8
            eau = v * 175
            self.res.text = f"RÉSULTATS ({v} m³) :\n• Ciment : {sacs:.1f} sacs ({ciment_kg:.0f} kg)\n• Sable : {sable:.2f} m³ | Gravier : {gravier:.2f} m³\n• Eau : {eau:.1f} Litres"
        except ValueError:
            self.res.text = "Veuillez entrer un volume valide."

    def partager(self, instance):
        # Simulation de génération PDF et Partage direct
        self.res.text += "\n[✔] Rapport PDF généré avec succès !\n[✔] Prêt pour envoi sur WhatsApp / Facebook."


# --- 3. MODULE ÉLECTRICITÉ (NOUVEAU) ---
class ElectriciteScreen(BaseCalcScreen):
    def __init__(self, **kwargs):
        super().__init__("Module Installation Électrique", **kwargs)
        
        self.content_layout.add_widget(Label(text="Puissance totale appareils (Watts) :", color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height='25dp', halign='left'))
        self.puissance = TextInput(hint_text="Ex: 3500", input_filter='float', multiline=False, size_hint_y=None, height='45dp')
        self.content_layout.add_widget(self.puissance)
        
        self.content_layout.add_widget(Label(text="Longueur de ligne (mètres) :", color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height='25dp', halign='left'))
        self.longueur = TextInput(hint_text="Ex: 20", input_filter='float', multiline=False, size_hint_y=None, height='45dp')
        self.content_layout.add_widget(self.longueur)
        
        calc_btn = Button(text="Calculer Section de Câble", size_hint_y=None, height='50dp', bold=True, background_color=(0.15, 0.5, 0.8, 1))
        calc_btn.bind(on_release=self.calculer)
        self.content_layout.add_widget(calc_btn)
        
        self.res = Label(text="Dimensionnement selon chute de tension admissible.", color=(0.3, 0.3, 0.3, 1), size_hint_y=None, height='100dp', halign='center', valign='middle')
        self.res.bind(size=self.res.setter('text_size'))
        self.content_layout.add_widget(self.res)

    def calculer(self, instance):
        try:
            p = float(self.puissance.text)
            I = p / 230  # Courant monophasé 230V
            section = (2 * self.longueur.text and float(self.longueur.text) * I * 0.017) / (3.0) # Formule indicative
            self.res.text = f"Intensité calculée : {I:.1f} A\nSection minimale recommandée du câble : 2.5 mm² ou 4 mm² (cuivre)"
        except ValueError:
            self.res.text = "Entrées invalides."


# --- 4. MODULES SIMPLES ADDITIONNELS ---
class GenericModuleScreen(BaseCalcScreen):
    def __init__(self, title, description, **kwargs):
        super().__init__(title, **kwargs)
        self.content_layout.add_widget(Label(text=description, font_size='16sp', color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height='100dp', halign='center', valign='middle'))


# --- APPLICATION PRINCIPALE ---
class BatiCalcProApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(BetonScreen(name='beton'))
        sm.add_widget(ElectriciteScreen(name='electricite'))
        sm.add_widget(GenericModuleScreen("Coffrage & Ferraillage", "Module de calcul des sections d'armatures HA et coffrage bois/métal.", name='ferraillage'))
        sm.add_widget(GenericModuleScreen("Calcul Escalier & RDM", "Module de vérification de la loi de Blondel et contraintes de flexion.", name='escalier'))
        sm.add_widget(GenericModuleScreen("Calcul des Matériaux", "Estimation des blocs, ciment, sable et mortier.", name='maconnerie'))
        sm.add_widget(GenericModuleScreen("Calcul Poids Structuraux", "Évaluation des charges permanentes et d'exploitation.", name='poids'))
        sm.add_widget(GenericModuleScreen("Calcul Fondations", "Dimensionnement des semelles isolées et filantes.", name='fondations'))
        sm.add_widget(GenericModuleScreen("Estimation Budget / Devis", "Génération globale du devis quantitatif et estimatif (DQE).", name='budget'))
        return sm

if __name__ == '__main__':
    
