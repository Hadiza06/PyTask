class TaskMaster:
    def __init__(self):
        self.missions = []
    
    def ajouter_mission(self, description):
        self.missions.append(description)

# ↓↓↓ CE CODE S'EXÉCUTE SEULEMENT SI TU LANCES CE FICHIER DIRECTEMENT ↓↓↓
if __name__ == "__main__":
    # Créer une instance de TaskMaster
    mon_gestionnaire = TaskMaster()
    
    # Tester la méthode ajouter_mission
    mon_gestionnaire.ajouter_mission("Apprendre Python")
    mon_gestionnaire.ajouter_mission("Faire les courses")
    
    # Vérifier que ça marche
    print("Missions ajoutées :", mon_gestionnaire.missions)