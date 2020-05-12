from django.test import TestCase

# Create your tests here.
# def foliumMap():
#     m = folium.Map()
#     iframe = m._repr_html_()
#     return iframe
#
# #display(HTML(iframe))

#
# { %
# for map in iframe %}
# < main
# role = "main"
#
#
# class ="container" >
#
# < div
#
#
# class ="jumbotron" >
#
# < h1 > 제목: {{map.title}} < / h1 >
# < br >
# < h4 > 작성일: {{map.pub_date}} < / h4 >
# < br >
# < h4 > 작성자: {{map.author}} < / h4 >
# < br >
# < p
#
#
# class ="lead" > {{map.body | safe}} < / p >
#
# < br >
# < a
#
#
# class ="btn btn-lg btn-primary"
#
#
# href = "{{ site.baseurl }}/docs/{{ site.docs_version }}/components/navbar/"
# role = "button" > View
# navbar
# docs & raquo; < / a >
# < / div >
# < / main >
# { % endfor %}
# < / div >
#
# < script >
# function
# insertHTML()
# {
#     var
# strHTML = {{iframe}};
# containerA.innerHTML = strHTML;
# }
# < / script >
# < input
# type = "button"
# value = "innerHTML"
# onclick = "insertHTML()" >
# < div
#
#
# class ="panel-body" id="containerA" > < / div >
