class TaskMaster:
    def __init__(self):
        self.missions = []
    
    def ajouter_mission(self, description):
        dic = {
            "description": description,
            "terminee": False
        }
        self.missions.append(dic)
       
    
    def marquer_terminee(self, numero_mission):
       # accéder à la mission par son index
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

    def supprimer_mission(self, numero_mission):
        if 1<=numero_mission<=len(self.missions):
            mission_supprimee=self.missions.pop(numero_mission - 1)
            print(f"🗑️ Mission '{mission_supprimee['description']}' supprimée !")
        else:
            print(f"❌ Mission {numero_mission} n'existe pas!")













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

    print("\n--- Test suppression mission ---")
    print("Avant suppression :")
    tm.afficher_missions()
    
    tm.supprimer_mission(1)  # Supprimer "Apprendre Python"
    print("\nAprès suppression :")
    tm.afficher_missions()
    
    print("\n--- Test suppression mission inexistante ---")
    tm.supprimer_mission(10)  # Doit afficher erreur


