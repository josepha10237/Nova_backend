from locust import HttpUser, task, between

class NovaUser(HttpUser):
    # Temps d'attente entre chaque action d'un utilisateur (entre 1 et 3 secondes)
    wait_time = between(1, 3)

    @task(3)
    def view_epreuves(self):
        # Simule un étudiant qui récupère la liste des épreuves
        self.client.get("/api/epreuves/")  # Ajuste l'URL selon ton endpoint DRF

    @task(1)
    def home_page(self):
        # Simule un utilisateur qui arrive sur l'accueil
        self.client.get("/")