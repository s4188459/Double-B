def get_page_html(form_data):
    print("About to return the home page...")
    page_html="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <p>Hello world! This page was generated from the code in page_1.py. You can go to a page below...</p>
        <p><a href="page_2.html">Page 2</a></p>
        <p><a href="page_3.html">Page 3</a></p>
    </body>
    </html>
    """
    return page_html