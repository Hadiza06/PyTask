class TaskMaster:
    def __init__(self):
        self.missions = []
    
    def ajouter_mission(self, description):
        dic = {
            "description": description,
            "terminee": False
        }
        self.missions.append(dic)
        # Tu peux enlever le 'pass' ici
    
    def marquer_terminee(self, numero_mission):
        # Correction : accéder à la mission par son index
        if 1 <= numero_mission <= len(self.missions):
            self.missions[numero_mission - 1]["terminee"] = True
        else:
            print(f"❌ Mission {numero_mission} n'existe pas!")
    
    def afficher_missions(self):
        if not self.missions:
            print("Aucune mission pour le moment ! ")
        else:
            for i, mission in enumerate(self.missions, start=1):
                statut = "✅" if mission["terminee"] else "⏳"
                print(f"Tâche à accomplir : {i}. {mission['description']} [{statut}]")

if __name__ == "__main__":
    tm = TaskMaster()
    
    print("--- Test liste vide ---")
    tm.afficher_missions()
    
    print("\n--- Test avec missions ---")
    tm.ajouter_mission("Apprendre Python")
    tm.ajouter_mission("Faire du sport")
    tm.afficher_missions()
    
    print("\n--- Test marquer comme terminée ---")
    tm.marquer_terminee(1)  # Marquer la première mission
    tm.afficher_missions()