from core.services.github import get_data

def contact_links(request):
    return {
        "contact": get_data("contact.txt")
    }

def global_data(request):
    return {
        "skills": get_data("skills.txt")
    }

