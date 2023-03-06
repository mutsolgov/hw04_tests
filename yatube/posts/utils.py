from django.core.paginator import Paginator

NUMBER_OF_POSTS_PER_PAGE = 10


def paginations(request, data_list):

    paginator = Paginator(data_list, NUMBER_OF_POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return page_obj
