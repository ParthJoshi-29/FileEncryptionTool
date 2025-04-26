if not uploaded_file:
    flash("No file uploaded!", "danger")
    return redirect(request.url)
