import requests
import json
from django.core.cache import cache

GITHUB_BASE_URL = "https://raw.githubusercontent.com/mehroj-saparov-io/data/main"
CACHE_TIMEOUT = 300


def load_github_txt(filename: str):
    url = f"{GITHUB_BASE_URL}/{filename}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return json.loads(response.text)
    except Exception as e:
        print(f"[GitHub load error] {filename} -> {e}")
        return {}


def load_github_html(path: str) -> str:
    url = f"{GITHUB_BASE_URL}/{path}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[GitHub HTML load error] {path} -> {e}")
        return "<p>Content not available.</p>"


def get_data(filename: str):
    cache_key = f"github_data_{filename}"
    data = cache.get(cache_key)

    if data is None:
        data = load_github_txt(filename)
        cache.set(cache_key, data, CACHE_TIMEOUT)

    return data
