def generate_business_card(name, title, company, email, phone):
    card = f"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃    {name}
    ┃    {title}
    ┃    {company}
    ┃    Email: {email}
    ┃    Phone: {phone}
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    return card


name = "Alex MacDonald "
title = "Network Engineer"
company = "Mitel Netsoltuions"
email = "clexander.macdonald@mitel.com"
phone = "775-954-5330"

business_card = generate_business_card(name, title, company, email, phone)
print(business_card)
