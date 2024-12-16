from bottle import route, request, run, get, post, template

@route('/notes')
def fn_notes():
    return '''
    <form action="/notes" method="post">
            Notes: <input name="form_notes" type="textarea" rows="4" cols="50"/>
            <input value="Save" type="submit" />

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" cols="40" placeholder="Enter your message"></textarea><br><br>
        </form>
    '''

@route('/notes', method='POST')
def fn_savenotes():
    lcl_notes = request.forms.form_notes
    lcl_notes2 = request.forms.message
    global gbl_notes
    gbl_notes = lcl_notes + lcl_notes2
    print ("fn_savenotes" + gbl_notes)
    return "<p>Notes saved.</p>"
    

@route('/retrieve')
def fn_displaynotes():
    print ("fn_displaynotes" + gbl_notes)
    return template ("<br>Notes: {{display_notes}}<br>", display_notes=gbl_notes)


run (host='0.0.0.0', port=8080)