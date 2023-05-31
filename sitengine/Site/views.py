from .models import Tag, Script, Man, Link, Command, Archivefile
from django.views.generic import View
from .utils import *
from django.db.models import Q


def head_page(request):
    return render(request, 'Site/index.html')


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'Site/tag_detail.html'


class ScriptDetail(ObjectDetailMixin, View):
    model = Script
    template = 'Site/script_detail.html'


class ManDetail(ObjectDetailMixin, View):
    model = Man
    template = 'Site/man_detail.html'


class CommandDetail(ObjectDetailMixin, View):
    model = Command
    template = 'Site/command_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'Site/tags_list.html', context={'tags': tags})


def scripts_list(request):
    scripts = Script.objects.all()
    return render(request, 'Site/scripts_list.html', context={'scripts': scripts})


def links_list(request):
    links = Link.objects.all()
    return render(request, 'Site/links_list.html', context={'links': links})


def mans_list(request):
    mans = Man.objects.all()
    return render(request, 'Site/mans_list.html', context={'mans': mans})


def commands_list(request):
    commands = Command.objects.all()
    return render(request, 'Site/commands_list.html', context={'commands': commands})


def archivefiles_list(request):
    archivefiles = Archivefile.objects.all()
    return render(request, 'Site/archivefiles_list.html', context={'archivefiles': archivefiles})


def search_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        scripts = Script.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        links = Link.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        commands = Command.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        mans = Man.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        context = {
            'search_query': search_query,
            'scripts': scripts,
            'links': links,
            'commands': commands,
            'mans': mans
        }
        return render(request, 'Site/search_list.html', context=context)
