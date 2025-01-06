

# TODO here we need to move define the tasks 
# we can define the task and then invoke the function here 

# example 

# @app.task(name="send-verification-token")
# def send_verification_token(email, token):
#     token_url = f"{base_settings.frontend_base_url}/auth/verify?token={token}"
#     body = MIMEText(get_email_string("verification").replace("%token_url%", token_url), "html")
#     message = get_email_message(email, "AI Hub - Verify your email address", body)

#     return send_email(message)