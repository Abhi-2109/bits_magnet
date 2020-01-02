from django.db import models

# Create your models here.


class person(models.Model):
    name = models.CharField(max_length=256)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    desciption = models.TextField()
    is_member = models.BooleanField(default=False)
    facebook_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    codechef_url = models.URLField(null=True, blank= True)
    hackerrank_url = models.URLField(null=True, blank= True)
    hackerearth_url = models.URLField(null=True, blank= True)

    def __str__(self):
        return self.name

class awards(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    team = models.ManyToManyField(person)
    pic = models.ImageField(upload_to= 'picture', blank=True)

    def __str__(self):
        return self.title


class education(models.Model):
    per = models.ForeignKey(person, on_delete=models.CASCADE)
    college = models.CharField(max_length=256)
    startYear = models.CharField(max_length=4)
    endYear = models.CharField(max_length=10)
    marks = models.CharField(max_length=50)

    def __str__(self):
        return str(self.per) + str(self.college)

class certification(models.Model):
    per = models.ForeignKey(person,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class internship(models.Model):
    per = models.ForeignKey(person, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=245)
    startDate = models.DateField()
    endDate = models.DateField()
    company_name = models.CharField(max_length=256)
    company_url = models.URLField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.profile_name

class skill(models.Model):
    per = models.ForeignKey(person,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rate_out_of_5 = models.IntegerField()

    def __str__(self):
        return self.name









