---
title: "Web Scrapping"
categories:
  - Projects
tags:
  - Web Scrapping
  - Python
  - JQuery
  - HTML
permalink: /webscrapping/
customjs :
  - https://code.jquery.com/jquery-3.3.1.js
---

```javascript
$(document).ready(function(){
        $.getJSON('headline.json',function(data){
            var headline_data = '';
            headline_data += "<table border='1'><tr><td>No</td><td>Judul</td><td>Kategori</td><td>Waktu Publish</td><td>Waktu Scrapping</td></tr>"
            $.each(data, function(key, value) {
                headline_data += '<tr>';
                headline_data += '<td>'+(key+1)+'</td>'
                headline_data += '<td>'+value.title+'</td>'
				        headline_data += '<td>'+value.category+'</td>'
                headline_data += '<td>'+value.get_time+'</td>'
				        headline_data += '<td>'+value.date+'</td>'
                headline_data += '</tr>'; 
            });
            $('#headline').append(headline_data);
        });
    });
```
<body>
    <h1>Head Line Republika Online, Update</h1>
    <div id="headline"></div>
</body>
</html>