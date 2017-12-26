var $ = window.jQuery;


    function get_url() {
      document.body.style.cursor='wait';

      var url = document.getElementById('url').value;

      if (url == ''){
        alert('Fill all fields and press \'Submit\'');
        document.body.style.cursor='default';
      }
      else{
        var autorize = {'url': url};

        var data = new FormData();
        data.append("data", JSON.stringify(autorize));

           $.ajax({
           //18.217.243.109
              url: 'http://18.217.243.109:8000/',
              type: 'POST',
              data: data,
              cache: false,
              dataType: 'json',
              processData: false,
              contentType: false,
              success:function(data, status) {
                 document.body.style.cursor='default';
                 if(data.result == 'Andrew noob'){
                     alert(data.result);
                 }
                 else{
                      var data = JSON.stringify(data);

                      data = JSON.parse(data);

                      var table = document.getElementById('table');

                      while(table.hasChildNodes())
                         {
                            table.removeChild(table.firstChild);
                         }


                      var row = table.insertRow(0);
                      var cell1 = row.insertCell(0);
                      cell1.innerHTML = data.result;

                      var first_tr = document.createElement('tr');
                      first_tr.setAttribute('id', 'title-row');

                      document.getElementById("table").insertBefore(first_tr, table.children[0]);

                      first_tr.innerHTML = '<td>Answer</td>';

                 }
              },
              error: function (XHR, status, error) {
                 console.log('Error: ', error);
              }
           });}
      }

