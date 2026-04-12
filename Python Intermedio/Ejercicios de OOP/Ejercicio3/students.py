class Student:
    def __init__(self,p_name,p_room,p_spanish,p_english, p_social_studies,p_science):
        self.name = p_name
        self.room = p_room
        self.g_spanish = p_spanish
        self.g_english = p_english
        self.g_social_studies = p_social_studies
        self.g_science = p_science
    def print_info(self):
        print(f"Nombre: {self.name}'\nSección: {self.room}"+
                f"\nNotas:\n\tEspañol: {self.g_spanish}"+
                f"\n\tInglés: {self.g_english}"+
                f"\n\tSociales: {self.g_social_studies}"+
                f"\n\tCiencias: {self.g_science}")