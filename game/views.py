import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Game choices
choices = ['rock', 'paper', 'scissors']

# View for the main game page
def game_view(request):
    return render(request, 'game/game.html')

# View for the result of the game
def result_view(request):
    user_choice = request.POST.get('choice')
    computer_choice = random.choice(choices)

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    }
    return render(request, 'game/result.html', context)

# View to play again
def play_again_view(request):
    return HttpResponseRedirect(reverse('game:game'))
