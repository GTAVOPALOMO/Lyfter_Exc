def create_sorted_file(p_path, p_list):
    with open(p_path, "w") as v_file:
        for item in p_list:
            v_file.write(item)

def read_file(p_path):
    with open(p_path) as p_file:
        return p_file.readlines()

songs = read_file('canciones.txt')
songs.sort()
create_sorted_file('sorted_songs.txt',songs)

