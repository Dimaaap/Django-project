def check_form_errors_service(form: callable):
    for i in form.errors:
        return form.errors[i][0]

