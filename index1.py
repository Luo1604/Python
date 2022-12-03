<html>
  <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
      <title>My First Page</title>
  </head>
  <body>
    <py-script>
      from pyodide.http import pyfetch
      import json
      import asyncio
      import re
      response = await pyfetch(url="https://www.andreasjakl.com/raycast-anchor-placing-ar-foundation-holograms-part-3/", method="GET")
      cal= str('C')
      output = f'{await response.json()}'
      def stemming(content):  
        stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
        stemmed_content = stemmed_content.lower()
        stemmed_content = stemmed_content.split()
        return stemmed_content
      
      
      print(stemming(output))
     
      
      </py-script>
    
  </body>
</html>
