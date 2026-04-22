def get_page_html(form_data):
    print("About to return page_3...")
    page_html="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Page 3</title>
    </head>
    <body>
    <p>This page is an example of taking inputs from a web page and using them in Python. 
        To keep this example simple, it does not validate the inputs. Refer to page_3.py for the code...</p>
    <form action="/page_3.html">
        <label for="first_number">First number</label>
        <input name="first_number" type="text">
        <label for="second_number">Second number</label>
        <input name="second_number" type="text">
        <input type="submit" value="Add them!">
    </form>
    """
    #In web pages (HTML), users inputs are taken through <form> elements. When they submit the form, the data is sent
    #through to the page in the form's "action" attribute (in this case, this same page). The get_page_html function
    #of the action page receives this data via the 'form_data' dictionary/object.
    
    #By calling form_data.get with the name of the HTML input field that we want, our python code can access the value that was entered
    #on the web page. As some input fields such as drop down lists can have multiple values, form_data.get returns
    #a list, even if there's only one value per input field.
    #If no values were sent through by the web page, the None value is received.
    list_first_number = form_data.get('first_number')
    list_second_number = form_data.get('second_number')
    
    
    #Before proceeding further, we check if there were any data sent by the webpage at all by checking for None values
    if (list_first_number!=None and list_second_number!=None):
        #At this point we know list_first_number and list_second_number are actual lists but wait...
        #As these values come from outside of the program, they are captured as strings, even if the user entered numbers!
        #We need to get the value (the value at index 0, which is the only value of that list) and then convert to float
        #so that we can perform calculations later.
        first_number = float(list_first_number[0])
        second_number = float(list_second_number[0])
        
        #From here onwards, we can do anything we want with the numbers.
        answer = first_number + second_number
        page_html += f"<p>{first_number} plus {second_number} is {answer}</p>"
    else:
        page_html += "<p>Enter some values and I will add them for you!</p>"
    
    page_html+="""
        <p>Back to the <a href="/">home</a> page</p>
    </body>
    </html>
    """
    return page_html