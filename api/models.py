from django.db import models

class Epreuve(models.Model):
    titre = models.CharField(max_length=255, blank=True, null=True)
    filiere = models.CharField(max_length=150, default="Génie Informatique")
    matiere = models.CharField(max_length=150, default="Algorithmique")
    niveau = models.CharField(max_length=50, default="Niveau 1")
    annee = models.CharField(max_length=50, default="2025-2026")
    type = models.CharField(max_length=50, default="Examen")
    pdf_file = models.FileField(upload_to='epreuves_pdfs/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.niveau} - {self.filiere} - {self.matiere} ({self.annee})"