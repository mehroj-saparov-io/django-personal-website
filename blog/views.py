from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from django.core.cache import cache

import requests
import json

# =====================================================
# GITHUB DATA LOADER (GitHub = Mini CMS)
# =====================================================

GITHUB_BASE_URL = "https://raw.githubusercontent.com/mehroj-saparov-io/data/main"
CACHE_TIMEOUT = 300  # 5 minutes


def load_github_txt(filename: str):
    """
    GitHub raw txt (JSON format) faylni o‘qib Python list/dict qaytaradi
    """
    url = f"{GITHUB_BASE_URL}/{filename}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        print(f"[GitHub load error] {filename} -> {e}")
        return []


def get_data(filename: str):
    """
    Cache bilan GitHub data olish
    """
    cache_key = f"github_data_{filename}"
    data = cache.get(cache_key)

    if data is None:
        data = load_github_txt(filename)
        cache.set(cache_key, data, CACHE_TIMEOUT)

    return data


# =====================================================
# HOME
# =====================================================

def home_view(request: HttpRequest) -> HttpResponse:
    skills = [
        "Python", "Django", "FastAPI",
        "PostgreSQL", "Redis", "Docker",
        "Git", "Linux", "REST"
    ]

    blogs = get_data("blogs.txt")
    latest_blogs = blogs[:3]

    return render(request, "home.html", {
        "skills": skills,
        "latest_blogs": latest_blogs,
    })


# =====================================================
# BLOG LIST (Pagination)
# =====================================================

def blog_view(request: HttpRequest) -> HttpResponse:
    blogs = get_data("blogs.txt")

    paginator = Paginator(blogs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog.html", {
        "blogs": page_obj
    })


# =====================================================
# BLOG DETAIL
# =====================================================

def blog_detail_view(request, slug):
    blogs = get_data("blogs.txt")

    blog = next(
        (b for b in blogs if b.get("slug") == slug),
        None
    )

    if not blog:
        return HttpResponse("Blog not found", status=404)

    return render(request, "blog_detail.html", {
        "blog": blog
    })



# =====================================================
# ABOUT
# =====================================================

def about_view(request: HttpRequest) -> HttpResponse:
    skills = [
        "Python", "Django", "FastAPI",
        "PostgreSQL", "Redis",
        "Docker", "Git", "Linux", "REST APIs"
    ]

    return render(request, "about.html", {
        "skills": skills
    })


# =====================================================
# PROJECTS
# =====================================================

def projects_view(request: HttpRequest) -> HttpResponse:
    projects = get_data("projects.txt")

    return render(request, "projects.html", {
        "projects": projects
    })


# =====================================================
# LECTURES (Filter + Pagination)
# =====================================================

def lectures_view(request: HttpRequest) -> HttpResponse:
    lectures = get_data("lectures.txt")
    category = request.GET.get("category")

    filtered_lectures = lectures
    if category:
        filtered_lectures = [
            l for l in lectures
            if l.get("category", "").lower() == category.lower()
        ]

    paginator = Paginator(filtered_lectures, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Category counts
    categories = {}
    for lecture in lectures:
        cat = lecture.get("category", "Other")
        categories[cat] = categories.get(cat, 0) + 1

    sorted_categories = sorted(
        categories.items(),
        key=lambda x: x[1],
        reverse=True
    )

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


# =====================================================
# CONTACT
# =====================================================

def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")
