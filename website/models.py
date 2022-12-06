from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, verbose_name='Nom')
    last_name = models.CharField(max_length=30, blank=False, verbose_name='Prénom')
    birth_date = models.DateField(blank=False, verbose_name='Date de Naissance')
    mail = models.EmailField(max_length=200, blank=False, verbose_name='Email')
    phone_regex = RegexValidator(regex=r'(0|\+33|0033)[1-9][0-9]{8}', message='*numéro incorrecte !')
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=False, verbose_name='Téléphone Portable')
    city = models.CharField(max_length=30, blank=False, verbose_name='Ville')
    zip_code = models.CharField(max_length=10, blank=False, verbose_name='Code Postal')
    register_date = models.DateTimeField(auto_now_add=True)
    code_validation = models.CharField(max_length=6, blank=False, verbose_name='Code Validation')


class CreditCard(models.Model):
    id = models.AutoField(primary_key=True)
    card_type = models.CharField(max_length=30, blank=False, verbose_name='Type de Carte')
    card_number = models.CharField(max_length=19, blank=False, verbose_name='Numéro de carte')
    expiration_month = models.CharField(max_length=2, blank=False, verbose_name='Mois Expiration')
    expiration_year = models.CharField(max_length=2, blank=False, verbose_name='Année Expiration')
    cvv = models.CharField(max_length=3, blank=False, verbose_name='Code CVV')
    amount_reservation = models.CharField(max_length=30, blank=False, verbose_name='Montant de la réservation')
    card_owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)