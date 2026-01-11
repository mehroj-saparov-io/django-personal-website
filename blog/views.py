from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator

from core.services.github import get_data, load_github_html


# =====================================================
# HOME
# =====================================================

def home_view(request: HttpRequest) -> HttpResponse:
    skills = get_data("skills.txt")

    blogs = get_data("blogs.txt")
    latest_blogs = blogs[:3]

    return render(request, "home.html", {
        "skills": skills,
        "latest_blogs": latest_blogs,
    })


# =====================================================
# BLOG LIST
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

def blog_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    blogs = get_data("blogs.txt")

    blog = next(
        (b for b in blogs if b.get("slug") == slug),
        None
    )

    if not blog:
        return HttpResponse("Blog not found", status=404)

    blog_content = ""
    if blog.get("content"):
        blog_content = load_github_html(
            f"blogs/{blog['content']}"
        )

    return render(request, "blog_detail.html", {
        "blog": blog,
        "blog_content": blog_content
    })


# =====================================================
# ABOUT
# =====================================================

def about_view(request: HttpRequest) -> HttpResponse:
    skills = get_data("skills.txt")

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
# LECTURES
# =====================================================

def lectures_view(request: HttpRequest) -> HttpResponse:
    all_lectures = get_data("lectures.txt")
    category = request.GET.get("category")

    # ---------- FILTER ----------
    lectures = all_lectures
    if category:
        lectures = [
            l for l in all_lectures
            if category.lower() in [
                c.lower() for c in l.get("category", [])
            ]
        ]

    # ---------- PAGINATION ----------
    paginator = Paginator(lectures, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # ---------- CATEGORY COUNTS ----------
    categories = {}
    for lecture in all_lectures:
        for cat in lecture.get("category", []):
            categories[cat] = categories.get(cat, 0) + 1

    sorted_categories = sorted(
        categories.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top_categories = sorted_categories[:2]
    other_categories = sorted_categories[2:]

    return render(request, "lectures.html", {
        "page_obj": page_obj,
        "total_count": len(all_lectures),
        "top_categories": top_categories,
        "other_categories": other_categories,
        "current_category": category,
    })


# =====================================================
# CONTACT
# =====================================================

def contact_view(request: HttpRequest) -> HttpResponse:
    # contact links context_processor orqali keladi
    return render(request, "contact.html")
