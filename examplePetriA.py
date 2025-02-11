from PetriDish import PetriDish
from HTGmethods import selectGSCrandLength, selectAll, selectTopN
from Task import TaskClump

def run():

    ptA = PetriDish(
            size = (400, 300),
            nametag = "A",
            population_size=50,
            robot_data = {
                'max_neighbours' :  5,
                'max_velocity' :    4.0,
                'sense_radius':     50.0,
                'diffuse_rate':     10, 
                'act_rate':         1,
                },
            htg_method = lambda x: selectGSCrandLength(x, min_length=2, max_length=4),
            task = TaskClump(min_fitness=0, max_fitness=100.0),
            fitness_selection_method = lambda x: selectTopN(x, top_n=15),
            visuals = {
                'colour_A'      : [100.0, 100.0, 100.0],
                'colour_B'      : [0.0, 225.0, 0.0],
                'background'    : [250.0, 220.0, 180.0],
                'draw_radius'   : False,
                'draw_transfer' : True
                },
            save_interval=1000,
            record_interval = 10,
            interaction_mode = False,
            )
    #ptA = PetriDish()
    ptA.run()

if __name__ == "__main__":
    run()
