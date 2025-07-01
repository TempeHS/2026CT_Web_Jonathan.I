git add -A git commit -m "add readme" git push

player_name = prompt("enter your name"); alert("i dont like " + player_name); alert("i dont like " + player_name); player_guess = prompt("Rock Paper Scissors"); computer_guess = randonIntFromInterval(1, 3);

if (player_guess == computer_guess) { document.getElementById("user_feedback").innerHTML = "Correct"; } else { document.getElementById("user_feedback").innerHTML = "Incorrect\n" + "It was " + computer_guess; }

function randonIntFromInterval(min, max) { //min and max included return Math.floor(Math.random() * (max - min + 1) + min); }
