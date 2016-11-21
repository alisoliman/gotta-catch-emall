width(2).
height(2).
number_of_pokemons(1).
poke_nums(1).
egg_time(10).
start_x(1).
start_y(1).
end_x(2).
end_y(1).
wall(1, 1, 1, 0).
wall(1, 0, 1, 1).

wall(1, 1, 0, 1).
wall(0, 1, 1, 1).
wall(1, 2, 1, 3).
wall(1, 3, 1, 2).
wall(1, 2, 0, 2).
wall(0, 2, 1, 2).

wall(1,1,1,2).
wall(1,2,1,1).
wall(2,2,3,2).
wall(3,2,2,2).

wall(2,2,2,3).
wall(2,3,2,2).

wall(2,1,3,1).
wall(3,1,2,1).

wall(2,1,2,0).
wall(2,0,2,1).
pokemons([(2, 1)]).
has_pokemon(1, 2).

helper([]).

helper([(X,Y)|T]):-
	(
		has_pokemon(X,Y),
		helper(T)
	).


del(X,[],[]).
del(X,[X|Tail],Tail).
del(X,[Y|Tail],[Y|Tail1]):-del(X,Tail,Tail1).

pokemon_exists(X, Y, P, P2):-
	(
		(	has_pokemon(X, Y),
			del((X, Y), P, P2)
		);
		(
			\+has_pokemon(X, Y),
			P2 = P
		)

	).

stance(X, Y, [], N, s0):-
	(
		start_x(X),
		start_y(Y),
		egg_time(N)
	).

stance(X, Y, P, N, result(A, S)):-
		(	A = move_right,
		X1 is X-1,
		\+wall(X1, Y, X, Y),
		pokemon_exists(X, Y, P, P2),
		(	(egg_time(H), N1 @< H, N1 is N+1 );
			(N1 is N)
		),
		stance(X1, Y, P2, N1, S)
	);
	(	A = move_down,
		Y1 is Y+1,
		\+wall(X, Y1, X, Y),
		pokemon_exists(X, Y, P, P2),
		(	(egg_time(H), N1 @< H, N1 is N+1 );
			(N1 is N)
		),
		stance(X, Y1, P2, N1, S)
	);
	(	A = move_up,
		Y1 is Y-1,
		\+wall(X, Y1, X, Y),
		pokemon_exists(X, Y, P, P2),
		(	(egg_time(H), N1 @< H, N1 is N+1 );
			(N1 is N)
		),
		stance(X, Y1, P2, N1, S)
		);
	(	A = move_left,
		X1 is X+1,
		\+wall(X1, Y, X, Y),
		pokemon_exists(X, Y, P, P2),
		(	(egg_time(H), N1 @< H, N1 is N+1 );
			(N1 is N)
		),
		stance(X1, Y, P2, N1, S)
	).