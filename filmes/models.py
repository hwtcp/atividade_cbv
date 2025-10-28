from django.db import models

class Filme(models.Model):
    GENEROS = [
        ('Ação', 'Ação'),
        ('Aventura', 'Aventura'),
        ('Comédia', 'Comédia'),
        ('Comédia Romântica', 'Comédia Romântica'),
        ('Drama', 'Drama'),
        ('Terror', 'Terror'),
        ('Romance', 'Romance'),
        ('Ficção Científica', 'Ficção Científica'),
        ('Animação', 'Animação'),
        ('Documentário', 'Documentário'),
        ('Suspense', 'Suspense'),
        ('Drama Policial', 'Drama Policial'),

    ]

    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30, choices=GENEROS)
    ano_lancamento = models.PositiveIntegerField()
    sinopse = models.TextField(blank=True, null=True)
    assistido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

