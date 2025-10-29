class TaskMaster:
    def __init__(self):
        self.missions = []
    
    def ajouter_mission(self, description):
        self.missions.append(description)
    
    def afficher_missions(self):
        if not self.missions:
            print("Aucune mission pour le moment !")
        else:
            for i, mission in enumerate(self.missions, start=1):
                print(f"Tâche à accomplir : {i}. {mission}")

if __name__ == "__main__":
    tm = TaskMaster()
    
    print("--- Test liste vide ---")
    tm.afficher_missions()  # ➡️ "Aucune mission pour le moment !"
    
    print("\n--- Test avec missions ---")
    tm.ajouter_mission("Apprendre Python")
    tm.ajouter_mission("Faire du sport")
    tm.afficher_missions()