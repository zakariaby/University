from django.db import models

# Create your models here.

PAYMENT_STATUS = [
    ("full_year_payment", "Paiement annuel"),
    ("half_year_payment", "Paiement semestriel")
]

class Enrollment(models.Model):
    student = models.ForeignKey(to="accounts.Student", on_delete=models.DO_NOTHING, blank=False)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS, default="half_year_payment")
    active = models.BooleanField(default=True)
    amount = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Enrollment: {} {}".format(self.student.first_name, self.student.last_name)