top_template = open('./templates/top.html').read()
bottom_template = open('./templates/bottom.html').read()

content = open('./content/index.html').read()
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)


about_me = open('./content/about_me.html').read()
about_me_html = top_template + about_me + bottom_template
open('about_me.html', 'w+').write(about_me_html)

contact_me = open('./content/contact_me.html').read()
contact_me_html = top_template + contact_me + bottom_template
open('contact_me.html', 'w+').write(contact_me_html)

