from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from .models import Comment


def get_filtered_comments(request):
    comments = Comment.objects.all()
    post_id = request.GET.get("post_id")

    if post_id and post_id.isdigit():
        comments = comments.filter(post_id=post_id)
    elif post_id:
        comments = comments.none()

    return comments


@require_GET
def comment_list(request):
    comments = get_filtered_comments(request)

    return render(
        request,
        "comments/comment_list.html",
        {
            "comments": comments,
            "post_id": request.GET.get("post_id", ""),
        },
    )


@require_GET
def comment_list_api(request):
    comments = get_filtered_comments(request)

    return JsonResponse(
        {
            "count": comments.count(),
            "results": [comment.to_dict() for comment in comments],
        }
    )


@require_GET
def comment_detail_api(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return JsonResponse(comment.to_dict())
