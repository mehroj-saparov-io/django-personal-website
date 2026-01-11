from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator


# ====== FAKE BLOG DATA ======
blogs = [
    {
        "id": 1,
        "title": "Clean Architecture in Django Projects",
        "excerpt": "How to structure Django projects for long-term maintainability and scalability.",
        "published_date": "Jan 10, 2026",
        "reading_time": "7 min read",
        "tags": ["Django", "Architecture", "Best Practices"],
    },
    {
        "id": 2,
        "title": "Building REST APIs with Django REST Framework",
        "excerpt": "A practical guide to building clean, secure, and scalable REST APIs using DRF.",
        "published_date": "Jan 7, 2026",
        "reading_time": "9 min read",
        "tags": ["Django", "REST", "API"],
    },
    {
        "id": 3,
        "title": "PostgreSQL Performance Tips for Backend Developers",
        "excerpt": "Indexes, query optimization, and common mistakes when working with PostgreSQL.",
        "published_date": "Jan 3, 2026",
        "reading_time": "8 min read",
        "tags": ["PostgreSQL", "Database", "Performance"],
    },
    {
        "id": 4,
        "title": "Dockerizing Python Applications the Right Way",
        "excerpt": "Best practices for containerizing Python apps for development and production.",
        "published_date": "Dec 29, 2025",
        "reading_time": "6 min read",
        "tags": ["Docker", "DevOps", "Python"],
    },
    {
        "id": 5,
        "title": "Async in Python: When and When Not to Use It",
        "excerpt": "Understanding asyncio, async views, and performance trade-offs in Python.",
        "published_date": "Dec 24, 2025",
        "reading_time": "10 min read",
        "tags": ["Python", "Async", "Backend"],
    },
    {
        "id": 6,
        "title": "Clean Architecture in Django Projects",
        "excerpt": "How to structure Django projects for long-term maintainability and scalability.",
        "published_date": "Jan 10, 2026",
        "reading_time": "7 min read",
        "tags": ["Django", "Architecture", "Best Practices"],
    },
]

projects = [
    {
        "name": "Personal Blog Platform",
        "description": "A minimal personal blog built with Django and Tailwind CSS.",
        "url": "https://github.com/yourusername/personal-blog",
    },
    {
        "name": "REST API with Django REST Framework",
        "description": "Scalable REST API using DRF and PostgreSQL.",
        "url": "https://github.com/yourusername/drf-api",
    },
]

# ===== DEFAULT LECTURES DATA (ID BOR) =====
lectures = [
    {"id": 1, "title": "Django Full Course – Part 1", "youtube_id": "bhZfQCj-yYg", "category": "Django"},
    {"id": 2, "title": "Django Models Explained", "youtube_id": "bhZfQCj-yYg", "category": "Django"},
    {"id": 3, "title": "Django REST Framework Basics", "youtube_id": "bhZfQCj-yYg", "category": "Django"},
    {"id": 4, "title": "Django Pagination Tutorial", "youtube_id": "bhZfQCj-yYg", "category": "Django"},
    {"id": 5, "title": "Django Authentication", "youtube_id": "bhZfQCj-yYg", "category": "Django"},
    {"id": 6, "title": "Django Deployment Guide", "youtube_id": "bhZfQCj-yYg", "category": "Django"},
    {"id": 7, "title": "Python Basics", "youtube_id": "bhZfQCj-yYg", "category": "Python"},
    {"id": 8, "title": "Python OOP Explained", "youtube_id": "bhZfQCj-yYg", "category": "Python"},
    {"id": 9, "title": "Async Python Explained", "youtube_id": "bhZfQCj-yYg", "category": "Python"},
    {"id": 10, "title": "Python Tips & Tricks", "youtube_id": "bhZfQCj-yYg", "category": "Python"},
]

# ====== HOME ======
def home_view(request: HttpRequest) -> HttpResponse:
    skills = [
        "Python", "Django", "FastAPI",
        "PostgreSQL", "Redis", "Docker",
        "Git", "Linux", "REST"
    ]

    latest_blogs = blogs[:3]

    return render(request, "home.html", {
        "skills": skills,
        "latest_blogs": latest_blogs,
    })


# ====== BLOG LIST (pagination) ======
def blog_view(request: HttpRequest) -> HttpResponse:
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog.html", {
        "blogs": page_obj
    })


# ====== BLOG DETAIL ======
def blog_detail_view(request: HttpRequest, blog_id: int) -> HttpResponse:
    blog = next((b for b in blogs if b["id"] == blog_id), None)

    if not blog:
        return HttpResponse("Blog not found", status=404)

    return render(request, "blog_detail.html", {"blog": blog})


# ====== ABOUT ======
def about_view(request: HttpRequest) -> HttpResponse:
    skills = [
        "Python", "Django", "FastAPI",
        "PostgreSQL", "Redis",
        "Docker", "Git", "Linux", "REST APIs"
    ]
    return render(request, "about.html", {"skills": skills})


# ====== PROJECTS ======
def projects_view(request: HttpRequest) -> HttpResponse:
    return render(request, "projects.html", {"projects": projects})


# ====== LECTURES ======
def lectures_view(request: HttpRequest) -> HttpResponse:
    category = request.GET.get("category")

    filtered_lectures = lectures
    if category:
        filtered_lectures = [
            l for l in lectures if l["category"].lower() == category.lower()
        ]

    paginator = Paginator(filtered_lectures, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # category counts
    categories = {}
    for lecture in lectures:
        categories[lecture["category"]] = categories.get(lecture["category"], 0) + 1

    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    top_categories = sorted_categories[:2]
    other_categories = sorted_categories[2:]

    context = {
        "page_obj": page_obj,
        "total_count": len(lectures),
        "top_categories": top_categories,
        "other_categories": other_categories,
        "current_category": category,
    }

    return render(request, "lectures.html", context)

# ====== CONTACT ======
def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")
