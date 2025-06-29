from celery import shared_task

@shared_task
def send_welcome_email(email):
    # Implement your email logic
    return f"Sent welcome email to {email}"
