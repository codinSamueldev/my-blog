from django.db import models

# Create your models here.
class PostModel(models.Model):
    TOPIC_CHOICES = (
        ("spirituality", "Spirituality"),
        ("personal", "Personal"),
    )

    title = models.CharField(max_length=75, verbose_name="Title")
    content = models.TextField(max_length=3500, verbose_name="Main content")
    topic = models.CharField(max_length=75, choices=TOPIC_CHOICES, verbose_name="Topic")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    picture = models.ImageField(upload_to="images/", blank=True, null=True)
    pic_source = models.CharField(max_length=175, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]

