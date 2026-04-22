def get_page_html(form_data):
    print("About to return page_2...")
    page_html="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Page 2</title>
    </head>
    <body>
    <p>This page is an example of content can be generated dynamically. The repeating lines below were made using a loop in page_2.py</p>
    <pre>"""
    
    for count in range(0,10):
        page_html+= f"Hello world {count}!\n"
        
    page_html+="""</pre>
        <p>Back to the <a href="/">home</a> page</p>
    </body>
    </html>
    """
    return page_html