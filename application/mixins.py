from django.core.cache import cache
from django.core.paginator import Paginator


class PaginatedCacheMixin:
    cache_timeout = 60 * 3  # Cache timeout in seconds (e.g., 15 minutes)

    def get_queryset(self):
        # Cashe queryset
        cache_key = f"{self.request.path}_queryset"
        cached_queryset = cache.get(cache_key)

        if cached_queryset is None:
            queryset = super().get_queryset()
            cache.set(cache_key, queryset, self.cache_timeout)
        else:
            queryset = cached_queryset

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get data from cash
        cache_key = f"{self.request.path}_queryset"
        queryset = cache.get(cache_key)

        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context[self.context_object_name] = page_obj
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        return context
