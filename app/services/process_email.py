import os

def process_email(all_valid_emails, chunk, company_name):
    #write emails to a txt file 
    write_emails_to_file(set(all_valid_emails), filename=f"{company_name}_valid_emails.txt")

    #process emails over SMTP
    return "process_email"

def write_emails_to_file(email_set, filename="valid_emails.txt"):
    downloads_path = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_path, filename)

    with open(file_path, "w") as f:
        for email in sorted(email_set):
            f.write(email + "\n")

    print(f"✅ Emails saved to {file_path}")