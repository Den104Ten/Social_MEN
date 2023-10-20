"""from django.template.defaultfilters import slugify

title_page = input()
print(slugify(title_page))

# здесь продолжайте программу"""


"""from django.template.defaultfilters import cut

title_page = input()
print(cut(title_page, ':'))"""



from django.template.defaultfilters import first, last

menu = list(map(str.strip, input().split(";")))
print(first(menu), last(menu))





