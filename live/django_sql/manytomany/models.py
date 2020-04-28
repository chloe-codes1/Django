from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)

    # [ M:N field 정의 ]
    #: reservation을 통해서 Doctor와 연결하겠다
    doctors = models.ManyToManyField(Doctor, 
                                    # through='reservation',
                                    related_name='patients', #역참조 option 설정
                                    )

# [중계 모델 만들기]
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    # doctor, patient로 저장해도 doctor_id, patient_id로 각각의 id로 호출해서 사용 가능


