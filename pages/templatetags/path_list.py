from django import template

register = template.Library()


@register.filter(name='path_list')
def return_path_list(value, index='None'):
	split_list = value.split('/')[1:]
	return split_list if type(index) != int else split_list[index]