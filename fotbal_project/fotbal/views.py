from django.shortcuts import render, get_object_or_404,  redirect
from .models import Team, Player, Match, Goal
from .forms import PlayerForm

def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('fotbal:players_list')  # přesměruj na seznam hráčů nebo jinam
    else:
        form = PlayerForm()
    return render(request, 'fotbal/player_form.html', {'form': form})


def home(request):
    teams = Team.objects.all()[:5]  # například prvních 5 týmů
    return render(request, 'fotbal/home.html', {'teams': teams})

def teams(request):
    teams = Team.objects.all()
    return render(request, 'fotbal/teams.html', {'teams': teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = Player.objects.filter(team=team).order_by('last_name', 'first_name')
    return render(request, 'fotbal/team_detail.html', {'team': team, 'players': players})

def players(request):
    players = Player.objects.all()
    return render(request, 'fotbal/players.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'fotbal/player_detail.html', {'player': player})

def matches(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'fotbal/matches.html', {'matches': matches})

def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    events = []
    if match.description:
        for line in match.description.split('\n'):
            if ". minuta:" in line:
                minute_str, desc = line.split(". minuta:", 1)
                minute = minute_str.strip()
                desc = desc.strip()
                desc_lower = desc.lower()
                css_class = ""
                if "gól" in desc_lower:
                    css_class = "event-goal"
                elif "žlutá karta" in desc_lower:
                    css_class = "event-yellow"
                elif "červená karta" in desc_lower:
                    css_class = "event-red"
                events.append({'minute': minute, 'desc': desc, 'css_class': css_class})
            else:
                events.append({'minute': '', 'desc': line, 'css_class': ''})
    else:
        events = []
    return render(request, 'fotbal/match_detail.html', {'match': match, 'events': events})


def goal_graph(request, match_id, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id, match_id=match_id)
    match = goal.match
    home_players = match.home_team.player_set.all()
    away_players = match.away_team.player_set.all()
    return render(request, 'fotbal/goal_graph.html', {
        'goal': goal,
        'match': match,
        'home_players': home_players,
        'away_players': away_players,
    })
