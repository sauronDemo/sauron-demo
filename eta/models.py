from django.models import ExtendedModel

class Eta(ExtendedModel):
	foo = CompressedSignatureField()
	bar = models.DateTimeField(auto_now_add=True)

	
	class Meta:
		db_table = 'abc'
