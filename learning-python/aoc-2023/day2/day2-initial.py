import re

def parse_game_data(line):
    # Split the line into parts
    parts = line.split(':')
    
    # Extract game name and results
    game_name = parts[0].strip()
    results = parts[1].strip().split(';')
    
    # Parse individual results for each game
    game_results = []
    for result in results:
        result_dict = {}
        # Split each result into color and count
        color_count_pairs = result.strip().split(', ')
        for pair in color_count_pairs:
            count, color = pair.split()
            result_dict[color.capitalize()] = int(count)
        game_results.append(result_dict)
    
    return game_name, game_results

def read_data_from_file(filename):
    games_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            game_name, game_results = parse_game_data(line)
            games_dict[game_name] = game_results
    return games_dict

def count_not_possible(game_dict):
    cubes_actual = {'Red': 12, 'Green': 13, 'Blue': 14}
    games_not_possible = []
    for game, results_list in games_dict.items():
        for result in results_list:
            for color, count in result.items():
                if cubes_actual[color] < count:
                    # print(f"Game {game} not possible.\nCube of color {color} actually have: {cubes_actual[color]}\nGame said we pulled {count} for that same color")
                    if game in games_not_possible:
                        continue
                    else:
                        games_not_possible.append(game)
    return games_not_possible

def sum_possible(games_dict, not_possible):
    games_possible = []
    for game in games_dict.keys():
        if game not in not_possible:
            games_possible.extend(re.findall(r'\d+', game))
            # print(games_possible)
    return sum(map(int, games_possible))



# Example usage
filename = 'day2input.txt'  # Replace with the actual file name
games_dict = read_data_from_file(filename)
print(sum_possible(games_dict, count_not_possible(games_dict)))


