width(2).
height(2).
number_of_pokemons(1).
poke_nums(1).
egg_time(2).
start_x(1).
start_y(1).
end_x(1).
end_y(2).
%% wall(1, 1, 1, 1).
%% wall(1, 2, 1, 1).
wall(1, 1, 1, 0).
wall(1, 0, 1, 1).
%% wall(1, 1, 2, 1).
%% wall(2, 1, 1, 1).
wall(1, 1, 0, 1).
wall(0, 1, 1, 1).
%% wall(1, 2, 1, 2).
%% wall(1, 3, 1, 2).
%% %% wall(1, 2, 1, 1).
%% %% wall(1, 1, 1, 2).
%% wall(1, 2, 2, 2).
%% wall(2, 2, 1, 2).
%% wall(1, 2, 0, 2).
wall(0, 2, 1, 2).
%% wall(2, 1, 2, 1).
%% wall(2, 2, 2, 1).
wall(2, 1, 2, 0).
wall(2, 0, 2, 1).
%% wall(2, 1, 3, 1).
%% wall(3, 1, 2, 1).
%% wall(2, 1, 1, 1).
%% wall(1, 1, 2, 1).
%% wall(2, 2, 2, 2).
%% wall(2, 3, 2, 2).
%% wall(2, 2, 2, 1).
%% wall(2, 1, 2, 2).
%% wall(2, 2, 1, 2).
%% wall(1, 2, 2, 2).
has_pokemon(1, 1).

pokemon_exists(X, Y, P, P1, Plist, Plist2):-
	(	
		has_pokemon(X, Y),
		\+member((X, Y), Plist),
		append([(X, Y)],Plist, Plist2),
		P1 is P+1
	).

stance(1, 1, 1, [(1,1)], 2, s0).

stance(X, Y, P, Plist, N, result(A, S)):-
	(	A = move_left, 
		X1 is X+1, 
		X \= 0, 
		\+wall(X1, Y, X, Y), 
		N1 is N+1, 
		pokemon_exists(X, Y, P, P1, Plist, Plist2),
		stance(X1, Y, P1, Plist2, N1, S)
	);
	(	A = move_right, 
		X1 is X-1,
		X \= 3, 
		\+wall(X1, Y, X, Y), 
		N1 is N+1,
		pokemon_exists(X, Y, P, P1, Plist, Plist2),
		stance(X1, Y, P1, Plist2, N1, S)
	);
	(	A = move_down, 
		Y1 is Y+1,
		Y \= 0, 
		\+wall(X, Y1, X, Y), 
		N1 is N+1, 
		pokemon_exists(X, Y, P, P1, Plist, Plist2),
		stance(X, Y1, P1, Plist2, N1, S)
	);
	(	A = move_up, 
		Y1 is Y-1, 
		Y \= 3, 
		\+wall(X, Y1, X, Y), 
		N1 is N+1, 
		pokemon_exists(X, Y, P, P1, Plist, Plist2),
		stance(X, Y1, P1, Plist2, N1, S)
	).













