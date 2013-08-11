from .models import Category

def menu(request):
	c = Category.objects.all().filter(active__exact=1).order_by('name')
	return {'category_list': c}